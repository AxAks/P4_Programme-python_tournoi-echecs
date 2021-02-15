# coding=utf-8

import re
import json

from datetime import date, datetime
from typing import Union
from enum import Enum
from json import JSONEncoder, JSONDecoder

from constants import MALE, FEMALE


class Player:
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE, FEMALE")

    def __init__(self, last_name: str, first_name: str, birthdate: str, gender: Gender, ranking: int):
        self.last_name = last_name
        self.first_name = first_name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
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
            self.__last_name = value.title()
        else:
            raise Exception("Last name contains not allowed characters")

    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        """
        Verification of entered characters for first name using regex
        ASCII table and a few special characters
        The list of authorized characters is to be completed !
        :param value:
        :return:
        """
        #  à factoriser ? : doublon avec last_name
        authorized_characters = re.compile("^[A-ZÉÈÇÀa-zéèçà\ -]+$")
        if re.match(authorized_characters, value):
            self.__first_name = value.title()
        else:
            raise Exception("First name contains not allowed characters")

    @property
    def gender(self) -> Gender:
        return self.__gender

    @gender.setter
    def gender(self, value: Gender):
        self.__gender = value.title()

    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        self.__birthdate = value
        """
        if type(value) != date:
            value = date(value)  # très faux !! l'idée est de forcer le format date
        
        if date.now - value > 18:
            self.__birthdate = value
        else:
            raise Exception("Player must be over 18")
        """

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, value: int):
        if type(value) == int:
            if value > 0:
                self.__ranking = value
            else:
                raise Exception("Rank must be positive")
        else:
            raise Exception("Rank must be an integer")


class PlayerEncoder(JSONEncoder):
    """
    This subclass contains methods to convert instances of the Python Object Player into a JSon dictionary
    in order to save it into a TinyDB database.
    """
    def __init__(self, player: dict):
        self.player = player

    def default(self, player: dict):
        if isinstance(player, Player):
            return player.__dict__
        else:
            return JSONEncoder.default(self, player)

    def serialize_one_player(self, player: dict):
        """
        This method enables to serialize a single player: from a Python Object to Json.
        :return:
        """
        return PlayerEncoder(player).default(player)

    def save_serialized_player(self, player: dict):
        serialized_player = self.serialize_one_player(player)
        with open('serialized_player.json', 'w') as file:
            json.dump(serialized_player, file, indent=4, ensure_ascii=False)


    def serialize_players(self, players: list):
        """
        This method enables to serialize a list of players: from Python Objects to Json.
        :return:
        """
        return [PlayerEncoder(player).default(player) for player in players]

    def save_list_of_serialized_players(self, players: list):
        serialized_players = self.serialize_players(players)
        with open('serialized_players.json', 'w') as file:
            json.dump(serialized_players, file, indent=4, ensure_ascii=False)


class PlayerDecoder(JSONDecoder):
    """
    This subclass contains methods to convert a JSON dictionary to instances of the Python Object Player
    in order to load it from a TinyDB database.
    """
    def __init__(self, player: str):
        self.player = player

    def decode(self, player: str):
        pass

    def deserialize_one_player(self, player: str):
        """
        This method enables to deserialize a single player: from Json to a Python Object.
        :return:
        """
        return PlayerDecoder(player).decode(player)

    def load_player(self, json_file: str):
        json_file = 'serialized_player.json'
        with open(json_file , 'w'):
            deserialized_player = self.deserialize_one_player(player)
            json.loads(deserialized_player)

    def deserialize_players(self, players: list):
        """
        This method enables to deserialize a list of players: from Json to Python Objects.
        :return:
        """
        return [PlayerDecoder(player).decode(player) for player in players]

    def load_list_of_serialized_players(self, players:list):
        deserialized_players = self.deserialize_players(players)
        json.loads(deserialized_players)