# coding=utf-8

import re

from typing import Union
from datetime import datetime

from models.serializable import Serializable
from models.tournaments import Tournament


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
    def tournament_pod(self) -> str:
        return self.__tournament

    @tournament.setter
    def tournament(self, value: object):
        self.__tournament = value

    @property
    def matches(self) -> list:
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

    def serialize(self):
        # Serializable.serialize() mais qui prend en compte la serialisation de Tournament en tant qu'attribut ? (surcharge/substitution)
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if cleaned_attribute_name == "tournament":
                tournament_infos_dict = Serializable.serialize(self.__dict__[attribute])
                attributes_dict[cleaned_attribute_name] = tournament_infos_dict
                continue
            try:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            except AttributeError:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict