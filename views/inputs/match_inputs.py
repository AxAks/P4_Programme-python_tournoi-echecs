# coding=utf-8


# Match: pour entrer les resultats d'un match
# 'player1_id', 'player2_id', 'player1_score', 'player2_score'

from views.inputs.generic_inputs import GenericInputs


class MatchInputs(GenericInputs):
    """
    Class listing all possible inputs related to Match
    """
    def __init__(self):
        super().init()

    # -> on pourrait passer tout ca dans PlayerInputs !
    # -> et generate_matchups dans Tournament_controller

    # en fait on le recupere de generate_matchups() + c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    # et également ask_identifier ou search_by_id dans player_inputs
    def ask_identifier(self):  # _player1
        """
        This method asks for player1's ID at the begining of a match/round
        """
        return input("Select Player1: ")

    #  en fait on le recupere de generate_matchups() + c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    #  et également ask_identifier ou search_by_id dans player_inputs
    def ask_identifier(self):  # _player2  + # en fait on le recupere de generate_matchups()
        """
        This method asks for player2's ID at the begining of a match/round
        """
        return input("Select Player2: ")

    # c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    def ask_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        return input("Enter Player1 Score: ")

    # c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
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

