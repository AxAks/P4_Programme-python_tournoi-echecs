# coding=utf-8

from datetime import date

from models.models_utils import player_manager
from views.inputs.generic_inputs import ask_alphabetical_string, ask_alphanumerical_string, ask_iso_date


class GetProperties:
    """
    Class used in the forms for the input an registering of a new instance.
    """

    def __init__(self):
        pass




    # -> on pourrait passer tout ca dans PlayerInputs !
    # -> et generate_matchups dans Tournament_controller

    # en fait on le recupere de generate_matchups() + c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    # et également ask_identifier ou search_by_id dans player_inputs
    @property
    def ask_identifier(self):  # _player1
        """
        This method asks for player1's ID at the beginning of a match/round
        """
        return input("Select Player1: ")

    #  en fait on le recupere de generate_matchups() + c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    #  et également ask_identifier ou search_by_id dans player_inputs
    @property
    def ask_identifier(self):  # _player2  + # en fait on le recupere de generate_matchups()
        """
        This method asks for player2's ID at the beginning of a match/round
        """
        return input("Select Player2: ")

    # c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    @property
    def ask_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        return input("Enter Player1 Score: ")

    # c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    @property
    def ask_match_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        return input("Enter Player2 Score: ")

    #  pas ici, dans un controller !!
    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass

    """
    @property
    def ask_name(self):  # Comme la methode de Tournament !!!!  ancien comm pour round : #  si le format est round+n, on peut incrementer au fur et à mesure
    """
        #This method asks for the round's name at the beginning of the round
    """
        return input("Enter Name: ")
    """
    @property
    def ask_matches(self):  # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés //controller
        """"
        This method asks for the list of match results for a round
        """
        pass

    @property
    def ask_end_time(self):  # doit etre renseigné automatiquement en fait !
        pass

    @property
    def ask_start_time(self):  # doit etre renseigné automatiquement en fait !
        pass

