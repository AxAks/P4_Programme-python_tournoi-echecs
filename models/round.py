# coding=utf-8

import re

from typing import Union
from datetime import datetime

from models.serializable import Serializable
from models.tournament import Tournament
from models.player import Player
from constants import INDEX_PLAYER1, INDEX_PLAYER2, INDEX_PLAYER1_SCORE, INDEX_PLAYER2_SCORE


class Round(Serializable):
    """
    This is the class for the Python Object: Round
    """

    def __init__(self, name: str, tournament: object, matches: list[tuple],
                 end_time: datetime, start_time: datetime = datetime.now()):
        errors = []
        try:
            self.name = name
        except AttributeError:
            errors.append('Name')
        try:
            self.tournament = tournament
        except AttributeError:
            errors.append('Tournament')
        try:
            self.matches = matches
        except AttributeError:
            errors.append('Matches')
        try:
            self.start_time = start_time
        except AttributeError:
            errors.append('Start Time')
        try:
            self.end_time = end_time
        except AttributeError:
            errors.append('End Time')

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
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà1-9_\- ]+$")
        if re.match(authorized_characters, value):
            self.__name = value.title()
        else:
            raise AttributeError()

    @property
    def tournament(self) -> Tournament:
        return self.__tournament

    @property
    def tournament_pod(self) -> dict:
        return self.__tournament

    @tournament.setter
    def tournament(self, value: Union[dict, Tournament]):
        if isinstance(value, dict):
            try:
                self.__tournament = Tournament(**value)
            except AttributeError:
                raise AttributeError()
        elif isinstance(value, Tournament):
            try:
                self.__tournament = value
            except AttributeError:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def matches(self) -> list[list[tuple]]:
        return self.__matches

    @matches.setter
    def matches(self, value: list[list[tuple]]):
        matches = []

        for tuple_item in value:
            match_infos = []
            for match_info in tuple_item:
                if isinstance(match_info, Player):
                    serialized_player = Player.serialize(match_info)
                    match_infos.append(serialized_player)
                else:
                    match_infos.append(match_info)
            """
            formatted_match_tuple = \
                [
                    (match_infos[INDEX_PLAYER1], match_infos[INDEX_PLAYER1_SCORE]),
                    (match_infos[INDEX_PLAYER2], match_infos[INDEX_PLAYER2_SCORE])
                ]
            """
            matches.append(match_infos)
        try:
            self.__matches = matches
        except AttributeError:
            raise AttributeError()

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    def start_time_pod(self) -> str:
        return self.__start_time.strftime('%Y-%m-%dT%H:%M:%S')

    @start_time.setter
    def start_time(self, value: datetime) -> Union[str, datetime]:  #  doit etre automatiquement enregisté lors de l'instanciation du round
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
                 value: Union[str, datetime]):  #  doit etre automatiquement enregisté lors de la fin de saisie des infos du round
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

    def serialize(self) -> dict:
        """
        This method overrides the Serializable.serialize() method to convert the property Tournament
        into a dict instead of a Tournament objects.
        and the property Matches into a list of tuple.
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict
