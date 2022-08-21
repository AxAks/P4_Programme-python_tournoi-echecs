from flask import Flask
from flask_restful import Api

from models.models_utils import data
from models.models_utils.supermanager import super_manager as sm

from models.player import Player as BasePlayer
from models.tournament import Tournament as BaseTournament

from api.resources import Player as ApiPlayer
from api.resources import Tournament as ApiTournament


app = Flask(__name__)
api = Api(app)

sm.create_manager(BasePlayer)
sm.create_manager(BaseTournament)
data.load()


api.add_resource(ApiPlayer, '/players/')
api.add_resource(ApiTournament, '/tournaments/')


if __name__ == '__main__':
    app.run(debug=True)
