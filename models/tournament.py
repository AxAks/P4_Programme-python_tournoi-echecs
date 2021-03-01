# coding=utf-8

import re

from datetime import date
from enum import Enum
from typing import Union

from models.player import Player
from models.serializable import Serializable


class Tournament(Serializable):
    """
    This is the class for the Python Object: Tournament
    Time_control is an intermediate class for the tournaments's time control
    that only accept the strings "Bullet", " Blitz"  and "Coup rapide".
    """
    Time_control = Enum("Time_control", "BULLET BLITZ RAPIDE")

    def __init__(self, **params):
        attributes = ('name', 'location', 'dates', 'players', 'time_control', 'description', 'rounds_list', 'rounds') # attention trouver comment mettre round à 4 par défaut !!
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
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\- 1-9]+$")
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
    def dates(self) -> Union[str, date]:
        return self.__dates

    def dates_pod(self) -> str:
        return self.__dates.isoformat()

    @dates.setter
    def dates(self, value: Union[str, date]):
        if isinstance(value, str):
            try:
                value = date.fromisoformat(value)
                self.__dates = value
            except ValueError:
                raise AttributeError()
        elif isinstance(value, date):
            self.__dates = value
        else:
            raise AttributeError()

    @property
    def players(self) -> list[dict]:
        return [player_instance.serialize() for player_instance in self.__players]

    @players.setter
    def players(self, value: Union[list[dict], list[Player]]):
        player_objs_list = []
        if isinstance(value[0], dict):
            for player_dict in value:
                try:
                    player_instance = Player(**player_dict)
                    player_objs_list.append(player_instance)
                    self.__players = player_objs_list
                except AttributeError:
                    raise AttributeError()
        elif isinstance(value[0], Player):
            self.__players = value
        else:
            raise AttributeError()

    @property
    def time_control(self) -> Time_control:
        return self.__time_control

    def time_control_pod(self) -> str:
        return self.__time_control.name

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
    def rounds_list(self) -> list[tuple[dict, int], tuple[dict, int]]:
        return self.__rounds_list

    @rounds_list.setter
    def rounds_list(self, value: list[tuple[dict, int], tuple[dict, int]]):
        self.__rounds_list = value

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
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict