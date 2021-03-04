# coding=utf-8

import re

from datetime import date, timedelta, datetime
from typing import Union
from uuid import uuid4, UUID
from enum import Enum

from constants import MINIMUM_AGE, MINIMUM_RANKING, MAXIMUM_RANKING, ALPHABETICAL_STRING_RULE

from models.model import Model


class Player(Model):
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")

    def __init__(self, **data):
        # homogeneiger et documenter
        """
        The initialization of the class Player checks wheter there is a missing parameter in the entered values.
        the type of data are as follows :
        - identifier: None, UUID or string
        - last_name: string
        - first_name: string
        - birthdate: string or date
        - gender: string or Gender
        - ranking: int
        """
        super().__init__(('identifier', 'last_name', 'first_name', 'birthdate', 'gender', 'ranking'), **data)

    @property
    def identifier(self) -> UUID:
        """
        This method returns the player's uuid as an UUID.
        """
        return self.__identifier

    @property
    def identifier_pod(self) -> str:
        """
        This method returns the player's uuid as an string.
        """
        return str(self.__identifier)

    @identifier.setter
    def identifier(self, value: Union[str, UUID]):
        """
        This setter checks the entered player's uuid:
        - it sets an uuid if there is none given.
        - it converts the value into an uuid if the entered value is a string
        """
        if value is None or value == '':
            value = uuid4()
            self.__identifier = value
        elif isinstance(value, UUID):
            self.__identifier = value
        elif isinstance(value, str):
            try:
                self.__identifier = UUID(value)
            except ValueError:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def last_name(self) -> str:
        """
        This method returns the player's last name as a string.
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        """
        This setter checks the entered characters for the player's last name using regex:
        alphanumerical characters and a few special characters are authorized
        The list of authorized characters can be extended.
        """
        if value is None:
            raise AttributeError()
        authorized_characters = ALPHABETICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__last_name = value.title()
        else:
            raise AttributeError()

    @property
    def first_name(self) -> str:
        """
        This method returns the player's first name as a string.
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        """
        This setter checks the entered characters for the player's first name using regex:
        alphanumerical characters and a few special characters are authorized
        The list of authorized characters can be extended.
        """
        if value is None:
            raise AttributeError()
        authorized_characters = ALPHABETICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__first_name = value.title()
        else:
            raise AttributeError()

    @property
    def birthdate(self) -> date:
        """
        This method returns the birthdate as a date.
        """
        return self.__birthdate

    def birthdate_pod(self) -> str:
        """
        # This method returns the birthdate as a string.
        """
        return self.__birthdate.isoformat()  # pose pb car on retourne une methode et non une string

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        """
        This setter checks that the entered value is a string or a date.
        in the case of a string, the string is formatted into a date.
        it also checks wheter the Player has the minimum required age.
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                value = date.fromisoformat(value)
            except ValueError:
                print('je suis content 2')
                # raise AttributeError()
        elif not isinstance(value, date):
            print('je suis content 3')
            # raise AttributeError()
        """
        if date.today() - value < timedelta(days=MINIMUM_AGE * 365):  # method() - date = pas possible ; je masque pour le moment !
            # raise AttributeError()
        """
        self.__birthdate = value

    @property
    def gender(self) -> str:
        """
        This method returns the gender as a string.
        """
        return self.__gender.name

    @gender.setter
    def gender(self, value: Union[str, Gender]):
        """
        This setter checks that the entered value is a string or a Gender Enum
        and sets it as a Gender.
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                self.__gender = self.Gender[value]
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Gender):
            self.__gender = value.name
        else:
            raise AttributeError()

    @property
    def ranking(self) -> int:
        """
        This method returns the player's ranking.
        """
        return self.__ranking

    @ranking.setter
    def ranking(self, value: int):
        """
        This setter checks that the entered value is a integer
        and whether the player's ranking fits in the possible ranking values (from 100 to 3000).
        """
        if value is None:
            raise AttributeError()
        if type(value) == int:
            if MINIMUM_RANKING < value <= MAXIMUM_RANKING:
                self.__ranking = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()
