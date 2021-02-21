# coding=utf-8

import re

from datetime import date, datetime, timedelta
from typing import Union
from enum import Enum

from models.serializable import Serializable


class Player(Serializable):
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")
    attributes = Enum("attributes", "last_name first_name birthdate gender ranking")

    def __init__(self, last_name: str, first_name: str, birthdate: Union[str, date],
                 gender: Union[str, Gender], ranking: int):
        errors = []
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
            regex_iso8601 = "^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$"
            check_iso8601_format = re.compile(regex_iso8601)
            if re.match(check_iso8601_format, value):
                try:
                    value = datetime.strptime(value, '%Y-%m-%d').date()  # transforme la string en format date
                except ValueError:
                    raise AttributeError()
            else:
                raise AttributeError()
        elif not isinstance(value, date):
            raise AttributeError()
        if date.today() - value < timedelta(days=12*365):
            raise AttributeError()

        self.__birthdate = value

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, value: int):
        if type(value) == int:
            if 0 < value < 3000:
                self.__ranking = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()
