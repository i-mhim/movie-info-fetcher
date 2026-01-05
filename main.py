from api import fetch_movie
from utils import format_movie, extract_favorite, format_favorite
import json
import os
print("Main file started")
FAVORITES_FILE = "favorites.json"

def save_favorite(movie):
    favorites = []

    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, "r") as f:
            favorites = json.load(f)

    movie_data = extract_favorite(movie)

    if movie_data not in favorites:
        favorites.append(movie_data)

        with open(FAVORITES_FILE, "w") as f:
            json.dump(favorites, f, indent=2)

def view_favorites():
    if not os.path.exists(FAVORITES_FILE):
        print("\nNo favorites saved yet.")
        return

    with open(FAVORITES_FILE, "r") as f:
        favorites = json.load(f)

    if not favorites:
        print("\nNo favorites saved yet.")
        return

    print("\nYour Favorite Movies:")
    for idx, movie in enumerate(favorites, start=1):
        print(f"\n{idx}.")
        print(format_favorite(movie))

def main():
    while True:
        title = input("\nEnter movie title, 'view' to see favorites, or 'q' to quit: ").strip()

        if title.lower() == "q":
            print("Goodbye.")
            break

        if title.lower() == "view":
            view_favorites()
            continue

        if not title:
            print("Empty input. Try again.")
            continue
            
        movie = fetch_movie(title)

        if movie is None:
            print("Movie not found or API error.")
            continue
        
        print(format_movie(movie))

        save = input("Save to favorites? (y/n): ").strip().lower()

        if save == "y":
            save_favorite(movie)
            print("Saved.")
        
if __name__ == "__main__":
    main()