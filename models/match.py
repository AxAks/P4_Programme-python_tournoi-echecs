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

    def __init__(self, player1: Player, player2: Player, player1_score: Union[int, Score],
                 player2_score: Union[int, Score]):
        errors = []
        try:
            self.player1 = player1
        except AttributeError:
            errors.append('Player 1')
        try:
            self.player2 = player2
        except AttributeError:
            errors.append('Player 2')
        try:
            self.player1_score = player1_score
        except AttributeError:
            errors.append('Score Player 1')
        try:
            self.player2_score = player2_score
        except AttributeError:
            errors.append('Score Player 2')

        if errors:
            raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    @property
    def player1(self) -> dict:
        return self.__player1

    @player1.setter
    def player1(self, value: Union[dict, Player]):
        if isinstance(value, dict):
            player1 = Player(**value)
            serialized_player1 = player1.serialize()
            self.__player1 = serialized_player1
        elif isinstance(value, Player):
            try:
                player_infos_dict = Serializable.serialize(self.__dict__[value])
                self.__player1 = player_infos_dict
            except AttributeError:
                raise Exception(f'Error in the serialization of the attribute: player1')
        else:
            raise AttributeError()

    @property
    def player2(self) -> Union[dict, Player]:
        return self.__player2

    @player2.setter
    def player2(self, value: Union[dict, Player]):
        if isinstance(value, dict):
            player2 = Player(**value)
            serialized_player2 = player2.serialize()
            self.__player2 = serialized_player2
        elif isinstance(value, Player):
            try:
                player_infos_dict = Serializable.serialize(self.__dict__[value])
                self.__player2 = player_infos_dict
            except AttributeError:
                raise Exception(f'Error in the serialization of the attribute: player1')
        else:
            raise AttributeError()

    @property
    def player1_score(self) -> Union[int, Score]:
        return self.__player1_score

    @property
    def player1_score_pod(self) -> int:
        return self.__player1_score.name

    @player1_score.setter
    def player1_score(self, value:  Union[int, Score]):
        if isinstance(value, int):
            try:
                self.__player1_score = value
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Score): # pas testé !
            self.__player1_score = self.Score[value]
        else:
            raise AttributeError()

    @property
    def player2_score(self) -> Union[int, Score]:
        return self.__player2_score

    @property
    def player2_score_pod(self) -> int:
        return self.__player2_score.name

    @player2_score.setter
    def player2_score(self, value:  Union[int, Score]):
        if isinstance(value, int):
            try:
                self.__player2_score = value
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Score):
            self.__player2_score = self.Score[value]
        else:
            raise AttributeError()

    def serialize(self) -> tuple[list, list]:
        """
        This method overrides the Serializable.serialize() method to convert Match Object
        into a list of 2 tuples [player, score].
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)

        # il faudrait sortir ce bout de code pour factoriser et seulement utiliser Serializable.serialize() partout
        match_tuple = \
            (
                [attributes_dict['player1'],
                 attributes_dict['player1_score']],
                [attributes_dict['player2'],
                 attributes_dict['player2_score']]
            )
        return match_tuple
