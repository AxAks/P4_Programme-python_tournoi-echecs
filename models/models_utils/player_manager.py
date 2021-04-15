# coding=utf-8
from typing import Union
from uuid import UUID

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.factory import Factory
from models.player import Player


class PlayerManager(Factory):

    def __init__(self):
        self.registry = sf.factories[Player].registry

    def list_registered_players(self) -> list[Player]:
        players_list = []
        for identifier in self.registry:
            player_obj = self.from_identifier_to_player_obj(identifier)
            players_list.append(player_obj)
        return players_list

    def from_identifier_to_player_obj(self, identifier: Union[UUID, str]) -> Player:
        if isinstance(identifier, UUID):
            player_obj = self.registry[identifier]
        elif isinstance(identifier, str):
            identifier = UUID(identifier)
            player_obj = self.registry[identifier]
        else:
            raise AttributeError()
        return player_obj
