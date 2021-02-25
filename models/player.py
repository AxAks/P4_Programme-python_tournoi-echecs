# coding=utf-8

import re

from datetime import date, datetime, timedelta
from typing import Union
from enum import Enum

from models.serializable import Serializable

from constants import MINIMUM_AGE, MINIMUM_RANKING, MAXIMUM_RANKING


class Player(Serializable):
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")
    attributes = Enum("attributes", "last_name first_name birthdate gender ranking")

#  ajouter un attribut uuid, voir uuid4 module (gestion des uuid pas de registre à tenir), sinon tenir un registre et on incremente, avec ID_MAX pour le player value)None possible, if value == None ajouter un UUID
    def __init__(self, uuid: int, last_name: str, first_name: str, birthdate: Union[str, date], #  (self, **params) avec boucle for + try/except si elle sont dans params on recupere la valeur
                 gender: Union[str, Gender], ranking: int):
        # super().__init__('last_name', 'first_name', ...) a faire dans toutes les classes
        errors = []
        try:
            self.uuid = uuid
        except AttributeError:
            errors.append('Uuid')
        try:
            self.last_name = last_name
        except AttributeError:
            errors.append('Last name')
        try:
            self.first_name = first_name
        except AttributeError:
            errors.append('First name')
        try:
            self.birthdate = birthdate
        except AttributeError:
            errors.append('Birthdate')
        try:
            self.gender = gender
        except AttributeError:
            errors.append('Gender')
        try:
            self.ranking = ranking
        except AttributeError:
            errors.append('Ranking')

        if errors:
            raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    @property
    def uuid(self) -> int:
        return self.__uuid

    @uuid.setter
    def uuid(self, value: int):
        if isinstance(value, int):
            self.__uuid = value
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
    def gender(self) -> Gender:
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
