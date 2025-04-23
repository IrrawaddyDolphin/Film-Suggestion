from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
movies_path = "C:\\Users\\dawid\\OneDrive\\Pulpit\\pokemon\\CV\\data\\ml-latest-small\\movies.csv"
ratings_path = "C:\\Users\\dawid\\OneDrive\\Pulpit\\pokemon\\CV\\data\\ml-latest-small\\ratings.csv"

movies_df = pd.read_csv(movies_path)
ratings_df = pd.read_csv(ratings_path)

movies_df["genres"] = movies_df["genres"].fillna("")

tfidf = TfidfVectorizer(token_pattern=f"[^|+]")
tfidf_matrix=tfidf.fit_transform(movies_df["genres"])

sim_cosine=cosine_similarity(tfidf_matrix,tfidf_matrix)

def suggested_movie(nazwa, top_n=5):
    match=movies_df[movies_df["title"].str.lower()==nazwa.lower()]
    if match.empty:
        return "Nie znaleziono"
    idx = match.index[0]
    sim_scores = list(enumerate(sim_cosine[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = [score for score in sim_scores if score[0] != idx]
    sim_scores = sim_scores[:top_n]
    movie_indices = [i[0] for i in sim_scores]
    return movies_df[["title", "genres"]].iloc[movie_indices]
print(suggested_movie("Ace Ventura: When Nature Calls (1995)"))