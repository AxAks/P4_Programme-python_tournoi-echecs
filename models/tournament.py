# coding=utf-8

import re

from datetime import date
from enum import Enum
from typing import Union
from uuid import UUID

from constants import ALPHA_NUMERICAL_STRING_RULE, ALPHABETICAL_STRING_RULE, TOURNAMENT_PROPERTIES

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
        - rounds: integer
        - dates: date or string
        - identifiers_list: list[str] or list[UUID]
        - time_control: string or Time_control
        - description: string
        - rounds_list: list[dict] or list[Round]
        - total_results: dict
        - not_played_yet: dict[list]
        """
        super().__init__(TOURNAMENT_PROPERTIES, **data)

    def __repr__(self):
        return f'{self.name}, {self.location}, {self.start_date}, {self.end_date}\n' \
               f'{self.rounds} Rounds\n' \
               f'{self.description}'

    @property
    def identifier(self) -> str:
        """
        This getter returns the tournament's name, location and dates  as a tuple of strings
        It enables to identify a tournament instance.
        """
        return str(f"{self.name} , {self.location} , {self.start_date_pod} , {self.end_date_pod}")

    @property
    def name(self) -> str:
        """
        This getter returns the tournament's name as a string.
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
        This getter returns the location as a string.
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
    def start_date(self) -> date:
        """
        This getter returns the dates of the tournament as a date.
        """
        return self.__start_date

    @property
    def start_date_pod(self) -> str:
        """
        This getter returns the dates of the tournament as a string.
        """
        return self.__start_date.isoformat()

    @start_date.setter
    def start_date(self, value: Union[str, date]):
        """
        This setter checks whether the entered value is a string or a date object
        and sets the attribute as a date
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                value = date.fromisoformat(value)
                self.__start_date = value
            except ValueError:
                raise AttributeError()
        elif isinstance(value, date):
            self.__start_date = value
        else:
            raise AttributeError()

        if hasattr(self, 'end_date'):
            if self.__start_date > self.__end_date:
                raise AttributeError()
            else:
                self.__start_date = value
        else:
            self.__start_date = value

    @property
    def end_date(self) -> date:
        """
        This getter returns the dates of the tournament as a date.
        """
        return self.__end_date

    @property
    def end_date_pod(self) -> str:
        """
        This getter returns the dates of the tournament as a string.
        """
        return self.__end_date.isoformat()

    @end_date.setter
    def end_date(self, value: Union[str, date]):
        """
        This setter checks whether the entered value is a string or a date object
        and sets the attribute as a date
        It also checks that the period of time is non-negative
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                value = date.fromisoformat(value)
                self.__end_date = value
            except ValueError:
                raise AttributeError()
        elif isinstance(value, date):
            self.__end_date = value
        else:
            raise AttributeError()

        if hasattr(self, 'start_date'):
            if self.__start_date > self.__end_date:
                raise AttributeError()
            else:
                self.__end_date = value
        else:
            self.__end_date = value

    @property
    def identifiers_list(self) -> list[str]:
        """
        This getter returns the players' identifier as a list of strings or UUID.
        The controller matches the Player instance through its identifier
        """
        return [str(player_id) for player_id in self.__identifiers_list]

    @identifiers_list.setter
    def identifiers_list(self, value: Union[list[str], list[UUID]]):
        """
        This setter checks whether the entered value is list of Player UUIDs or a list of strings
        and sets the attribute as a list of Player UUIDs
        """
        if value is None or value == []:
            raise AttributeError()
        players_identifiers_list = []
        for player_id in value:
            if player_id is None or player_id == '':
                raise AttributeError()
            if isinstance(player_id, str):
                try:
                    player_id = UUID(player_id)
                    players_identifiers_list.append(player_id)
                except AttributeError:
                    raise AttributeError()
            elif isinstance(player_id, UUID):
                try:
                    players_identifiers_list.append(player_id)
                except AttributeError:
                    raise AttributeError()
            else:
                raise AttributeError()

        if len(players_identifiers_list) % 2 != 0:
            raise AttributeError()
        else:
            self.__identifiers_list = players_identifiers_list

    @property
    def time_control(self) -> Time_control:
        """
        This getter returns the Time Control as a Time Control Enum.
        """
        return self.__time_control

    @property
    def time_control_pod(self) -> str:
        """
        This getter returns the Time Control as a string.
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
        This getter returns the description as an integer.
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
        This getter returns the tournament's list of rounds as a list of Round objects.
        """
        return self.__rounds_list

    @property
    def rounds_list_pod(self) -> list[dict]:
        """
        This getter returns the tournament's list of rounds as a list of dicts.
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
        This getter returns the total number of round as an integer.
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

    @property
    def total_results(self) -> dict:
        return self.__total_results

    @total_results.setter
    def total_results(self, value: dict):
        if value is None or value == {}:
            self.__total_results = {}
        elif isinstance(value, dict):
            self.__total_results = value
        else:
            raise AttributeError()

    @property
    def not_played_yet(self) -> dict[list]:
        return self.__not_played_yet

    @not_played_yet.setter
    def not_played_yet(self, value: dict[list]):
        if value is None:
            try:
                not_played_yet = {}
                for identifier in self.identifiers_list:
                    opponents_list = self.identifiers_list.copy()
                    opponents_list.remove(identifier)
                    not_played_yet[identifier] = opponents_list
                self.__not_played_yet = not_played_yet
            except AttributeError:
                raise AttributeError()
        elif isinstance(value, dict):
            try:
                self.__not_played_yet = value
            except AttributeError:
                raise AttributeError()
        else:
            raise AttributeError()
        if value == {}:
            try:
                self.__not_played_yet = {}
            except AttributeError:
                raise AttributeError()

    @property
    def done(self):
        """
        This getter return whether the Tournament is done or not
        """
        return self.__done

    @done.setter
    def done(self, value: bool) -> bool:
        """
        this setter checks that the value is a boolean
        """
        if value is None:
            self.__done = False
        elif isinstance(value, bool):
            self.__done = value
        else:
            raise AttributeError()
