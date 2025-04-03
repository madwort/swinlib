
from swinlib.database import SwinLib

SWINSIAN_FILENAME = "./Library.sqlite"

def main():
    sl = SwinLib(SWINSIAN_FILENAME)
    album = ("Uncharted Territories")
    tracks = sl.get_album(album)
    print(tracks)

    sl.move_album(
        album,
        '/Users/tom/Music/iTunes/iTunes Media/Music/',
        '/Volumes/Elements/Music/',
        True
    )

if __name__ == "__main__":
    main()
