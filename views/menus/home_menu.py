# coding=utf-8

"""
Class for the Home Menu
This file is launched via the
"""

from views.menus.menu import Menu
from views.menus.player_menu import PlayerMenu
from views.menus.tournament_menu import TournamentMenu


class HomeMenu(Menu):
    """
    This class is a parent Class for all Menu screens
    It enables to navigate through the program.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='-Home Menu-',
                         root_page=True)
        specific_menu_choices = [self.manage_players, self.manage_tournaments]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def manage_players(self):
        """
        This method leads to the Players Database Manager menu
        """
        PlayerMenu().run()

    def manage_tournaments(self):
        """
        This method leads to the Tournaments Manager menu
        """
        TournamentMenu().run()





    # defs à reprendre et reutiliser autre part

    # Round: pour entrer les resultats d'un round
    # 'name', 'matches', 'end_time', 'start_time'

    def ask_round_name(self): # si le format est round+n, on peut incrementer au fur et à mesure
        """
        This method asks for the round's name at the beginning of the round
        """
        return input("Enter Round Name: ")

    def ask_round_matches(self): # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés
        """"
        This method asks for the list of match results for a round
        """
        pass

    def ask_round_end_time(self):  # doit etre renseigné automatiquement en fait !
        pass

    def ask_round_start_time(self):  # doit etre renseigné automatiquement en fait !
        pass


    # Match: pour entrer les resultats d'un match
    # 'player1_id', 'player2_id', 'player1_score', 'player2_score'

    def ask_match_player1_id(self):  # en fait on le recupere de generate_matchups()
        """
        This method asks for player1's ID at the begining of a match/round
        """
        return input("Select Player1: ")

    def ask_match_player2_id(self):  # en fait on le recupere de generate_matchups()
        """
        This method asks for player2's ID at the begining of a match/round
        """
        return input("Select Player2: ")

    def ask_match_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        return input("Enter Player1 Score: ")

    def ask_match_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        return input("Enter Player2 Score: ")

    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass

