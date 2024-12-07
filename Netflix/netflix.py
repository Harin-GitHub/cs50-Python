import sys
import requests
import json
import csv
import re


def main():
    if len(sys.argv) == 3:
        for i in [1, 2]:
            if not re.search(r".+\.csv$", sys.argv[i]) and i == 2:
                sys.exit("Usage: python input.csv output.csv")
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File does not exist")

        tracks = read(file)


def read(file):
    reader = csv.DictReader(file)

    genres = {}
    artists = {}
    count_genre, count_artist = 0, 0

    for song in reader:
        response = requests.get(
            f"https://itunes.apple.com/search?term={song['track']}+{song['artist']}&entity=song&media=music&songTerm={song['track']}&artistTerm={song['artist']}&limit=1"
        )
        response = response.json()
        song_info = []
        for j in ["artistName", "primaryGenreName"]:
            result = add(response, j)
            if result != False:
                song_info.append(result)
            else:
                song_info.append("")
        if song_info[0] and song_info[1] != None:
            if song["artist"].lower() == song_info[0].lower():
                artists.update({song_info[0]: count_artist + 1})

                if song_info[1] != "":
                    if "/" in song_info[1]:
                        list = split(song_info[1])
                        for genre in list:
                            genres.update({genre: count_genre + 1})
                    else:
                        genres.update({song_info[1]: count_genre + 1})

    print(genres, artists)
    reccomend([genres, artists])


def add(response, key):
    for result in response["results"]:
        if key in result:
            return result[key]
        return False


def split(str):
    start = 0
    end = len(str) - 1
    list = []
    while True:
        index = str.find("/", start, end)
        if index != -1:
            list.append(str[start:index])
            start = index + 1
        else:
            list.append(str[start:])
            return list


def reccomend(list):
    for dic in list:
        for key in dic:
            percent = float((dic[key] / len(dic)) * 100)
            dic.update({key: percent})
    print(list)
    


if __name__ == "__main__":
    main()
