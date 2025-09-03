import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

# 🔐 Fill in your own Spotify Developer credentials
SPOTIFY_CLIENT_ID = 'e4c92c4bc2bc4c85b869d61e12665a2d'
SPOTIFY_CLIENT_SECRET = '812a39970ba24a28a695293b5ee4bb83'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# def play_music(emotion):
#     query = f"{emotion} mood music"
#     results = sp.search(q=query, limit=1, type='track')

#     if results['tracks']['items']:
#         track = results['tracks']['items'][0]
#         print(f"Playing: {track['name']} by {track['artists'][0]['name']}")
#         webbrowser.open(track['external_urls']['spotify'])
#     else:
#         print("No track found for mood:", emotion)
emotion_to_song = {
    'happy': 'https://open.spotify.com/track/0cx3DUvLuL7iTJ6aUzAZNx?si=5f3e9137f0d94854',  # Replace with a Kannada happy song
    'sad': 'https://open.spotify.com/track/1sA2Ml7Uk3kuaCTA3ouzB4?si=d77cebfcd67f44b8',
    'angry': 'https://open.spotify.com/track/6kWYigBhkWT2EINUNNtYr4?si=c6d4bdbff611408b',
    'surprise': 'https://open.spotify.com/track/4aoUuflxosBouuLBmZcI7J?si=b8f4177959a7427c',
    'neutral': 'https://open.spotify.com/track/038gnuPve7s8rADCEDYsMH?si=c7fd19de86c74d19',
    'fear': 'https://open.spotify.com/track/5cniDYPxk30dUnpEjYAnAV?si=c01369c02a874cd6',
    'disgust': 'https://open.spotify.com/track/7MsH6gZMOgzohJYDLGHHVw?si=d6fd3b5648f14cdd',
}

def play_music(emotion):
    emotion = emotion.lower()  # normalize the input
    url = emotion_to_song.get(emotion)
    if url:
        print(f"Playing song for emotion: {emotion}")
        webbrowser.open(url)
    else:
        print("No predefined song for mood:", emotion)

