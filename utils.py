def format_movie(movie):
    title = movie.get("Title", "N/A")
    year = movie.get("Year", "N/A")
    genre = movie.get("Genre", "N/A")
    rating = movie.get("imdbRating", "N/A")
    plot = movie.get("Plot", "N/A")

    return (
        f"\nTitle     : {title}\n"
        f"Year        : {year}\n"
        f"Genre       : {genre}\n"
        f"IMDb Rating : {rating}\n"
        f"Plot        : {plot}\n"
    )
def extract_favorite(movie):
    return {
        "Title": movie.get("Title", "N/A"),
        "Year": movie.get("Year", "N/A"),
        "imdbRating": movie.get("imdbRating", "N/A")
    }

def format_favorite(movie: dict) -> str:
    return (
        f"\nTitle       : {movie.get('Title', 'N/A')}\n"
        f"Year        : {movie.get('Year', 'N/A')}\n"
        f"IMDb Rating : {movie.get('imdbRating', 'N/A')}\n"
    )
