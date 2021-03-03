# coding=utf-8

import re

from datetime import date
from enum import Enum
from typing import Union

from constants import ALPHA_NUMERICAL_STRING_RULE, ALPHABETICAL_STRING_RULE

from models.player import Player
from models.serializable import Serializable


class Tournament(Serializable):
    """
    This is the class for the Python Object: Tournament
    Time_control is an intermediate class for the tournaments's time control
    that only accept the strings "Bullet", " Blitz"  and "Coup Rapide".
    """
    Time_control = Enum("Time_control", "BULLET BLITZ RAPIDE")

    def __init__(self, **params: dict):
        """
        The initialization of the class Tournament checks wheter there is a missing parameter in the entered values.
        """
        super().__init__(**params)
        tournament_attributes = ('tournament_name', 'location', 'dates', 'players',
                                 'time_control', 'description', 'rounds_list', 'rounds')
        # attention trouver comment mettre round à 4 par défaut !!
        errors = []
        missing_attributes = []
        for key, value in params.items():
            if key in tournament_attributes:
                try:
                    setattr(self, key, value)
                except AttributeError:
                    errors.append(key)
            else:
                missing_attributes.append(key)

        if missing_attributes:
            raise AttributeError(f'The following attributes do not exist'
                                 f' for the object {self.__class__.__name__}:'
                                 f' {", ".join(missing_attributes)}')
        if errors:
            raise Exception(f'Errors detected in the following fields: {", ".join(errors)}')

    @property
    def tournament_name(self) -> str:
        """
        This method returns the tournament's name as a string.
        """
        return self.__tournament_name

    @tournament_name.setter
    def tournament_name(self, value: str):
        """
        This setter checks the entered characters for the tournament's name using regex:
        alphanumerical characters and a few special characters are authorized
        The list of authorized characters can be extended.
        """
        authorized_characters = ALPHA_NUMERICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__tournament_name = value.title()
        else:
            raise AttributeError()

    @property
    def location(self) -> str:
        """
        This method returns the location as a string.
        """
        return self.__location

    @location.setter
    def location(self, value: str):
        """
        This setter checks the entered characters for the tournament's location using regex:
        alphabetical characters and a few special characters are authorized
        The list of authorized characters can be extended.
        """
        authorized_characters = ALPHABETICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__location = value.title()
        else:
            raise AttributeError()

    @property
    def dates(self) -> date:
        """
        This method returns the date as a date.
        """
        return self.__dates

    def dates_pod(self) -> str:
        """
        This method returns the date as a string.
        """
        return self.__dates.isoformat()

    @dates.setter
    def dates(self, value: Union[str, date]):
        """
        This setter checks wheter the entered value is a string or a date object
        and sets the attribute as a date
        """
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
        """
        This method returns the players as a list of dicts.
        """
        return [player_instance.serialize() for player_instance in self.__players]

    @players.setter
    def players(self, value: Union[list[dict], list[Player]]):
        """
        This setter checks wheter the entered value is list of Player Objects or a list of dicts
        and sets the attribute as a list of Player Objects
        """
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
        """
        This method returns the Time Control as a Time Control Enum.
        """
        return self.__time_control

    def time_control_pod(self) -> str:
        """
        This method returns the Time Control as a string.
        """
        return self.__time_control.name

    @time_control.setter
    def time_control(self, value: Union[str, Time_control]):
        """
        This setter checks wheter the entered value is a string or a Time Control Enum
        and sets the attribute as a Time Control Enum
        """
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
        """
        This method returns the description as an integer.
        """
        return self.__description

    @description.setter
    def description(self, value: str):
        """
        This setter checks that the entered value is a string.
        """
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
        """
        This method returns the number of round as an integer.
        """
        return self.__rounds

    @rounds.setter
    def rounds(self, value: int):
        """
        This setter checks that the entered value is a positive integer.
        """
        if type(value) == int:
            if value > 0:
                self.__rounds = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()

    def add_round(self, round_info):
        """
        This method enables to add the list of Matches of a Round to the Tournament Object
        """
        pass
