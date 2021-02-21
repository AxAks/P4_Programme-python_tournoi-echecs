# coding=utf-8

from models.serializable import Serializable


class Round:
    """
    This is the class for the Python Object: Round
    """
    def __init__(self, matches: list):
        self.matches = matches
