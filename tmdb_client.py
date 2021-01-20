import requests

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def api_call(endpoint):
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYmMwMjU5OWY5MDMwMGE1MDdiOGI2OGRkODY4YTBkMCIsInN1YiI6IjVmZmUyYzQxOTgyNGM4MDAzZWZiOGNjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BGqyWN5q7N6G0a0zpsDyCVeP9CwVsX4OS4nNoBSH2cc"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    return api_call(endpoint)

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    return api_call(endpoint)

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    return api_call(endpoint)["cast"]

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"