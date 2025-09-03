# Moodify 🎵😃

A **Mood-Based Music Recommendation System** that uses **real-time facial emotion recognition** to detect your mood via webcam and then automatically plays a song on Spotify that matches your current emotion.

---

## 🚀 Features

- **Real-Time Emotion Detection**  
  Uses OpenCV and a pre-trained deep learning model to detect emotions from your face via webcam.

- **Automatic Music Recommendation**  
  Plays predefined songs (via Spotify links) based on the detected emotion.

- **Multi-Emotion Support**  
  Handles moods like: Happy, Sad, Angry, Surprise, Neutral, Fear, and Disgust.

- **Cross-Platform**  
  Works on Windows, macOS, and Linux (requires Python 3.x).

---

## 🛠️ Tech Stack

- [Python 3.x](https://www.python.org/)
- [OpenCV](https://opencv.org/) for webcam and face detection
- [Spotipy](https://spotipy.readthedocs.io/en/2.19.0/) for Spotify integration
- [Spotify Web Player](https://open.spotify.com/) (opens in browser)

---

## 📦 Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/Darshanmp1/moodify.git
   cd moodiflyy
2. **Install the dependencies**
   pip install -r requirements.txt

3. Set up Spotify Developer Credentials (optional if using predefined links):

   Create an app at Spotify Developer Dashboard

   Copy the Client ID and Client Secret.

   Update the values in recommend_music.py:

   SPOTIFY_CLIENT_ID = "your_client_id"
   
   SPOTIFY_CLIENT_SECRET = "your_client_secret"
