# coding=utf-8

from models.serializable import Serializable


class Match(Serializable):
    def __init__(self, white_player, black_player, result, ):
        self.white_player = white_player
        self.black_player = black_player
        self.result = result
