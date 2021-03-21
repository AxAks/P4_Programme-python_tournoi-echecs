# coding=utf-8

"""
Form file for the creation of a new tournament in the database.
"""

from views.forms.form import Form
from views.general_inputs import TournamentInputs


class NewTournamentForm(Form):  # faire heriter de Menu aussi ? (fonction de navigation : back, etc)
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """
    def __init__(self):
        pass

        #  Tournament : Pour la création des tournois
        #  'name', 'location', 'start_date', 'end_date', 'players_identifier',
        # 'time_control', 'description', 'rounds_list', 'rounds'

    def add_new_tournament(self) -> dict:  # mettre des verifs champs par champs!
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        name = TournamentInputs().ask_tournament_name()
        location = TournamentInputs().ask_tournament_location()
        start_date = TournamentInputs().ask_tournament_start_date()
        end_date = TournamentInputs().ask_tournament_end_date()  #  demander si le tournoi est sur un jour si oui attribuer la meme date que start_date
        players_identifier = TournamentInputs().ask_tournament_players_identifier()
        time_control = TournamentInputs().ask_tournament_time_control()
        description = TournamentInputs().ask_tournament_description()
        new_tournament_dict = {
            'name': name,
            'location': location,
            'start_date': start_date,
            'end_date': end_date,
            'players_identifier': players_identifier,
            'time_control': time_control,
            'description': description
        }
        print(new_tournament_dict)
        return new_tournament_dict
        """
        print(f'\nTournament Information\n', new_tournament_dict)
        tournament_factory = Factory(Tournament)
        new_tournament = tournament_factory.create(**new_tournament_dict)
        print(tournament_factory.registry)
        print(new_tournament.__dict__)
        return new_tournament
        """


