# lib/main.py
from config import CONN, CURSOR
from song import Song

def main():
    # Create the songs table
    Song.create_table()

    # Create and save songs
    hello = Song.create("Hello", "25")
    despacito = Song.create("Despacito", "Vida")

    # Print the song details
    print(f"hello: id={hello.id}, name={hello.name}, album={hello.album}")
    print(f"despacito: id={despacito.id}, name={despacito.name}, album={despacito.album}")

if __name__ == "__main__":
    main()
