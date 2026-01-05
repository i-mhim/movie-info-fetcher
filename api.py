import requests
import os

API_KEY = os.environ.get("OMDB_KEY")
BASE_URL = "http://www.omdbapi.com/"

if not API_KEY:
    raise RuntimeError("OMDB_KEY environment variable not set. Set it before running the program.")



def fetch_movie(title):
    params = {
        "t": title,
        "apikey": API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "False":
            return None
        return data
    except requests.exceptions.RequestException:
        return None