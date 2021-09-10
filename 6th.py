import requests
import sqlite3
import json
from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

url = "https://api.chucknorris.io/jokes/random"


class GetJoke(Resource):
    def get(self):
        response = requests.get(url)
        joke = response.json()["value"]
        conn = sqlite3.connect('mydata.db')
        cursor = conn.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS jokes (joke TEXT)')

        # data = joke
        data = random.choice(joke)
        cursor.execute('INSERT INTO jokes VALUES (?)', data)

        conn.commit()
        return joke


class AllJokes(Resource):
    def get(self):
        response = requests.get(url)
        joke = response.json()["value"]
        return joke


api.add_resource(GetJoke, '/random_joke')
api.add_resource(AllJokes, '/saved_joks')

if __name__ == '__main__':
    app.run(debug=True)