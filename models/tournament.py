# coding=utf-8

import re

from datetime import date
from enum import Enum
from typing import Union
from uuid import UUID

from constants import ALPHA_NUMERICAL_STRING_RULE, ALPHABETICAL_STRING_RULE

from models.model import Model
from models.round import Round


class Tournament(Model):
    """
    This is the class for the Python Object: Tournament
    Time_control is an intermediate class for the tournament's time control
    that only accept the strings "Bullet", " Blitz"  and "Coup Rapide".
    """
    Time_control = Enum("Time_control", "BULLET BLITZ RAPIDE")

    def __init__(self, **data):
        """
        The initialization of all classes is done in the parent class Model.
        the types of data for Tournament are as follows :
        - name: string
        - location: string
        - dates: date or string
        - players_identifier: list[str] or list[UUID]
        - time_control: string or Time_control
        - description: string
        - rounds_list: list[dict] or list[Round]
        - rounds: integer
        """
        super().__init__(('name', 'location', 'dates', 'players_identifier',
                         'time_control', 'description', 'rounds_list', 'rounds'), **data)

    @property
    def identifier(self) -> tuple[str, str, str]:
        """
        This method returns the tournament's name, location and dates  as a tuple of strings
        It enables to identify a tournament instance.
        """
        return self.name, self.location, self.dates_pod

    @property
    def name(self) -> str:
        """
        This method returns the tournament's name as a string.
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        """
        This setter checks the entered characters for the tournament's name using regex:
        alphanumerical characters and a few special characters are authorized
        The list of authorized characters can be extended.
        """
        if value is None:
            raise AttributeError()
        authorized_characters = ALPHA_NUMERICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__name = value.title()
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
        if value is None:
            raise AttributeError()
        authorized_characters = ALPHABETICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__location = value.title()
        else:
            raise AttributeError()

    @property
    def dates(self) -> date:
        """
        This method returns the dates of the tournament as a date.
        """
        return self.__dates

    @property
    def dates_pod(self) -> str:
        """
        This method returns the dates of the tournament as a string.
        """
        return self.__dates.isoformat()

    @dates.setter
    def dates(self, value: Union[str, date]):
        """
        This setter checks whether the entered value is a string or a date object
        and sets the attribute as a date
        """
        if value is None:
            raise AttributeError()
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
    def players_identifier(self) -> list[str]:
        """
        This method returns the players' identifier as a list of strings or UUID.
        The controller matches the Player instance through its identifier
        """
        return [str(player_id) for player_id in self.__players_identifier]

    @players_identifier.setter
    def players_identifier(self, value: Union[list[str], list[UUID]]):
        """
        This setter checks whether the entered value is list of Player UUIDs or a list of strings
        and sets the attribute as a list of Player UUIDs
        """
        if value is None:
            raise AttributeError()
        players_identifier_list = []
        for player_id in value:
            if isinstance(player_id, str):
                try:
                    player_id = UUID(player_id)
                    players_identifier_list.append(player_id)
                    self.__players_identifier = players_identifier_list
                except AttributeError:
                    raise AttributeError()

            elif isinstance(player_id, UUID):
                try:
                    player_id = player_id
                    players_identifier_list.append(player_id)
                    self.__players_identifier = players_identifier_list
                except AttributeError:
                    raise AttributeError()
            else:
                raise AttributeError()

    @property
    def time_control(self) -> Time_control:
        """
        This method returns the Time Control as a Time Control Enum.
        """
        return self.__time_control

    @property
    def time_control_pod(self) -> str:
        """
        This method returns the Time Control as a string.
        """
        return self.__time_control.name

    @time_control.setter
    def time_control(self, value: Union[str, Time_control]):
        """
        This setter checks whether the entered value is a string or a Time Control Enum
        and sets the attribute as a Time Control Enum
        """
        if value is None:
            raise AttributeError()
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
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            self.__description = value
        else:
            raise AttributeError()

    @property
    def rounds_list(self) -> list[Round]:
        """
        This method returns the tournament's list of rounds as a list of Round objects.
        """
        return self.__rounds_list

    @property
    def rounds_list_pod(self) -> list[dict]:
        """
        This method returns the tournament's list of rounds as a list of dicts.
        """
        return [round_item.serialize() for round_item in self.__rounds_list]

    @rounds_list.setter
    def rounds_list(self, value: Union[list[Round], list[dict]]):
        """
        This setter checks whether the entered value is a list of Round objects or a list of dicts
        and sets it as a list of Round object.
        """
        rounds_list = []
        if value is None or value == []:
            try:
                self.__rounds_list = rounds_list
            except AttributeError:
                raise AttributeError()
        else:
            for round_item in value:
                if isinstance(round_item, Round):
                    try:
                        rounds_list.append(round_item)
                    except AttributeError:
                        raise AttributeError()
                elif isinstance(round_item, dict):
                    try:
                        round_item = Round(**round_item)
                        rounds_list.append(round_item)
                    except AttributeError:
                        raise AttributeError()
                else:
                    raise AttributeError()

        self.__rounds_list = rounds_list

    @property
    def rounds(self) -> int:
        """
        This method returns the number of round as an integer.
        """
        return self.__rounds

    @rounds.setter
    def rounds(self, value: int = 4):
        """
        This setter checks that the entered value is a positive integer
        The default number of rounds is set to 4.
        """
        if value is None:
            self.__rounds = 4
        elif type(value) == int:
            if value > 0:
                self.__rounds = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()
