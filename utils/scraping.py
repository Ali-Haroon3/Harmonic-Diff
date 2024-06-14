import requests
from bs4 import BeautifulSoup

def scrape_song_lyrics(song_name):
    url = f"https://genius.com/search?q={song_name.replace(' ', '%20')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract song lyrics or metadata here
    return song_lyrics

song_name = "Imagine"
lyrics = scrape_song_lyrics(song_name)
print(lyrics)
