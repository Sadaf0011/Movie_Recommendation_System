import streamlit as st
import pickle
import requests

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie recommendation system')
movies = pickle.load(open('movies.pkl','rb'))
movie_list = movies['title'].values.tolist() 

selected_movie = st.selectbox(
    'Choose your movie',
    movie_list 
)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(selected_movie): 
    ind = movies[movies['title'] == selected_movie].index[0] 
    distance = similarity[ind]  
    movie_list_ind = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recom_list = []
    recommended_movie_posters = []
    for i in movie_list_ind:
      
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recom_list.append(movies.iloc[i[0]].title) 
    return recom_list,recommended_movie_posters

if st.button('Show Recommendation'):
    recom_list,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recom_list[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recom_list[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recom_list[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recom_list[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recom_list[4])
        st.image(recommended_movie_posters[4])
        

import base64

# Load background image
with open("backgrounddd.jpg", "rb") as f:
    data = base64.b64encode(f.read()).decode()

st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(
        rgba(0, 0, 0, 0.65),
        rgba(0, 0, 0, 0.65)
    ), url("data:image/jpeg;base64,{data}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)
st.markdown("""



<style>

/* 3D effect on movie posters */
.stImage img {
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    border-radius: 12px;
}

.stImage img:hover {
    transform: perspective(1000px) rotateY(8deg) scale(1.08);
    box-shadow: 0px 15px 30px rgba(255, 0, 0, 0.4);
}

/* Button styling */
.stButton button {
    background-color: #e50914;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 20px rgba(229, 9, 20, 0.7);
}

</style>
""", unsafe_allow_html=True)
