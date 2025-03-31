import sqlite3

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
            "SELECT dateadded from track WHERE track_id = :track_id LIMIT 1",
            data
        )
        track = res.fetchone()
        dateadded = track[0]
        return dateadded


    def get_album(self, album):
        cur = self.con.cursor()
        res = cur.execute(
            "SELECT track_id, tracknumber, dateadded, artist, title, path from track WHERE album = :album  ORDER BY tracknumber",
            (album,)
        )
        tracks = res.fetchall()
        return tracks

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

    def get_all_albums(self):
        cur = self.con.cursor()
        res = cur.execute(
            "SELECT album from track group by album"
        )
        albums = res.fetchall()
        # for album in albums:
        #     print(album[0])
        return albums

    def move_album(self, album, current_location, new_location):
        # this can also be done like
        # UPDATE track SET path = replace(path, '/PREFIX/OF/YOUR/OLD/PATH/', '/PREFIX/OF/YOUR/NEW/PATH/');
        # but in our case we want to do it selectively, and also move the files
        # ourselves...

        print(album + current_location + new_location)
        tracks = self.get_album(album)
        for track in tracks:
                old_path = track[5]
                new_path = track[5].replace(current_location, new_location)
                print(f"{old_path}")
                print(f"-> {new_path}")
