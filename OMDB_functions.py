"""Functionss involving the OMDB API."""

import os
import requests

API_KEY = os.environ['API_KEY']


def get_movies(movie):
    """Requests and returns movie search results from OMDB."""

    url = f'http://www.omdbapi.com/?s={movie}&plot=full&apikey={API_KEY}'

    req = requests.get(url)

    movie_data = req.json()

    return movie_data


def get_movie_info(movie):
    """Requests and returns movie information from OMDB."""

    url = f'http://www.omdbapi.com/?i={movie}&plot=full&apikey={API_KEY}'

    req = requests.get(url)

    movie_data = req.json()

    return movie_data