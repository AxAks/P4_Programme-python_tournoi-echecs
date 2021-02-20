# coding=utf-8

import re

from datetime import datetime, date
from enum import Enum
from typing import Union

from models.serializable import Serializable


class Tournament(Serializable):
    """
    This is the class for the Python Object: Tournament
    Time_control is an intermediate class for the tournaments's time control
    that only accept the strings "Bullet", " Blitz"  and "Coup rapide".
    """
    Time_control = Enum("Time_control", "BULLET BLITZ RAPIDE")

    def __init__(self, name: str, location: str, date: Union[str, date], rounds_count: int,
                 rounds: int, players: list, time_control: Time_control, description: str):
        errors = []
        try:
            self.name = name
        except AttributeError:
            errors.append('Name')
        try:
            self.location = location
        except AttributeError:
            errors.append('Location')
        try:
            self.date = date
        except AttributeError:
            errors.append('Date')
        try:
            self.rounds_count = rounds_count
        except AttributeError:
            errors.append('Rounds Count')
        try:
            self.rounds = rounds
        except AttributeError:
            errors.append('Rounds')
        try:
            self.players = players
        except AttributeError:
            errors.append('Players')
        try:
            self.time_control = time_control
        except AttributeError:
            errors.append('Time Control')
        try:
            self.description = description
        except AttributeError:
            errors.append('Description')

        if errors:
            raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        """
        Verification of entered characters for last name using regex
        ASCII table and a few special characters
        The list of authorized characters is to be completed !
        :param value:
        :return:
        """
        #  à factoriser ? : doublon avec Player last_name et first_name
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\- ]+$")
        if re.match(authorized_characters, value):
            self.__name = value.title()
        else:
            raise AttributeError()

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, value: str):
        """
        Verification of entered characters for last name using regex
        ASCII table and a few special characters
        The list of authorized characters is to be completed !
        :param value:
        :return:
        """
        #  à factoriser ? : doublon avec Player last_name et first_name etc ... (les attributs strings)
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\-]+$")
        if re.match(authorized_characters, value):
            self.__location = value.title()
        else:
            raise AttributeError()

    @property
    def date(self) -> date:
        return self.__date

    @property
    def date_pod(self) -> str:
        return self.__date.isoformat()

    @date.setter
    def date(self, value: str):
        if isinstance(value, str):
            regex_iso8601 = "^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$"
            check_iso8601_format = re.compile(regex_iso8601)
            if re.match(check_iso8601_format, value):
                try:
                    value = datetime.strptime(value, '%Y-%m-%d').date()
                except ValueError:
                    raise AttributeError()
            else:
                raise AttributeError()

        elif not isinstance(value, date):
            raise AttributeError()

        self.__date = value

    @property
    def rounds_count(self) -> int:
        return self.__rounds_count

    @rounds_count.setter
    def rounds_count(self, value):
        self.__rounds_count = value

    @property
    def rounds(self):
        return self.__rounds

    @rounds.setter
    def rounds(self, value):
        self.__rounds = value

    @property
    def players(self) -> object:
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    @property
    def time_control(self) -> Time_control:
        return self.__time_control

    @time_control.setter
    def time_control(self, value):
        self.__time_control = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
