from datetime import date
from typing import Union
from enum import Enum


class Player:
    """
    blabla docstring
    """
    class Gender(Enum):
        """
        Intermediate class for gender : only accept the strings "Male" and "Female"
        """
        MALE = "Male"
        FEMALE = "Female"

    def __init__(self, last_name: str, first_name: str, birthdate: str, gender: Gender, rank: int):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        self.__last_name = value.title()


    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        self.__first_name = value.title()


    @property
    def gender(self) -> Gender:
        return self.__gender

    @gender.setter
    def gender(self, value: Gender):
        self.__gender = value()


    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @first_name.setter
    def birthdate(self, value: Union[str, date]):
        if date.now - value > 18:
            self.__birthdate = value()


    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, value: int):
        if type(value) == int:
            if value > 0:
                self.__rank = value
            else:
                raise Exception("Rank must be positive")
        else:
            raise Exception("Rank must be an integer")


"""
player1 = Player('richard', 'Bor', 4, '01/03/1982')

print(player1.first_name)

player1.first_name = 'Pierre'

print(player1.first_name)
"""