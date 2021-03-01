# coding=utf-8

import re
import uuid

from datetime import date, timedelta
from typing import Union
from enum import Enum
from uuid import uuid4, UUID
from models.serializable import Serializable

from constants import MINIMUM_AGE, MINIMUM_RANKING, MAXIMUM_RANKING


class Player(Serializable):
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")


    def __init__(self, **params):
        attributes = ('player_uuid', 'last_name', 'first_name', 'birthdate', 'gender', 'ranking')
        errors = []
        for key, value in params.items():
            if key in attributes:
                try:
                    setattr(self, key, value)
                except AttributeError:
                    errors.append(key)

            if errors:
                raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    @property
    def player_uuid(self) -> str:
        return str(self.__player_uuid)

    @player_uuid.setter
    def player_uuid(self, value: Union[str, UUID]):
        if value is None:
            value = uuid4()
            self.__player_uuid = value
        if isinstance(value, UUID):
            self.__player_uuid = value
        elif isinstance(value, str):
            try:
                self.__player_uuid = UUID(value)
            except ValueError:
                raise AttributeError()
        else:
            raise AttributeError()

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
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\-]+$")
        if re.match(authorized_characters, value):
            self.__last_name = value.title()
        else:
            raise AttributeError()

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
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\-]+$")
        if re.match(authorized_characters, value):
            self.__first_name = value.title()
        else:
            raise AttributeError()

    @property
    def gender(self) -> Union[str, Gender]:
        return self.__gender

    def gender_pod(self) -> str:
        return self.__gender.name

    @gender.setter
    def gender(self, value: Union[str, Gender]):
        if isinstance(value, str):
            try:
                self.__gender = self.Gender[value]
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Gender):
            self.__gender = value
        else:
            raise AttributeError()

    @property
    def birthdate(self) -> Union[str, date]:
        return self.__birthdate

    def birthdate_pod(self) -> str:
        return self.__birthdate.isoformat()

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        if isinstance(value, str):
            try:
                value = date.fromisoformat(value)
            except ValueError:
                raise AttributeError()
        elif not isinstance(value, date):
            raise AttributeError()
        if date.today() - value < timedelta(days=MINIMUM_AGE*365):
            raise AttributeError()

        self.__birthdate = value

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, value: int):
        if type(value) == int:
            if MINIMUM_RANKING < value <= MAXIMUM_RANKING:
                self.__ranking = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()
