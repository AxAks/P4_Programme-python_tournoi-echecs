# coding=utf-8
from flask import request
from flask_restful import Resource

from api.normalizer import player_normalizer, tournament_normalizer
from api.serializer import players_list_serializer, tournaments_list_serializer
from controllers.list_tournaments_controller import ListTournamentsCtrl
from models.models_utils import data
from models.player import Player as BasePlayer
from models.tournament import Tournament as BaseTournament


class Player(Resource):
    def get(self):
        """
        lists all registered players as dict for the api
        """
        request_data = request.values
        serialized_players_list_by_last_name = players_list_serializer()
        if request_data and 'sort_by' in request_data:
            if request_data['sort_by'] == 'ranking':
                serialized_players_list_by_ranking = sorted(serialized_players_list_by_last_name,
                                                            key=lambda x: x['ranking'], reverse=True)
                return {'players': serialized_players_list_by_ranking}
            else:
                return {'sort_by_error': 'wrong input for sort by argument'}
        else:
            return {'players': serialized_players_list_by_last_name}

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


    def put(self):
        """
        Updates a given player (ex: ranking)
        """
        pass

    """
    def search_one_player # = get (//retrieve)  by ID
    """


class Tournament(Resource):
    def get(self):
        """
        lists all registered tournaments as dict for the api
        """
        request_data = request.values
        serialized_tournaments_list_by_name = tournaments_list_serializer()

        if request_data and 'sort_by' in request_data:
            if request_data['sort_by'] == 'start_date':
                serialized_tournaments_list_by_start_date = sorted(serialized_tournaments_list_by_name,
                                                                   key=lambda x: x['start_date'], reverse=True)
                return {'players': serialized_tournaments_list_by_start_date}
            elif request_data['sort_by'] == 'location':
                serialized_tournaments_list_by_location = sorted(serialized_tournaments_list_by_name,
                                                                 key=lambda x: x['location'])
                return {'players': serialized_tournaments_list_by_location}
            else:
                return {'sort_by_error': 'wrong input for sort by argument'}
        else:
            return {'tournaments': serialized_tournaments_list_by_name}

    def post(self):
        """
        adds a new tournament
        """
        request_data = request.values
        new_tournament = tournament_normalizer(request_data)
        if isinstance(new_tournament, BaseTournament):
            serialized_new_tournament = new_tournament.serialize()
            data.save()
            return {'new_tournament': serialized_new_tournament}
        else:
            return {'error': new_tournament}
