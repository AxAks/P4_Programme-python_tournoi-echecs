# coding=utf-8
from flask import request
from flask_restful import Resource

from api.normalizer import player_normalizer
from controllers.players_controller import PlayersCtrl
from controllers.list_tournaments_controller import ListTournamentsCtrl
from models.models_utils import data
from models.player import Player as BasePlayer


class Player(Resource):
    def get(self):
        """
        lists all registered players as dict for the api
        """
        registered_players_obj = PlayersCtrl.sort_by_last_name()  #  + sort_by_ranking, via args ?
        serialized_player_list = [player_obj.serialize() for player_obj in registered_players_obj]
        return {'players': serialized_player_list}

    def post(self):
        """
        Adds a new player
        """
        request_data = request.values
        new_player = player_normalizer(request_data)
        if isinstance(new_player, BasePlayer):
            serialized_new_player = new_player.serialize()
            data.save()
            return {'new_player': serialized_new_player}
        else:
            return {'error': new_player}


class Tournament(Resource):
    def get(self):
        """
        lists all registered tournaments as dict for the api
        """
        registered_tournaments_obj = ListTournamentsCtrl.sort_by_name()  #  + autres sort_by, via args ?
        serialized_tournaments_list = [tournament_obj.serialize() for tournament_obj in registered_tournaments_obj]
        return {'tournaments': serialized_tournaments_list}

    def post(self):
        """
        adds a new tournament
        """
