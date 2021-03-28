# coding=utf-8

"""
Form file for the creation of a new tournament in the database.
"""

from views.forms.form import Form
from views.inputs.generic_inputs import GenericInputs
#from views.inputs.tournament_inputs import TournamentInputs
from views.menus import tournament_menu
from controllers import menu_controller


class NewTournamentForm(Form):  # faire heriter de Menu aussi ? (fonction de navigation : back, etc) # en cascade actuellement : Menu -> Form -> .
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Tournament Form',
                         previous_page=tournament_menu.TournamentMenu(),
                         root_page=False, exiting_message='Leaving Form')

        specific_menu_choices = [self.add_new_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_new_tournament(self) -> dict: #  à passer en tnat que add_new dans Form
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        print(self.program_name, '\n', self.menu_name, '\n')
        ask_properties_dict = {
        'name': GenericInputs().ask_properties('name'),
        'location': GenericInputs().ask_properties('location'),
        'start_date': GenericInputs().ask_properties('start_date'),
        # demander si le tournoi est sur un jour si oui attribuer la meme date que start_date (controller ?) voir check_one_day_tournament (a repenser)
        'end_date': GenericInputs().ask_properties('end_date'),
        'identifiers_list': GenericInputs().ask_properties('identifiers_list'),
        'time_control': GenericInputs().ask_properties('time_control'),
        'description': GenericInputs().ask_properties('description')
        }
        new_tournament_dict = {}
        for key in ask_properties_dict:
            new_tournament_dict[key] = ask_properties_dict[key]
        return new_tournament_dict
        """
        print(f'\nTournament Information\n', new_tournament_dict)  # pas dans les views
        tournament_factory = Factory(Tournament)
        new_tournament = tournament_factory.create(**new_tournament_dict)
        return new_tournament
        """

