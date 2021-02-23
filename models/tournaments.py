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

    def __init__(self, name: str, location: str, date: Union[str, date], players: list,
                 time_control: Union[str, Time_control], description: str, rounds_list: list, rounds: int = 4):
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
        try:
            self.rounds_list = rounds_list
        except AttributeError:
            errors.append('Rounds Count')
        try:
            self.rounds = rounds
        except AttributeError:
            errors.append('Rounds')

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
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\- ]+$")
        if re.match(authorized_characters, value):
            self.__location = value.title()
        else:
            raise AttributeError()

    @property
    def date(self) -> Union[str, date]:
        return self.__date

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
    def players(self) -> list:
        return self.__players

    @players.setter
    def players(self, value: list):
        if isinstance(value, list):
            self.__players = value
        else:
            raise AttributeError()

    @property
    def time_control(self) -> Time_control:
        return self.__time_control

    def time_control_pod(self) -> str:
        return self.__time_control

    @time_control.setter
    def time_control(self, value: Union[str, Time_control]):
        if isinstance(value, str):
            try:
                self.__time_control = self.Time_control[value]
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Time_control):
            self.__time_control = value
        else:
            raise AttributeError()

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        if isinstance(value, str):
            self.__description = value
        else:
            raise AttributeError()

    @property
    def rounds_list(self) -> list:
        return self.__rounds_list

    @rounds_list.setter
    def rounds_list(self, value: list):
        if type(value) == int:
            if value >= 0:
                self.__rounds_list = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def rounds(self) -> int:
        return self.__rounds

    @rounds.setter
    def rounds(self, value: int):
        if type(value) == int:
            if value > 0:
                self.__rounds = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()

    def serialize(self) -> dict:
        """
        This method overrides the Serializable.serialize() method to convert the property Players
        into a list of dicts instead of a list of Player objects.
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if cleaned_attribute_name == "players":
                try:
                    player_dicts_list = [Serializable.serialize(player_obj) for player_obj in self.players]
                    players = player_dicts_list
                    attributes_dict[cleaned_attribute_name] = players
                    continue
                except AttributeError:
                    raise Exception(f'Error in the serialization of the attribute: {cleaned_attribute_name}')
            try:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            except AttributeError:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict
