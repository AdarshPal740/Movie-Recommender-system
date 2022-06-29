import streamlit as st
import pandas as pd
import pickle
import requests
def fetch_poster(movie_id):
   resposnse=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=b2768e6230215e70a0ab08b37c835340'.format(movie_id))
   data=resposnse.json()
   return "http://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
         movie_id=movies.iloc[i[0]].movie_id
         recommended_movies.append(movies.iloc[i[0]].title)
         recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pickle.load(open('movie_list.pkl','rb'))
st.title("Movie Recommender System")
selected=st.selectbox('Select Movie Name',movies['title'].values)

if st.button('Recommend'):
    names,poster=recommend(selected)
    # for i in range(5):
    #  print(names[i],poster[i])
    #  st.text(names[i])
    #  st.image(poster[i])
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])  
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])   
    with col5:
        st.text(names[4])
        st.image(poster[4])       
        