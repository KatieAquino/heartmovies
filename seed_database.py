"""Script to seed database."""

import os
import json
from random import choice, randint

from model import connect_to_db
from crud import *
import server

os.system('dropdb testdb')
os.system('createdb testdb')

connect_to_db(server.app)
db.create_all()

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

db_users = [mickey_mouse, minnie_mouse, donald_duck, daisy_duck,]

for user in db_users:
    db.session.add(user)