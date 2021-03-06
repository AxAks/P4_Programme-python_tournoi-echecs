# coding=utf-8

import re

from typing import Union
from datetime import datetime

from constants import ALPHA_NUMERICAL_STRING_RULE

from models.model import Model
from models.match import Match


class Round(Model):
    """
    This is the class for the Python Object: Round
    """

    def __init__(self, **params: dict):
        """
        The initialization of all classes is done in the parent class Model.
        the types of data for Round are as follows :
        - name: string
        - matches: list[dict] or list[Match]
        - end_time: datetime or string  # doit etre automatiquement enregisté lors de la fin de saisie des infos du round
        - start_time: datetime or string  # start_time = datetime.now() # end_time = datetime de la fin de round
        """
        super().__init__(('name', 'matches', 'end_time', 'start_time'), **params)

    @property
    def name(self) -> str:
        """
        This getter returns the round's name as a string.
        """
        return self.__name

    @name.setter
    def name(self, value: str):
        """
        This setter checks the entered characters for the round's name using regex:
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
    def matches(self) -> list[Match]:
        """
        This getter returns the list of matches for a round as a list of Match objects.
        """
        return self.__matches

    @property
    def matches_pod(self) -> list[dict]:
        """
        This getter returns the list of matches for a round as a list of match dicts
        """
        return [match_obj.serialize() for match_obj in self.__matches]

    @matches.setter
    def matches(self, value: Union[list[dict], list[Match]]):
        """
        This setter checks whether the entered value is a list of Match Objects or a list of dicts
        and sets the attribute as a list of Match objects
        """
        matches_list = []
        if value is None or value == []:
            self.matches_list = matches_list
        else:
            for match in value:
                if isinstance(match, Match):
                    try:
                        matches_list.append(match)
                        self.__matches = matches_list
                    except AttributeError:
                        raise AttributeError()
                elif isinstance(match, dict):
                    try:
                        match = Match(**match)
                        matches_list.append(match)
                        self.__matches = matches_list
                    except AttributeError:
                        raise AttributeError()
                else:
                    raise AttributeError()

    @property
    def start_time(self) -> datetime:
        """
        This getter returns the start time of the round as a datetime.
        """
        return self.__start_time

    @property
    def start_time_pod(self) -> str:
        """
        This getter returns the start time of the round as a string.
        """
        return self.__start_time.strftime('%Y-%m-%dT%H:%M:%S')

    @start_time.setter
    def start_time(self, value: datetime) -> Union[str, datetime]:
        """
        This setter checks whether the entered value is a string or a datetime object
        and sets the attribute as a datetime
        """
        #  doit etre automatiquement enregisté lors de l'instanciation du round, voir comment et où on gère ca : use datetime.datetime.now()
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                self.__start_time = value
            except ValueError:
                raise AttributeError()
        elif isinstance(value, datetime):
            self.__start_time = value
        else:
            raise AttributeError()

    @property
    def end_time(self) -> datetime:
        """
        This getter returns the end time of the round as a datetime.
        """
        return self.__end_time

    @property
    def end_time_pod(self) -> str:
        """
        This getter returns the end time of the round as a string.
        """
        return self.__end_time.strftime('%Y-%m-%dT%H:%M:%S')

    @end_time.setter
    def end_time(self,
                 value: Union[str, datetime]):
        """
        This setter checks whether the entered value is a string or a datetime object
        and sets the attribute as a datetime
        """
        #  doit etre automatiquement enregisté lors de la fin de saisie des infos du round : use datetime.datetime.now()
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                self.__end_time = value
            except ValueError:
                raise AttributeError()
        elif isinstance(value, datetime):
            self.__end_time = value
        else:
            raise AttributeError()
