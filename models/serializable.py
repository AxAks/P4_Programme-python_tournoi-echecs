# coding=utf-8

from enum import Enum


class Serializable:
    """
    The Serializable class is set as a common/factorized Parent Class for serializable Objects and Attributes
    It shares the principe of heritage with its Subclasses : Player, Tournament, Round and Match.
    Gender is a sub-class for the Player's gender : only accept the strings "Male" and "Female".
    """
    Gender = Enum("Gender", "MALE FEMALE")

    def __init__(self, **params):
        player_attributes = ('player_uuid', 'last_name', 'first_name', 'birthdate', 'gender', 'ranking')
        tournament_attributes = ('tournament_name', 'location', 'dates', 'players',
                                 'time_control', 'description', 'rounds_list', 'rounds')
        round_attributes = ('round_name', 'tournament', 'matches', 'end_time', 'start_time')
        match_attributes = ('player1', 'player2', 'player1_score', 'player2_score')

        all_attributes = (player_attributes + tournament_attributes + round_attributes + match_attributes)

        errors = []
        for key, value in params.items():
            if key in all_attributes:
                try:
                    setattr(self, key, value)
                except AttributeError:
                    errors.append(key)

        if errors:
            raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    def serialize(self):
        """
        This method enables to serialize Python Objects to simple types handled by TinyDB
        It uses introspection to access the object's attributes and methods.
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict
