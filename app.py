import streamlit as st
import pickle
import pandas as pd
import gdown
import os

def download_similarity_file():
    file_id = "1sNsISLjf5nb9mvvyGFR0h6OKirZlMNUn"
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "similarity.pkl"
    if not os.path.exists(output):
        st.info("Downloading similarity.pkl ...")
        gdown.download(url, output, quiet=False)


st.title('🎬 CineMatch - Movie Recommender')

movies = pickle.load(open('movies.pkl', 'rb'))

download_similarity_file()

with open("similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movie_names


movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('🎥 Show Recommendations'):
    recommended_movie_names = recommend(selected_movie)
    st.header('Recommended Movies:')
    for movie in recommended_movie_names:
        st.write(movie)
