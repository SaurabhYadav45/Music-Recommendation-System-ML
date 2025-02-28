#Music Recommendation System 🎵

A Music Recommendation System built using Machine Learning and Spotify API that suggests songs based on user input. The system analyzes song similarities and provides personalized recommendations with album covers and Spotify links.

##🚀 Features                                                                                                                                                           
###Deployment Link : https://saurabhyadav45-music-recommendation-system-ml-app-ooqcsk.streamlit.app/

🔍 Search & Select: Choose a song from the dropdown list.

🎶 Smart Recommendations: Suggests 10 similar songs based on machine learning algorithms.

🖼 Album Cover Display: Fetches album artwork from Spotify.

🎧 Spotify Integration: Provides direct links to listen on Spotify.

🌐 Deployed on Streamlit Cloud for easy access.

###🛠 Tech Stack

Frontend: Streamlit

Backend: Python, Pandas, Pickle

Machine Learning: Content-based filtering

APIs: Spotify API

Cloud Storage: Google Drive (for large files)

📂 Project Structure

├── app.py                 # Main application script
├── df.pkl                 # Pickle file containing song dataset
├── similarity.pkl         # Precomputed similarity matrix
├── requirements.txt       # Required dependencies
├── README.md              # Project documentation

🎯 How It Works

The system loads a dataset of songs and their features.

A similarity matrix (precomputed) is used to find songs similar to the selected one.

The app fetches song details and album covers using the Spotify API.

Recommendations are displayed with clickable Spotify links.

🚀 Deployment on Streamlit

The app is deployed on Streamlit Cloud. You can access it here.

🛠 Installation & Running Locally

Clone the Repository

git clone https://github.com/yourusername/music-recommendation-system-ml.git
cd music-recommendation-system-ml

Install Dependencies

pip install -r requirements.txt

Run the Streamlit App

streamlit run app.py

📦 Dependencies

Make sure you have the following installed:

streamlit
spotipy
gdown
pickle
pandas

📝 License

This project is open-source and available under the MIT License.

💡 Feel free to contribute, report issues, or suggest improvements!

