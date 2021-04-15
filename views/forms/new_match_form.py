# coding=utf-8

from constants import MATCH_PROPERTIES
from views.forms.form import Form


class NewPlayerForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self):
        super().__init__(properties=MATCH_PROPERTIES, cls=self)

    def add_new_match(self) -> dict:  # à passer en tant que add_new (générique) dans Form, si possible, si générique
        new_match_dict = {}
        for _property in self.properties:
            # if _property != '':  # à voir!
            new_match_dict[_property] = self.ask_property(_property)
        return new_match_dict

    #  c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2), pb pour la construction de la methode ...
    def ask_identifier(self):  # pour le player1, puis pour le player 2
        """
        This method asks for player1's ID at the beginning of a match/round
        """
        return input("Select Player1: ")

    def ask_score(self):  # pour le player1, puis pour le player 2
        """
        This method asks for player1's score at the end of a match/round
        """
        return input("Enter Player1 Score: ")
