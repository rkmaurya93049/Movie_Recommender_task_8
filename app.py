import pickle

import pandas as pd
import streamlit as st


def recommend(movie_title: str) -> list[str]:
    """Return the five most similar movie titles for the selected movie."""
    movie_index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[movie_index]
    ranked_movies = sorted(
        enumerate(distances),
        reverse=True,
        key=lambda item: item[1],
    )[1:6]

    return [movies.iloc[index].title for index, _ in ranked_movies]


with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

with open("movie_dict.pkl", "rb") as file:
    movie_dict = pickle.load(file)

movies = pd.DataFrame(movie_dict)

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie",
    movies["title"].values,
)

if st.button("Recommend"):
    for recommendation in recommend(selected_movie_name):
        st.write(recommendation)
