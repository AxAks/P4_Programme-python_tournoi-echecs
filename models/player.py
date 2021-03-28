# coding=utf-8

import re

from datetime import date, timedelta
from typing import Union
from uuid import uuid4, UUID
from enum import Enum

from constants import MINIMUM_AGE, ALPHABETICAL_STRING_RULE, RANKING_RANGE, PLAYER_PROPERTIES
from models.model import Model


class Player(Model):
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")

    def __init__(self, **data):
        """
        The initialization of all classes is done in this parent class Model
        the types of data for Player are as follows :
        - identifier: None, UUID or string
        - last_name: string
        - first_name: string
        - birthdate: string or date
        - gender: string or Gender
        - ranking: int
        """
        super().__init__(PLAYER_PROPERTIES, **data)

    @property
    def identifier(self) -> UUID:
        """
        This getter returns the player's uuid as an UUID.
        """
        return self.__identifier

    @property
    def identifier_pod(self) -> str:
        """
        This getter returns the player's uuid as an string.
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
            if value == UUID(str(value), version=4):
                self.__identifier = value
            else:
                raise AttributeError()
        elif isinstance(value, str):
            if UUID(value) == UUID(value, version=4):
                self.__identifier = UUID(value)
            else:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def last_name(self) -> str:
        """
        This getter returns the player's last name as a string.
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
        This getter returns the player's first name as a string.
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
        This getter returns the birthdate as a date.
        """
        return self.__birthdate

    @property
    def birthdate_pod(self) -> str:
        """
        # This getter returns the birthdate as a string.
        """
        return self.__birthdate.isoformat()

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        """
        This setter checks that the entered value is a string or a date.
        in the case of a string, the string is formatted into a date.
        it also checks whether the Player has the minimum required age.
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                value = date.fromisoformat(value)
            except ValueError:
                raise AttributeError()
        elif not isinstance(value, date):
            raise AttributeError()

        if date.today() - value < timedelta(days=MINIMUM_AGE * 365):
            raise AttributeError()

        self.__birthdate = value

    @property
    def gender(self) -> Gender:
        """
        This getter returns the gender as an Enum.
        """
        return self.__gender

    @property
    def gender_pod(self) -> str:
        """
        # This getter returns the gender as a string.
        """
        return self.__gender.name.title()

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
        This getter returns the player's ranking.
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
            if value in RANKING_RANGE:
                self.__ranking = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()
