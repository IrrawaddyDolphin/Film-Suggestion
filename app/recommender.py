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

cos_symulacja=cosine_similarity(tfidf_matrix,tfidf_matrix)

def suggested_movie(nazwa, top_n=7):
    match=movies_df[movies_df["title"].str.lower()==nazwa.lower()]
    if match.empty:
        return "Nie znaleziono"
    idx = match.index[0]
    wynik_sym = list(enumerate(cos_symulacja[idx]))
    wynik_sym = sorted(wynik_sym, key=lambda x: x[1], reverse=True)
    wynik_sym = [wynik for wynik in wynik_sym if wynik[0] != idx]
    wynik_sym = wynik_sym[:top_n]
    movie_indices = [i[0] for i in wynik_sym]
    return movies_df[["title", "genres"]].iloc[movie_indices]
#print(suggested_movie("Waiting to Exhale (1995)"))