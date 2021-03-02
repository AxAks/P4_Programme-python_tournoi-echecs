# coding=utf-8

from enum import Enum
from typing import Union

from models.serializable import Serializable
from models.player import Player


class Match(Serializable):
    """
    This is the class for the Python Object: Match
    A single match is saved as a tuple of two lists:
    -> ([player1, player1_result],[player2, player2_result])

    Multiple matches are not saved here but as a list in the Class Round
    -> Round.matches = [match1, match2, match3]
    """
    Score = Enum("Score", "0 0.5 1")

    def __init__(self, **params: dict):
        errors = []
        attributes = ('player1', 'player2', 'player1_score', 'player2_score')
        for key, value in params.items():
            if key in attributes:
                try:
                    setattr(self, key, value)
                except AttributeError:
                    errors.append(key)
        if errors:
            raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    @property
    def player1(self) -> dict:
        return self.__player1.serialize()

    @player1.setter
    def player1(self, value: Union[dict, Player]):
        if isinstance(value, dict):
            player1 = Player(**value)
            self.__player1 = player1
        elif isinstance(value, Player):
            try:
                self.__player1 = value
            except AttributeError:
                raise Exception(f'Error in the serialization of the attribute: player1')
        else:
            raise AttributeError()

    @property
    def player2(self) -> dict:
        return self.__player2.serialize()

    @player2.setter
    def player2(self, value: Union[dict, Player]):
        if isinstance(value, dict):
            player2 = Player(**value)
            self.__player2 = player2
        elif isinstance(value, Player):
            try:
                self.__player2 = value
            except AttributeError:
                raise Exception(f'Error in the serialization of the attribute: player2')
        else:
            raise AttributeError()

    @property
    def player1_score(self) -> int:
        return self.__player1_score

    @player1_score.setter
    def player1_score(self, value: int):
        if isinstance(value, int):
            try:
                self.__player1_score = value
            except KeyError:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def player2_score(self) -> int:
        return self.__player2_score

    @player2_score.setter
    def player2_score(self, value: int):
        if isinstance(value, int):
            try:
                self.__player2_score = value
            except KeyError:
                raise AttributeError()
        else:
            raise AttributeError()

    def get_match_as_tuple(self):
        # bout de code de serialize extrait en methode pour factoriser dans Serializable.serialize() partout
        return [self.player1, self.player1_score], [self.player2, self.player2_score]
