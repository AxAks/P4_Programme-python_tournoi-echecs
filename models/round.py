# coding=utf-8

from models.serializable import Serializable


class Round:
    """
    This is the class for the Python Object: Round
    """
    def __init__(self, matches_list: list):
        self.matches_list = matches_list  # à modifier r ne vaut rien !