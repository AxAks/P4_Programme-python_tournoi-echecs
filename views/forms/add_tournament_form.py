# coding=utf-8

"""
Form file for the creation of a new tournament in the database.
"""
from controllers import tournament_controller
from views.forms.form import Form
from views.inputs.generic_inputs import GenericInputs
from views.menus import tournament_menu
from constants import TOURNAMENT_PROPERTIES


class NewTournamentForm(Form):  # héritage en cascade  : Menu -> Form -> .
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='New Tournament Form',
                         previous_page_ctrl=tournament_controller,
                         root_page=False, exiting_message='Leaving Form', properties=TOURNAMENT_PROPERTIES)

        specific_menu_choices = [self.add_new_tournament]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def add_new_tournament(self) -> dict: #  à passer en tnat que add_new dans Form
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        print(self.program_name, '\n', self.menu_name, '\n')
        ask_properties_dict = {}
        for _property in TOURNAMENT_PROPERTIES:
            if _property not in ('rounds_list', 'rounds'):
                ask_properties_dict[_property] = GenericInputs().ask_properties(_property)
        """
        new_tournament_dict = {}
        for key in ask_properties_dict:
            new_tournament_dict[key] = ask_properties_dict[key]
        return new_tournament_dict
        print(f'\nTournament Information\n', new_tournament_dict)  # pas dans les views
        tournament_factory = Factory(Tournament)
        new_tournament = tournament_factory.create(**new_tournament_dict)
        return new_tournament
        """
