# coding=utf-8

from enum import Enum
from typing import Union

from models.model import Model
from models.player import Player


class Match(Model):
    """
    This is the class for the Python Object: Match
    A single match is saved as a tuple of two lists:
    -> ([player1, player1_result],[player2, player2_result])

    Multiple matches are not saved here but as a list in the Class Round
    -> Round.matches = [match1, match2, match3]
    """

    class Score(Enum):
        WIN = 1.0
        LOSE = 0.0
        TIE = 0.5

    def __init__(self, **params: dict):
        # homogeneiger et documenter comme Player
        """
        The initialization of the class Match checks wheter there is a missing parameter in the entered values.
        the type of data are as follows :
        - player1:
        - player2:
        - player1_score:
        - player2_score:
        """
        super().__init__(('player1', 'player2', 'player1_score', 'player2_score'), **params)
        match_attributes = ('player1', 'player2', 'player1_score', 'player2_score')
        errors = []
        missing_attributes = []
        for key, value in params.items():
            if key in match_attributes:
                try:
                    setattr(self, key, value)
                except AttributeError:
                    errors.append(key)
            else:
                missing_attributes.append(key)

        if missing_attributes:
            raise AttributeError(f'The following attributes do not exist'
                                 f' for the object {self.__class__.__name__}:'
                                 f' {", ".join(missing_attributes)}')
        if errors:
            raise Exception(f'Errors detected in the following fields: {", ".join(errors)}')

    @property
    def player1(self) -> dict:
        """
        This method returns the player 1 as a dict.
        """
        return self.__player1.serialize()

    @player1.setter
    def player1(self, value: Union[dict, Player]):
        """
        The setter checks whether the entered value is a dict or a Player object
        and sets the attribute as a Player object
        """
        if value is None:
            raise AttributeError()
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
        """
        This method returns the player 2 as a dict.
        """
        return self.__player2.serialize()

    @player2.setter
    def player2(self, value: Union[dict, Player]):
        """
        The setter checks whether the entered value is a dict or a Player object
        and sets the attribute as a Player object
        """
        if value is None:
            raise AttributeError()
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
    def player1_score(self) -> Score:  # à revoir !
        """
        This method returns the score of player 1 as an integer.
        """
        return self.__player1_score.name

    def player1_score_pod(self) -> float:  # à revoir !
        """
        This method returns the score of player 1 as an integer.
        """
        return self.__player2_score

    @player1_score.setter
    def player1_score(self, value: Union[float, Score]):  # à revoir !
        """
        This setter checks that the entered value is an integer
        and sets it as a Score.
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, int):
            value =float(value)
            try:
                self.__player1_score = self.Score(value)
            except KeyError:
                raise AttributeError()
        if isinstance(value, float):
            try:
                self.__player1_score = self.Score(value)
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Score):
            self.__player1_score = value
        else:
            raise AttributeError()

    @property
    def player2_score(self) -> Score:  # à revoir !
        """
        This method returns the score of player 2 as an integer.
        """
        return self.__player2_score.name

    def player2_score_pod(self) -> float:  # à revoir !
        """
        This method returns the score of player 2 as an integer.
        """
        return self.__player2_score

    @player2_score.setter
    def player2_score(self, value: Union[float, Score]):  # à revoir !
        """
        This setter checks that the entered value is an integer
        and sets the property to a Score.
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, float):
            try:
                self.__player2_score = self.Score(value)
            except KeyError:
                raise AttributeError()
        elif isinstance(value, self.Score):
            self.__player2_score = value
        else:
            raise AttributeError()

    def get_match_as_tuple(self): # pas forcement en tuple, si j'y arrive c'est bien !
        # bout de code de serialize extrait en methode pour factoriser dans Serializable.serialize() partout
        return [self.player1, self.player1_score], [self.player2, self.player2_score]
