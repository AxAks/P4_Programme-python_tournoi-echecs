# coding=utf-8

from models.serializable import Serializable


class Match(Serializable):
    def __init__(self, player1, player2, player1_result, player2_result):
        self.player1 = player1
        self.player2 = player2
        self.player1_result = player1_result
        self.player2_result = player2_result
