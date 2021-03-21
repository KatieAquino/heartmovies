"""Script to seed database."""

import os
import json
from random import choice

from crud import *
import server

os.system('dropdb testdb')
os.system('createdb testdb')

connect_to_db(server.app)
db.create_all()


# seeds database with users
mickey_mouse = create_user( username = 'mickeymouse',
                            email = 'mmouse@test.com',
                            password = '123password')

minnie_mouse = create_user( username = 'minniemouse',
                            email = 'dotsandbows@test.com',
                            password = '456password'
                        )

donald_duck = create_user(  username = 'donaldduck',
                            email = 'dduck@test.com',
                            password = '789password'
                        )

daisy_duck = create_user(   username = 'daisyduck',
                            email = 'daisybow@test.com',
                            password = 'donaldstopnow'
                        
                        )

capt_janeway = create_user( username = 'capt_janeway',
                            email = 'janeway@test.com',
                            password = 'coffee'
                            )

users_in_db = [mickey_mouse, minnie_mouse, donald_duck, daisy_duck, capt_janeway]

print('*' * 50)
print('Users successfully added!')
print('*' * 50)


# seeds database with a several movies
with open('data/movies.json') as o:
    movie_data = json.loads(o.read())

movies_in_db = []

for movie in movie_data:
    title = (movie['title'])
    poster = (movie['poster'])
    plot = (movie['plot'])

    movie = create_movie(title, poster, plot)

    movies_in_db.append(movie)

print('*' * 50)
print('Movies successfully added!')
print('*' * 50)


# seeds database with a few favorite movies for different users
for user in users_in_db:
    for i in range(4):
        fav_movie = choice(movies_in_db)
        create_favorite_movie(user.id, fav_movie.id)

print('*' * 50)
print('Favorites successfully added!')
print('*' * 50)
