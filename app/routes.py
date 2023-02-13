from flask import Flask
from flask import jsonify
from app.db_RAndM_Spotify_service import DbRickAndMortySpotify

from app.RickAndMortyPopulator.character.character_controller import character_page

app = Flask(__name__)

app.register_blueprint(character_page)


@app.route('/')
def home():
    DbRickAndMortySpotify.create_table_characters()
    message = {
        "Home": 'http://127.0.0.1:8080/',
        "Artist": 'http://127.0.0.1:8080/artist?name=',
        "Character": 'http://127.0.0.1:8080/character',
        "Episode": 'http://127.0.0.1:8080/episode',
        "Favourites": 'http://127.0.0.1:8080/favourites',

    }
    return jsonify(message)
