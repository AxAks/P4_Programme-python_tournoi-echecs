# coding=utf-8

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from models.models_utils import data
from models.models_utils.supermanager import super_manager as sm

from models.player import Player as BasePlayer
from models.tournament import Tournament as BaseTournament

from api.resources import Player as ApiPlayer
from api.resources import Tournament as ApiTournament
from api.resources import Data as ApiData


app = Flask(__name__)
CORS(app)
api = Api(app)

sm.create_manager(BasePlayer)
sm.create_manager(BaseTournament)
data.load()

api.add_resource(ApiData, '/api/v1/data/')
api.add_resource(ApiPlayer, '/api/v1/players/')
api.add_resource(ApiTournament, '/api/v1/tournaments/')


if __name__ == '__main__':
    app.run()
