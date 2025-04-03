import os
import shutil
import sqlite3
from pathlib import Path

from swinlib.time import datetime_string_to_time_float


class SwinLib:
    def __init__(self, filename):
        self.filename = filename
        self.con = sqlite3.connect(self.filename)

    def get_a_track(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT * from track LIMIT 1")
        return res.fetchone()

    def get_dateadded_track(self):
        track_id = 1
        data = {"track_id": track_id}
        cur = self.con.cursor()
        res = cur.execute(
            "SELECT dateadded from track WHERE track_id = :track_id LIMIT 1", data
        )
        track = res.fetchone()
        dateadded = track[0]
        return dateadded

    def get_all_albums(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT album from track group by album")
        albums = res.fetchall()
        # for album in albums:
        #     print(album[0])
        return albums

    def get_album(self, album):
        cur = self.con.cursor()
        res = cur.execute(
            "SELECT track_id, tracknumber, dateadded, artist, title, path from track WHERE album = :album  ORDER BY tracknumber",
            (album,),
        )
        tracks = res.fetchall()
        return tracks

    def get_album_metadata(self, album):
        cur = self.con.cursor()
        res = cur.execute(
            "SELECT lastplayed, artist, title, path from track WHERE album = :album  ORDER BY tracknumber",
            (album,),
        )
        tracks = res.fetchall()
        return tracks

    def album_has_duplicate(self, album):
        cur = self.con.cursor()
        if album is None:
            # this covers a bunch of stuff mixed together, so we want to be cautious
            # and treat it like a duplicated album (needs special attention)
            return True
        # breakpoint()
        res = cur.execute(
            "SELECT count(path) cp FROM track WHERE album = :album GROUP BY title ORDER BY cp DESC",
            (album,),
        )
        # duplicate = res.fetchall()
        # print(duplicate)
        duplicate = res.fetchone()
        if duplicate[0] > 1:
            return True
        return False

    def album_is_stored_internal_drive(self, album):
        cur = self.con.cursor()
        if album is None:
            return
        # breakpoint()
        res = cur.execute(
            "SELECT count(*) FROM track WHERE album = :album and path like '/Users/tom/Music/%'",
            (album,),
        )
        # duplicate = res.fetchall()
        # print(duplicate)
        internal_drive = res.fetchone()

        res = cur.execute(
            "SELECT count(*) FROM track WHERE album = :album and path not like '/Users/tom/Music/%'",
            (album,),
        )
        external_drive = res.fetchone()

        if internal_drive[0] > 1 and external_drive[0] < 1:
            return True
        return False

    def album_played_since_date(self, album, datetime_string):
        cur = self.con.cursor()
        if album is None:
            return
        # breakpoint()
        res = cur.execute(
            "SELECT lastplayed FROM track WHERE album = :album ORDER BY lastplayed desc",
            (album,),
        )
        most_recently_played_track = res.fetchone()
        if most_recently_played_track[0] is not None and most_recently_played_track[
            0
        ] > datetime_string_to_time_float(datetime_string):
            return True
        return False

    def album_added_before_date(self, album, datetime_string):
        cur = self.con.cursor()
        if album is None:
            return
        # breakpoint()
        res = cur.execute(
            "SELECT dateadded FROM track WHERE album = :album ORDER BY dateadded desc",
            (album,),
        )
        most_recently_added_track = res.fetchone()
        if most_recently_added_track[0] is not None and most_recently_added_track[
            0
        ] < datetime_string_to_time_float(datetime_string):
            return True
        return False

    def get_misordered_albums(self, albums):
        # TODO: handle duplicated albums, e.g. music for large & small ensembles
        misordered_albums = set()
        for album in albums:
            album = album[0]
            tracks = self.get_album(album)
            previous_track_dateadded = 0.0
            for track in tracks:
                if track[2] < previous_track_dateadded:
                    print(album)
                    misordered_albums.add(album)
                previous_track_dateadded = track[2]
        return misordered_albums

    def move_album(self, album, current_location, new_location, dry_run=True):
        print(f"{album} - {current_location} -> {new_location}")
        tracks = self.get_album(album)
        for track in tracks:
            old_path = track[5]
            new_path = track[5].replace(current_location, new_location)
            new_directory = Path(new_path).parent

            # print(f"mkdir {new_directory}")

            print(f"{old_path} -> {new_path}")
            if dry_run:
                continue

            os.makedirs(new_directory, exist_ok=True)
            shutil.move(old_path, new_path)

            # TODO: then update the db
            # this can also be done like
            # UPDATE track SET path = replace(path, '/PREFIX/OF/YOUR/OLD/PATH/', '/PREFIX/OF/YOUR/NEW/PATH/');
            # but in our case we want to do it selectively, and also move the files
            # ourselves...
            cur = self.con.cursor()
            res = cur.execute(
                "UPDATE track SET path = :new_path WHERE path = :old_path;",
                ({"old_path": old_path, "new_path": new_path}),
            )
            print(f"tracks updated {res.rowcount}")

        if dry_run:
            return

        self.con.commit()
        print(f"{album} moved")
