from controllers.list_tournaments_controller import ListTournamentsCtrl
from controllers.players_controller import PlayersCtrl


def players_list_serializer():
    registered_players_obj = PlayersCtrl.sort_by_last_name()
    serialized_player_list = [player_obj.serialize() for player_obj in registered_players_obj]
    return serialized_player_list


def tournaments_list_serializer():
    registered_tournaments_obj = ListTournamentsCtrl.sort_by_name()  #  + autres sort_by, via args ?
    serialized_tournaments_list = [tournament_obj.serialize() for tournament_obj in registered_tournaments_obj]
    return serialized_tournaments_list

