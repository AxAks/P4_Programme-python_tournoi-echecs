# coding=utf-8

import re
import json

from datetime import date, datetime
from typing import Union
from enum import Enum
from json import JSONEncoder

from constants import MALE, FEMALE


class Player:
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE, FEMALE")

    def __init__(self, last_name: str, first_name: str, birthdate: str, gender: Gender, ranking: int):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        """
        Verification of entered characters for last name using regex
        ASCII table and a few special characters
        The list of authorized characters is to be completed !
        :param value:
        :return:
        """
        #  à factoriser ? : doublon avec first_name
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\ -]+$")
        if re.match(authorized_characters, value):
            self.__last_name = value.title()
        else:
            raise Exception("Last name contains not allowed characters")

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        """
        Verification of entered characters for first name using regex
        ASCII table and a few special characters
        The list of authorized characters is to be completed !
        :param value:
        :return:
        """
        #  à factoriser ? : doublon avec last_name
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\ -]+$")
        if re.match(authorized_characters, value):
            self.__first_name = value.title()
        else:
            raise Exception("First name contains not allowed characters")

    @property
    def gender(self) -> Gender:
        return self.__gender

    @gender.setter
    def gender(self, value: Gender):
        self.__gender = value.title()

    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        self.__birthdate = value
        """
        if type(value) != date:
            value = date(value)  # très faux !! l'idée est de forcer le format date
        
        if date.now - value > 18:
            self.__birthdate = value
        else:
            raise Exception("Player must be over 18")
        """

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, value: int):
        if type(value) == int:
            if value > 0:
                self.__ranking = value
            else:
                raise Exception("Rank must be positive")
        else:
            raise Exception("Rank must be an integer")

    def player_to_json(self):
        """
        This method convert a python objet Player into a JSon dictionary
        in order to save it to the database
        """
        JSONEncoder


"""
# à supprimer c'etait un test !

player1 = Player('richard', 'Bor', 4, '01/03/1982')

print(player1.first_name)

player1.first_name = 'Pierre'

print(player1.first_name)
"""


class PlayerEncoder(JSONEncoder):
    def __init__(self, player):
        self.player = player

    def default(self, player):
        if isinstance(player, Player):
            return player.__dict__
        else:
            return JSONEncoder.default(self, player)


# Tests Serialization
player1 = Player('Akondé', 'Axel', '02/05/1896', MALE, 1)
player2 = Player('Berd', 'Bernard', '01/03/1982', MALE, 3)
player3 = Player('CERAS', 'Cédric', '26/04/1978', MALE, 2)
player4 = Player('Deflar', 'Didier', '21/12/1991', MALE, 4)
player5 = Player('Edourd', 'Emilie', '01/05/1922', FEMALE, 10)
player6 = Player('Ferrat', 'Fanny', '12/09/1985', FEMALE, 9)
player7 = Player('GRAND', 'Gérard', '01/03/1982', MALE, 7)
player8 = Player('Harry', 'Henriette', '21/11/1972', FEMALE, 8)
player9 = Player('Isidore', 'Isabelle', '01/03/1984', FEMALE, 6)
player10 = Player('Junot', 'Juliette', '01/03/1982', FEMALE, 5)

players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]


def serialize_players(players):
    serialized_players = [PlayerEncoder(player).default(player) for player in players]
    [print(serialized_player) for serialized_player in serialized_players]


def serialize_one_player(player):
    serialized_player = PlayerEncoder(player).default(player)
    print(serialized_player)


serialize_one_player(player1)
print("---")
serialize_players(players)

"""
# Tests Deserialization

player1 = {}
player2 = {}
player3 = {}
player4 = {}
player5 = {}
player6 = {}
player7 = {}
player8 = {}
player9 = {}
player10 = {}
"""