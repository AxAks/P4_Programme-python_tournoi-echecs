# coding=utf-8

import re

from typing import Union
from datetime import datetime

from constants import INDEX_PLAYER1, INDEX_PLAYER2,\
    INDEX_PLAYER1_SCORE, INDEX_PLAYER2_SCORE, ALPHA_NUMERICAL_STRING_RULE

from models.model import Model
from models.tournament import Tournament
from models.player import Player


class Round(Model):
    """
    This is the class for the Python Object: Round
    """
    def __init__(self, **params: dict):
        # homogeneiger et documenter comme Player
        """
        The initialization of the class Round checks wheter there is a missing parameter in the entered values.
        the types of data are as follows :
        - round_name: string
        - tournament: # à supprimer ! on va identifier , le round sera identifié dans la classe Tournament
        - matches: list [tuple or dict] # voir entre tuple et list
        - end_time: datetime or string  # doit etre automatiquement enregisté lors de la fin de saisie des infos du round
        - start_time: datetime or string  # start_time = datetime.now() # end_time = datetime de la fin de round
        """
        super().__init__(('round_name', 'matches', 'end_time', 'start_time'), **params)

    @property
    def round_name(self) -> str:
        """
        This method returns the round's name as a string.
        """
        return self.__name

    @round_name.setter
    def round_name(self, value: str):
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

    # Comment gère t-on la reference à Tournament dans Round ? à voir

    @property
    def matches(self) -> list[tuple[list]]:
        """
        This method returns the list of matches for a round as a list of tuple.
        """
        return self.__matches

    @matches.setter
    def matches(self, value: Union[dict, list[tuple[list]]]):  #  à revoir !!!! # tuple pas obligatoire ? seulement si possible, si dict : pas si grave !
        """
        This setter checks wheter the entered value is a list of Match Objects or a dict
        and sets the attribute as a list of matches as tuples
        """
        if value is None:
            raise AttributeError()
        matches = []
        for tuple_item in value:
            match_infos = []
            for match_info in tuple_item:
                if isinstance(match_info, Player):
                    serialized_player = match_info.serialize()
                    match_infos.append(serialized_player)
                else:
                    match_infos.append(match_info)
            """
            formatted_match_tuple = \
                (
                    [match_infos[INDEX_PLAYER1], match_infos[INDEX_PLAYER1_SCORE]],
                    [match_infos[INDEX_PLAYER2], match_infos[INDEX_PLAYER2_SCORE]]
                )
            matches.append(formatted_match_tuple)
            """
            matches.append(match_infos)
        try:
            self.__matches = value
        except AttributeError:
            raise AttributeError()

    @property
    def start_time(self) -> datetime:
        """
        This method returns the start time of the round as a datetime.
        """
        return self.__start_time

    @property
    def start_time_pod(self) -> str:
        """
        This method returns the start time of the round as a string.
        """
        return self.__start_time.strftime('%Y-%m-%dT%H:%M:%S')

    @start_time.setter
    def start_time(self, value: datetime) -> Union[str, datetime]:
        """
        This setter checks wheter the entered value is a string or a datetime object
        and sets the attribute as a datetime
        """
        #  doit etre automatiquement enregisté lors de l'instanciation du round
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
        This method returns the end time of the round as a datetime.
        """
        return self.__end_time

    @property
    def end_time_pod(self) -> str:
        """
        This method returns the end time of the round as a string.
        """
        return self.__end_time.strftime('%Y-%m-%dT%H:%M:%S')

    @end_time.setter
    def end_time(self,
                 value: Union[str, datetime]):
        """
        This setter checks wheter the entered value is a string or a datetime object
        and sets the attribute as a datetime
        """
        #  doit etre automatiquement enregisté lors de la fin de saisie des infos du round
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

    def add_match(self, match):
        """
        This method enables to add the information of a Match to the list of matches of the Round Object
        """
        pass
