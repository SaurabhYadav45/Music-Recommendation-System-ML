import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

CLIENT_ID = "bd3552464b90445cb3f452f9b3afcae9"
CLIENT_SECRET = "9d2639aaa3e4463392914151963e4da6"

import gdown

similarity_url = "https://drive.google.com/uc?id=1F7bMlMadWdl-6uFSZ0b2lqS-CHerHu_d"

# Local filenames
similarity_file = "similarity.pkl"
df_file = "df.pkl"  # Already present locally

# Download similarity.pkl if not present
if not os.path.exists(similarity_file):
    gdown.download(similarity_url, similarity_file, quiet=False)

# Load the similarity matrix
similarity = pickle.load(open(similarity_file, "rb"))

# Load df.pkl (which is already present locally)
music = pickle.load(open(df_file, "rb"))


# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        # Song Url
        song_url = track["external_urls"]["spotify"]
        print(album_cover_url)
        print(song_url)
        return album_cover_url, song_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png", None

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_urls = []
    for i in distances[1:11]:
        # fetch the movie poster
        artist = music.iloc[i[0]].artist
        #
        song_name = music.iloc[i[0]].song
        print(artist)
        print(music.iloc[i[0]].song)

        album_cover_url, song_url = get_song_album_cover_url(song_name, artist)

        recommended_music_posters.append(album_cover_url)
        recommended_music_urls.append(song_url)
        recommended_music_names.append(song_name)

    return recommended_music_names,recommended_music_posters, recommended_music_urls

# Set background color to black using custom CSS


st.header('Music Recommendation System')
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names,recommended_music_posters, recommended_music_urls = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        # st.image(recommended_music_posters[0], width=200)
        st.markdown(f'<img src="{recommended_music_posters[0]}" class="poster">', unsafe_allow_html=True)
        # st.markdown(f"[Listen on Spotify]({recommended_music_urls[0]})")

        st.markdown(
            f'<a href="{recommended_music_urls[0]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[0]}</a>',
            unsafe_allow_html=True
        )

    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
        
        st.markdown(
            f'<a href="{recommended_music_urls[1]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[1]}</a>',
            unsafe_allow_html=True
        )

    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
        
        st.markdown(
            f'<a href="{recommended_music_urls[2]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[2]}</a>',
            unsafe_allow_html=True
        )

    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
        
        st.markdown(
            f'<a href="{recommended_music_urls[3]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[3]}</a>',
            unsafe_allow_html=True
        )

    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
        
        st.markdown(
            f'<a href="{recommended_music_urls[4]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[4]}</a>',
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(recommended_music_names[5])
        st.image(recommended_music_posters[5])
        st.markdown(
            f'<a href="{recommended_music_urls[5]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[5]}</a>',
            unsafe_allow_html=True
        )

    with col7:
        st.text(recommended_music_names[6])
        st.image(recommended_music_posters[6])
        st.markdown(
            f'<a href="{recommended_music_urls[6]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[6]}</a>',
            unsafe_allow_html=True
        )
    with col8:
        st.text(recommended_music_names[7])
        st.image(recommended_music_posters[7])
        st.markdown(
            f'<a href="{recommended_music_urls[7]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f'Listen to {recommended_music_names[7]}</a>',
            unsafe_allow_html=True
        )
    with col9:
        st.text(recommended_music_names[8])
        st.image(recommended_music_posters[8])
        st.markdown(
            f'<a href="{recommended_music_urls[8]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f'Listen to {recommended_music_names[8]}</a>',
            unsafe_allow_html=True
        )
    with col10:
        st.text(recommended_music_names[9])
        st.image(recommended_music_posters[9])
        st.markdown(
            f'<a href="{recommended_music_urls[9]}" target="_blank" style="text-decoration: none; color: magenta; border: 2px solid #f5bd22; padding: 5px; border-radius: 5px; display: inline-block;">'
            f' Listen to {recommended_music_names[9]}</a>',
            unsafe_allow_html=True
        )


# streamlit run "c:\Users\saura\OneDrive\Documents\Desktop\Jupyter Notebook\Music Recommendation System\app.py"

