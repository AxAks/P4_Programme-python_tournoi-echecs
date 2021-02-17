# coding=utf-8

import re
import json # ne sera pas utilisé

from datetime import date, datetime, timedelta
from typing import Union
from enum import Enum
from json import JSONEncoder, JSONDecoder # ne sera pas utilisé

from models.serializable import Serializable


class Player(Serializable):
    """
    This is the class for the Python Object: Player
    Gender is an sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")

    def __init__(self, last_name: str, first_name: str, birthdate: Union[str, date],
                 gender: Union[str, Gender], ranking: int):
        errors = []
        try:
            self.last_name = last_name
        except AttributeError:
            errors.append('Last name')
        try:
            self.first_name = first_name
        except AttributeError:
            errors.append('First name')
        try:
            self.birthdate = birthdate
        except AttributeError:
            errors.append('Birthdate')
        try:
            self.gender = gender
        except AttributeError:
            errors.append('Gender')
        try:
            self.ranking = ranking
        except AttributeError:
            errors.append('Ranking')

        if errors:
            raise Exception(", ".join(errors))

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
            raise AttributeError()

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
            raise AttributeError()

    @property
    def gender(self) -> Gender:
        return self.__gender

    @property
    def gender_pod(self) -> str:
        return self.__gender.value()

    @gender.setter
    def gender(self, value: Gender):
        self.__gender = value.title()

    @property
    def birthdate(self) -> Union[str, date]:
        return self.__birthdate

    @property
    def birthdate_pod(self) -> str:
        return self.__birthdate.isoformat()

    @birthdate.setter
    def birthdate(self, value: Union[str, date]):
        if isinstance(value, str):
            value = datetime.strptime(value, '%Y/%m/%d').date()  # l'idée est de forcer le format date, a retravailler, bon que si on entre une date au format YYYY/MM/DD
            self.__birthdate = value
            """
            if date.today() - value >= date.age(12): # limite d'age, ne fonctionne pas ... timedelta >= int pas accepté
                self.__birthdate = value
            else:
                raise AttributeError()
            self.__birthdate = value
            """
        else:
            self.__birthdate = value

    @property
    def ranking(self) -> int:
        return self.__ranking

    @ranking.setter
    def ranking(self, value: int):
        if type(value) == int:
            if 0 < value < 3000:
                self.__ranking = value
            else:
                raise AttributeError()
        else:
            raise AttributeError()


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

    def dump_serialized_player(self, player: dict) -> str:
        serialized_player = self.serialize_one_player(player)
        return json.dumps(serialized_player, indent=4)

    def save_serialized_player_to_file(self, player: dict):
        serialized_player = self.serialize_one_player(player)
        with open('serialized_player.json', 'w') as output_file:
            json.dump(serialized_player, output_file, indent=4, ensure_ascii=False)

    def serialize_players(self, players: list):
        """
        This method enables to serialize a list of players: from Python Objects to Json.
        :return:
        """
        return [PlayerEncoder(player).default(player) for player in players]

    def dump_list_of_serialized_players(self, players: list):
        serialized_players = self.serialize_players(players)
        return json.dumps(serialized_players, indent=4)

    def save_list_of_serialized_players_to_file(self, players: list):
        serialized_players = self.serialize_players(players)
        with open('serialized_players.json', 'w') as output_file:
            json.dump(serialized_players, output_file, indent=4, ensure_ascii=False)











"""
class PlayerDecoder(JSONDecoder):
    
    This subclass contains methods to convert a JSON dictionary to instances of the Python Object Player
    in order to load it from a TinyDB database.
    
    def __init__(self, player_string: str):
        self.player_string = player_string

    def decode(self, player_string: str):
        pass

    def deserialize_one_player(self, player_string: str):
        
        This method enables to deserialize a single player: from Json to a Python Object.
        :return:
        
        print(PlayerDecoder(player_string).decode(player_string))

    def load_player(self, player_string: str):
        # deserialized_player = \
        json.loads(player_string)
        # self.deserialize_one_player(player)
        # json.loads(deserialized_player)

    def deserialize_players(self, players: list):
        
        This method enables to deserialize a list of players: from Json to Python Objects.
        :return:
        
        return [PlayerDecoder(player).decode(player) for player in players]

    def load_list_of_serialized_players(self, players:list):
        deserialized_players = self.deserialize_players(players)
        json.loads(deserialized_players)



# test
player2_string = '{"_Player__last_name": "Berd",' \
                 ' "_Player__first_name": "Bernard",' \
                 ' "_Player__birthdate": "01/03/1982",' \
                 ' "_Player__gender": "Male",' \
                 ' "_Player__ranking": 3}'
"""