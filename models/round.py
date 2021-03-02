# coding=utf-8

import re

from typing import Union
from datetime import datetime

from constants import INDEX_PLAYER1, INDEX_PLAYER2,\
    INDEX_PLAYER1_SCORE, INDEX_PLAYER2_SCORE, ALPHA_NUMERICAL_STRING_RULE

from models.serializable import Serializable
from models.tournament import Tournament
from models.player import Player


class Round(Serializable):
    """
    This is the class for the Python Object: Round
    """

    def __init__(self, **params: dict):
        super().__init__(**params)
        round_attributes = ('round_name', 'tournament', 'matches', 'end_time',
                            'start_time')  #  start_time = datetime.new() # end_time = datetime de la fin de round
        errors = []
        missing_attributes = []
        for key, value in params.items():
            if key in round_attributes:
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
    def round_name(self) -> str:
        return self.__name

    @round_name.setter
    def round_name(self, value: str):
        """
        Verification of entered characters for last name using regex
        ASCII table and a few special characters
        The list of authorized characters is to be completed !
        :param value:
        :return:
        """
        authorized_characters = ALPHA_NUMERICAL_STRING_RULE
        if re.match(authorized_characters, value):
            self.__name = value.title()
        else:
            raise AttributeError()

    @property
    def tournament(self) -> Tournament:
        return self.__tournament

    @property
    def tournament_pod(self) -> dict:
        return Serializable.serialize(self.__tournament)

    @tournament.setter
    def tournament(self, value: Union[dict, Tournament]):
        if isinstance(value, dict):
            try:
                self.__tournament = value
            except AttributeError:
                raise AttributeError()
        elif isinstance(value, Tournament):
            try:
                serialized_tournament = value.serialize()
                self.__tournament = serialized_tournament
            except AttributeError:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def matches(self) -> list[tuple[list]]:
        return self.__matches

    @matches.setter
    def matches(self, value: Union[dict, list[tuple[list]]]):  #  à revoir !
        matches = []
        for tuple_item in value:
            match_infos = []
            for match_info in tuple_item:
                if isinstance(match_info, Player):
                    serialized_player = match_info.serialize()
                    match_infos.append(serialized_player)
                else:
                    match_infos.append(match_info)
            formatted_match_tuple = \
                (
                    [match_infos[INDEX_PLAYER1], match_infos[INDEX_PLAYER1_SCORE]],
                    [match_infos[INDEX_PLAYER2], match_infos[INDEX_PLAYER2_SCORE]]
                )
            matches.append(formatted_match_tuple)
        try:
            self.__matches = value
        except AttributeError:
            raise AttributeError()

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    def start_time_pod(self) -> str:
        return self.__start_time.strftime('%Y-%m-%dT%H:%M:%S')

    @start_time.setter
    def start_time(self, value: datetime) -> Union[str, datetime]:
        #  doit etre automatiquement enregisté lors de l'instanciation du round
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
        return self.__end_time

    def end_time_pod(self) -> str:
        return self.__end_time.strftime('%Y-%m-%dT%H:%M:%S')

    @end_time.setter
    def end_time(self,
                 value: Union[str, datetime]):
        #  doit etre automatiquement enregisté lors de la fin de saisie des infos du round
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
