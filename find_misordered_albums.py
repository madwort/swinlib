from swinlib.database import SwinLib

SWINSIAN_FILENAME = "./Library.sqlite"


def main():
    sl = SwinLib(SWINSIAN_FILENAME)
    album = "Your Kisses Are Like Roses: Fado Recordings, 1914-1936"
    tracks = sl.get_album(album)
    # print(tracks)

    # albums = [(album, )]
    albums = sl.get_all_albums()
    misordered_albums = sl.get_misordered_albums(albums)
    print(misordered_albums)


if __name__ == "__main__":
    main()
