# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python, Machine Learning, Pandas, and Streamlit**. This application recommends movies based on the similarity between movie features and provides movie posters through The Movie Database (TMDB) API.

<p align="center">

  🚀 **[LIVE DEMO – TRY THE APPLICATION](https://movie-recommendation-system-by-sadaf.streamlit.app/)**

</p>

---

## 📌 Project Overview

The Movie Recommendation System helps users discover movies similar to their selected movie. It uses a content-based filtering approach to calculate similarity between movies and recommends the top 5 most similar movies.

The application provides an interactive interface where users can select a movie from a dropdown menu and instantly receive recommendations along with their movie posters.

## ✨ Features

- **Movie Selection:** Choose a movie from an extensive movie collection.
- **Movie Recommendations:** Get the top 5 similar movie recommendations.
- **Content-Based Filtering:** Uses a precomputed similarity matrix to identify similar movies.
- **Movie Posters:** Fetches movie posters dynamically using the TMDB API.
- **Interactive Interface:** Built using Streamlit for a simple and user-friendly experience.
- **Custom UI:** Includes a background image, styled buttons, and interactive 3D hover effects on movie posters.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and similarity calculations |
| Streamlit | Web application interface |
| Pickle | Saving and loading model data |
| Requests | Fetching movie information from TMDB API |
| TMDB API | Retrieving movie posters |

## ⚙️ How It Works

1. **Dataset Loading:** Loads movie information from the TMDB 5000 Movies and Credits datasets.
2. **Feature Processing:** Uses processed movie information to represent movies as feature vectors.
3. **Similarity Calculation:** Uses a similarity matrix to calculate relationships between movies.
4. **Movie Selection:** The user selects a movie through the Streamlit interface.
5. **Recommendation Generation:** Identifies the selected movie and retrieves the five most similar movies.
6. **Poster Fetching:** Uses the TMDB API to fetch and display posters of recommended movies.

## 📂 Project Structure

```text
Movie_Recommendation_System/
│
├── app.py
├── movie_pred.ipynb
│
├── movies.pkl
├── similarity.pkl
│
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
├── backgrounddd.jpg
├── requirements.txt
├── .gitattributes
└── README.md
```

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**, which contains movie-related information.

The dataset includes:
- Movie titles
- Movie IDs
- Genres
- Keywords
- Cast
- Crew
- Movie overview and other details

## 💻 Installation and Setup

Follow these steps to run the project locally.

**1. Clone the repository**

```bash
git clone https://github.com/Sadaf0011/Movie_Recommendation_System.git
```

**2. Navigate to the project directory**

```bash
cd Movie_Recommendation_System
```

**3. Install the required libraries**

```bash
pip install -r requirements.txt
```

**4. Configure your TMDB API key**

Create a `.streamlit/secrets.toml` file for local development:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

Do not upload your API key or secrets file to GitHub.

**5. Run the application**

```bash
streamlit run app.py
```

The application will open in your default browser.

## 🌐 Live Deployment

The application is deployed using **Streamlit Community Cloud**.

🚀 **[Click Here to Open the Live Movie Recommendation System](https://movie-recommendation-system-by-sadaf.streamlit.app/)**

## 📸 Application Preview

The application provides an interactive movie selection interface with recommended movie posters and a customised visual design.

## 👩‍💻 Author

**Sadaf**

- GitHub: [@Sadaf0011](https://github.com/Sadaf0011)
- Project Repository: [Movie Recommendation System](https://github.com/Sadaf0011/Movie_Recommendation_System)
- Live Application: [Movie Recommendation System](https://movie-recommendation-system-by-sadaf.streamlit.app/)

---

⭐ If you find this project interesting, consider giving this repository a star!

**Thank you for visiting!**
