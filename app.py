import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=f786b795917885caf910a26b649fc784&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
       movie_id = movies.iloc[i[0]].movie_id
       #  fetch poster from api

       recommended_movies.append(movies.iloc[i[0]].title)
       recommended_movies_poster.append(fetch_poster(movie_id))
       # print(recommended_movies)
    return recommended_movies,recommended_movies_poster
movies_dict = pickle.load(open('movie_dict20.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity =  pickle.load(open('similarity20.pkl','rb'))
st.title('Movie-Recommender System')

selected_movie_name = st.selectbox(
    'Select movie',
    movies['title'].values)
dict = {}
if st.button('Recommend'):
   names,posters = recommend(selected_movie_name)
   # print(names)
   # if len(set(names)) != len(names) or len(set(posters)) != len(posters):
   #     st.error("Duplicate entries found in the names or posters list.")
   # else:
   #     # Display names and posters
   #     for name, poster in zip(names, posters):
   #         st.image(poster, caption=name, width=200, use_column_width=False)

   col1 , col2 , col3 , col4 , col5  = st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])
   col6, col7, col8, col9, col10  = st.columns(5)
   with col6:
       st.text(names[5])
       st.image(posters[5])
   with col7:
       st.text(names[6])
       st.image(posters[6])
   with col8:
       st.text(names[7])
       st.image(posters[7])
   with col9:
       st.text(names[8])
       st.image(posters[8])
   with col10:
       st.text(names[9])
       st.image(posters[9])
