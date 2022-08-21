# coding=utf-8

from flask_restful import Resource

from controllers.players_controller import PlayersCtrl
from controllers.list_tournaments_controller import ListTournamentsCtrl


class Player(Resource):
    def get(self):
        """
        lists all registered players as dict for the api
        """
        registered_players_obj = PlayersCtrl.sort_by_last_name()  #  + sort_by_ranking, via args ?
        serialized_player_list = [player_obj.serialize() for player_obj in registered_players_obj]
        return {'players': serialized_player_list}

    def post(self, **kwargs):
        new_player = PlayersCtrl.add_player()
        return {'new_player': new_player}


class Tournament(Resource):
    def get(self):
        """
        lists all registered tournaments as dict for the api
        """
        registered_tournaments_obj = ListTournamentsCtrl.sort_by_name()  #  + autres sort_by, via args ?
        serialized_tournaments_list = [tournament_obj.serialize() for tournament_obj in registered_tournaments_obj]
        return {'tournaments': serialized_tournaments_list}

    def post(self):
        pass
