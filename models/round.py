# coding=utf-8

import re

from typing import Union
from datetime import datetime

from models.serializable import Serializable
from models.tournament import Tournament
from models.match import Match
from models.player import Player
from constants import INDEX_PLAYER1, INDEX_PLAYER2, INDEX_PLAYER1_SCORE, INDEX_PLAYER2_SCORE


class Round(Serializable):
    """
    This is the class for the Python Object: Round
    """

    def __init__(self, name: str, tournament: object, matches: list,
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
    def tournament(self) -> object:
        return self.__tournament

    @property
    def tournament_pod(self) -> dict:
        return self.__tournament

    @tournament.setter
    def tournament(self, value: Union[dict, object]):
        self.__tournament = value

    @property
    def matches(self) -> list:
        return self.__matches

    @property
    def matches_pod(self) -> list:
        return self.__matches

    @matches.setter
    def matches(self, value: list):
        self.__matches = value

    @property
    def start_time(self) -> datetime:
        return self.__start_time

    def start_time_pod(self) -> str:
        return self.__start_time.isoformat()

    @start_time.setter
    def start_time(self, value: datetime):  #  doit etre automatiquement enregisté lors de l'instanciation du round
        self.__start_time = value

    @property
    def end_time(self) -> datetime:
        return self.__end_time

    def end_time_pod(self) -> str:
        return self.__end_time.isoformat()

    @end_time.setter
    def end_time(self,
                 value: datetime):  #  doit etre automatiquement enregisté lors de la fin de saisie des infos du round
        self.__end_time = value

    def serialize(self) -> dict:
        """
        This method overrides the Serializable.serialize() method to convert the property Tournament
        into a dict instead of a Tournament objects.
        and the property matches into a list of tuple.
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if cleaned_attribute_name == "tournament":
                try:
                    tournament_infos_dict = Tournament.serialize(self.__dict__[attribute])
                    attributes_dict[cleaned_attribute_name] = tournament_infos_dict
                    continue
                except AttributeError:
                    raise Exception(f'Error in the serialization of the attribute: {cleaned_attribute_name}')
            elif cleaned_attribute_name == "matches":
                matches = []
                for tuple_item in self.matches:
                    match_infos = []
                    for match_info in tuple_item:
                        if isinstance(match_info, Player):
                            serialized_player = Player.serialize(match_info)
                            match_infos.append(serialized_player)
                        else:
                            match_infos.append(match_info)
                    formated_match_tuple = \
                        [
                            (match_infos[INDEX_PLAYER1], match_infos[INDEX_PLAYER1_SCORE]),
                            (match_infos[INDEX_PLAYER2], match_infos[INDEX_PLAYER2_SCORE])
                        ]
                    matches.append(formated_match_tuple)
                try:
                    attributes_dict[cleaned_attribute_name] = matches   # jusqu'ici ca va, je recupere ce que je veux  !! /Prise de tete ici mais ca se fait surement dans setters ! cf date aussi
                except AttributeError:
                    raise Exception(f'Error in the serialization of the attribute: {cleaned_attribute_name}')
            if cleaned_attribute_name != "matches":
                if hasattr(self, cleaned_attribute_name + '_pod'):
                    attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
                else:
                    attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
            else:
                pass
        print(f'censé etre un attributes dict du round serialized : {attributes_dict}')
        return attributes_dict