# coding=utf-8

from datetime import date
from typing import Union
from enum import Enum
import re
import json


class Player:
    """
    This is the class for the Python Object: Player
    """
    class Gender(Enum):
        """
        Intermediate class for the Player's gender : only accept the strings "Male" and "Female"
        """
        MALE = "Male"
        FEMALE = "Female"

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
        authorized_characters = re.compile("^[A-Za-z\ -]+$")
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
        authorized_characters = re.compile("^[A-Za-z\ -]+$")
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

    @first_name.setter
    def birthdate(self, value: Union[str, date]):
        if date.now - value > 18:
            self.__birthdate = value


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


    def serialize_player(self):
        """
        This method convert a python objet Player into a dictionary
        """


"""
# à supprimer c'etait un test !

player1 = Player('richard', 'Bor', 4, '01/03/1982')

print(player1.first_name)

player1.first_name = 'Pierre'

print(player1.first_name)
"""