# coding=utf-8

from enum import Enum
from typing import Union
from uuid import UUID
from models.model import Model


class Match(Model):
    """
    This is the class for the Python Object: Match
    A single match is saved as a tuple of two lists:
    -> ([player1_id, player1_result],[player2_id, player2_result])

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
        the types of data are as follows :
        - player1_id: UUID or String
        - player2_id: UUID or String
        - player1_score: integer or Score
        - player2_score: integer or Score
        """
        super().__init__(('player1_id', 'player2_id', 'player1_score', 'player2_score'), **params)

    @property
    def player1_id(self) -> UUID:
        """
        This method returns player1 ID as an UUID.
        """
        return self.__player1_id

    @property
    def player1_id_pod(self) -> str:
        """
        This method returns player1 ID as a string.
        """
        return str(self.__player1_id)

    @player1_id.setter
    def player1_id(self, value: Union[str, UUID]):
        """
        The setter checks whether the entered value is a string or an UUID
        and sets the attribute as a player UUID
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            try:
                self.__player1_id = UUID(value)
            except AttributeError:
                raise AttributeError()
        elif isinstance(value, UUID):
            try:
                self.__player1_id = value
            except AttributeError:
                raise AttributeError
        else:
            raise AttributeError()

    @property
    def player2_id(self) -> UUID:
        """
        This method returns player2 ID as an UUID.
        """
        return str(self.__player2_id)

    @property
    def player2_id_pod(self) -> str:
        """
        This method returns player2 ID as a string.
        """
        return str(self.__player2_id)

    @player2_id.setter
    def player2_id(self, value: Union[str, UUID]):
        """
        The setter checks whether the entered value is a string or an UUID
        and sets the attribute as a player UUID
        """
        if value is None:
            raise AttributeError()
        if isinstance(value, str):
            self.__player2_id = UUID(value)
        elif isinstance(value, UUID):
            try:
                self.__player2_id = value
            except AttributeError:
                raise AttributeError()
        else:
            raise AttributeError()

    @property
    def player1_score(self) -> Score:
        """
        This method returns the score of player 1 as a Score
        """
        return self.__player1_score

    @property
    def player1_score_pod(self) -> float:
        """
        This method returns the score of player 1 as an integer.
        """
        return self.__player1_score.value

    @player1_score.setter
    def player1_score(self, value: Union[float, Score]):
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
    def player2_score(self) -> Score:
        """
        This method returns the score of player 2 as an integer.
        """
        return self.__player2_score

    @property
    def player2_score_pod(self) -> float:
        """
        This method returns the score of player 2 as an integer.
        """
        return self.__player2_score.value

    @player2_score.setter
    def player2_score(self, value: Union[float, Score]):
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

    # Voir si on surcharge pour avoir un tuple,
    # mais un dict est plus pratique à manipuler
    def serialize(self, properties=None):
        """
        This method enables to serialize Python Objects to simple types handled by TinyDB
        It uses introspection to access the object's attributes and methods.
        """
        if not properties:
            properties = self.properties
        return {property: getattr(self, f"{property}_pod" if hasattr(self, f"{property}_pod") else property)
                for property in self.properties if property in properties}

    def get_match_as_tuple(self): # pas forcement en tuple, si j'y arrive c'est bien !
        # bout de code de serialize extrait en methode pour factoriser dans Serializable.serialize() partout
        return [self.player1_id, self.player1_score], [self.player2_id, self.player2_score]
