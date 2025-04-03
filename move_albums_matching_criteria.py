
from swinlib.database import SwinLib

SWINSIAN_FILENAME = "./Library.sqlite"
LOCAL_LIBRARY_PATH = "/Users/tom/Music/"
REMOTE_LIBRARY_PATH = "/Volumes/WD Passport/Music/"

def main():
    sl = SwinLib(SWINSIAN_FILENAME)
    dry_run = False

    # get all album names
    albums = sl.get_all_albums()
    # albums = [
    #      # no duplicate
    #     ("Leather Blvd.", ),
    #      # duplicate
    #     ("Yan Kuba - Kora Music From Gambia", ),
    #     # Local disk, added 2022, last played 2023
    #     ("Water Music", ),
    #     # ("Freeness", ),
    # ]

    candidate_albums = [
        album[0] for album in albums if album_is_candidate(sl, album[0])
    ]

    # breakpoint()
    print(f"{len(candidate_albums)} albums to move")

    for album in candidate_albums:
        sl.move_album(album, LOCAL_LIBRARY_PATH, REMOTE_LIBRARY_PATH, dry_run)


def album_is_candidate(sl, album):
    # don't move' albums which have duplicates
    # move albums which aren't on the local hard drive
    # move "old" albums

    return (
        (not sl.album_has_duplicate(album))
        and
        sl.album_is_stored_internal_drive(album)
        and
        (not sl.album_played_since_date(album, "2024-01-01"))
        and
        sl.album_added_before_date(album, "2024-01-01")
    )

if __name__ == "__main__":
    main()
