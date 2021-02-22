# coding=utf-8

from models.serializable import Serializable
from models.players import Player


class Match(Serializable):
    def __init__(self, player1, player2, player1_result, player2_result):
        self.player1 = player1
        self.player2 = player2
        self.player1_result = player1_result
        self.player2_result = player2_result

    @property
    def player1(self) -> object:
        return self.__player1

    @player1.setter
    def player1(self, value: object):
        if isinstance(value, object):
            self.__player1 = value
        else:
            raise AttributeError()

    @property
    def player2(self) -> object:
        return self.__player2

    @player2.setter
    def player2(self, value: object):
        if isinstance(value, object):
            self.__player2 = value
        else:
            raise AttributeError()

    @property
    def player1_result(self) -> int:
        return self.__player1_result

    @player1_result.setter
    def player1_result(self, value: int):
        if isinstance(value, int):
            self.__player1_result = value
        else:
            raise AttributeError()

    @property
    def player2_result(self) -> int:
        return self.__player2_result

    @player2_result.setter
    def player2_result(self, value: int):
        if isinstance(value, int):
            self.__player2_result = value
        else:
            raise AttributeError()
