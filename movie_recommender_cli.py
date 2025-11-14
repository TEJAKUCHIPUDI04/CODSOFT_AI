

import sys
import difflib
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
MOVIES = pd.DataFrame([
    {"movie_id": 1,  "title": "Inception",              "genres": "sci-fi action",               "tags": "dream heist mind-bending nolan"},
    {"movie_id": 2,  "title": "The Dark Knight",        "genres": "action crime thriller",       "tags": "batman joker nolan vigilante"},
    {"movie_id": 3,  "title": "Interstellar",           "genres": "sci-fi drama adventure",      "tags": "space time black-hole nolan"},
    {"movie_id": 4,  "title": "The Prestige",           "genres": "drama mystery thriller",      "tags": "magicians rivalry twist nolan"},
    {"movie_id": 5,  "title": "Titanic",                "genres": "romance drama",               "tags": "ship love tragedy historical"},
    {"movie_id": 6,  "title": "La La Land",             "genres": "romance musical drama",       "tags": "music dance hollywood love"},
    {"movie_id": 7,  "title": "Mad Max: Fury Road",     "genres": "action adventure",            "tags": "post-apocalyptic chase desert"},
    {"movie_id": 8,  "title": "The Matrix",             "genres": "sci-fi action",               "tags": "simulation hacker chosen-one"},
    {"movie_id": 9,  "title": "Parasite",               "genres": "thriller drama",              "tags": "class satire korean oscar"},
    {"movie_id": 10, "title": "The Social Network",     "genres": "drama biography",             "tags": "facebook startup coding law"},
    {"movie_id": 11, "title": "Toy Story",              "genres": "animation family adventure",  "tags": "toys friendship pixar"},
    {"movie_id": 12, "title": "Finding Nemo",           "genres": "animation family adventure",  "tags": "ocean fish pixar journey"},
    {"movie_id": 13, "title": "The Notebook",           "genres": "romance drama",               "tags": "love couple period tears"},
    {"movie_id": 14, "title": "John Wick",              "genres": "action thriller",             "tags": "assassin revenge dog"},
    {"movie_id": 15, "title": "Arrival",                "genres": "sci-fi drama",                "tags": "aliens linguistics time"}
])

def build_content_model(movies: pd.DataFrame):
    content = (
        movies["title"].str.lower() + " " +
        movies["genres"].str.lower() + " " +
        movies["tags"].str.lower()
    )
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(content)
    sim = cosine_similarity(tfidf)  
    return sim, vectorizer

ITEM_SIM, _ = build_content_model(MOVIES)

def find_movie_index_by_title(user_input: str) -> int:
    """Return the row index in MOVIES that best matches the user's input title.
    Uses exact (case-insensitive) then fuzzy matching.
    Raises ValueError if nothing plausible is found.
    """
    titles = MOVIES["title"].tolist()
    for i, t in enumerate(titles):
        if t.lower() == user_input.strip().lower():
            return i
    close = difflib.get_close_matches(user_input, titles, n=1, cutoff=0.5)
    if close:
        best = close[0]
        return MOVIES.index[MOVIES["title"] == best][0]
    raise ValueError("No similar title found. Try another movie title.")

def recommend_like(title_input: str, top_n: int = 5):
    """Given a movie title (approximate), recommend top_n similar movies."""
    idx = find_movie_index_by_title(title_input)
    sim_scores = ITEM_SIM[idx]
    sim_scores = sim_scores.copy()
    sim_scores[idx] = -np.inf
    order = np.argsort(sim_scores)[::-1][:top_n]
    results = MOVIES.iloc[order][["title", "genres"]].copy()
    results["similarity"] = sim_scores[order]
    return MOVIES.iloc[idx]["title"], results

def main():
    print("🎬 Interactive Movie Recommender (Content-Based)")
    print("Type a movie you like. Example titles include:")
    print(", ".join(MOVIES['title'].tolist()))
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_in = input("WHICH MOVIE YOU LIKE THE MOST? ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if user_in.lower() in {"exit", "quit"}:
            print("Bye!")
            break
        if not user_in:
            continue

        try:
            matched_title, recs = recommend_like(user_in, top_n=5)
            print(f"\nBecause you like: {matched_title}")
            print("You might also enjoy:")
            for i, row in recs.reset_index(drop=True).iterrows():
                print(f"  {i+1}. {row['title']}  —  {row['genres']}")
            print()
        except ValueError as e:
            print(f"⚠️  {e}\n")

if __name__ == "__main__":
    main()
