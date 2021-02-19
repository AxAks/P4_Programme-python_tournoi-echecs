# coding=utf-8

import re

from datetime import date
from enum import Enum

from models.serializable import Serializable


class Tournament(Serializable):
    """
    This is the class for the Python Object: Tournament
    """
    #     Time_control = Enum("Time_control", "BULLET BLITZ RAPIDE")  # vérifier comment ca marche !
    class Time_control(Enum):
        """
        Intermediate class for the tournaments's time control :
        only accept the strings "Bullet", " Blitz"  and "Coup rapide".
        """
        BULLET = "Bullet"
        BLITZ = "Blitz"
        RAPIDE = "Coup rapide"

    def __init__(self, name: str, location: str, date: date, rounds_count: int,
                 rounds: list, players: list, time_control: Time_control, description: str):
        errors = []
        try:
            self.name = name
        except AttributeError:
            errors.append('Name')
        try:
            self.location = location
        except AttributeError:
            errors.append('Location')
        try:
            self.date = date
        except AttributeError:
            errors.append('Date')
        try:
            self.rounds_count = rounds_count
        except AttributeError:
            errors.append('Rounds Count')
        try:
            self.rounds = rounds
        except AttributeError:
            errors.append('Rounds')
        try:
            self.players = players
        except AttributeError:
            errors.append('Players')
        try:
            self.time_control = time_control
        except AttributeError:
            errors.append('Time Control')
        try:
            self.description = description
        except AttributeError:
            errors.append('Description')

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
        #  à factoriser ? : doublon avec first_name
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\ -]+$")
        if re.match(authorized_characters, value):
            self.__name = value.title()
        else:
            raise AttributeError()
