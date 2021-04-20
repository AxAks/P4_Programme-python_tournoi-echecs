# coding=utf-8
from typing import Union
from uuid import UUID

from models.models_utils.supermanager import super_manager as sm
from models.models_utils.manager import Manager
from models.player import Player


class PlayerManager(Manager):

    def __init__(self):
        self.registry = sm.managers[Player].registry

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

    def from_player_obj_to_identifier_str(self, player_obj: Player) -> str:
        identifier = player_obj.identifier_pod
        return identifier
