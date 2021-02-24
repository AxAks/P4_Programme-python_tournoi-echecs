# coding=utf-8

from enum import Enum
from typing import Union

from models.serializable import Serializable
from models.players import Player


class Match(Serializable):
    # à ré-écrire !!
    """
    This is the class for the Python Object: Match

    Un match unique doit etre stocké sous la forme d'un tuple contenant deux listes :
    -> match1 = ([player1, player1_result],[player2, player2_result])

    Les matchs multiples doivent être stockés sous forme de liste sur l'instance du tour:
    -> matches = [match1, match2, match3]
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
    def player1(self) -> object:
        return self.__player1

    @property
    def player1_pod(self) -> str:
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

    @property
    def player2_pod(self) -> str:
        return self.__player2

    @player2.setter
    def player2(self, value: object):
        if isinstance(value, object):
            self.__player2 = value
        else:
            raise AttributeError()

    @property
    def player1_score(self) -> Union[int, Score]:
        return self.__player1_score

    @player1_score.setter
    def player1_score(self, value:  Union[int, Score]):
        if isinstance(value, int):
            self.__player1_score = value
        else:
            raise AttributeError()

    @property
    def player2_score(self) ->  Union[int, Score]:
        return self.__player2_score

    @player2_score.setter
    def player2_score(self, value:  Union[int, Score]):
        if isinstance(value, int):
            self.__player2_score = value
        else:
            raise AttributeError()

    def serialize(self) -> dict:
        """
        This method overrides the Serializable.serialize() method to convert Match Object
        into a tuple of 2 lists [player, score].
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if cleaned_attribute_name in ('player1', 'player2'):
                try:
                    player_infos_dict = Serializable.serialize(self.__dict__[attribute])
                    attributes_dict[cleaned_attribute_name] = player_infos_dict
                    continue
                except AttributeError:
                    raise Exception(f'Error in the serialization of the attribute: {cleaned_attribute_name}')
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        match_tuple = \
            (
                [attributes_dict['player1'],
                 attributes_dict['player1_score']],
                [attributes_dict['player2'],
                 attributes_dict['player2_score']]
            )
        return match_tuple