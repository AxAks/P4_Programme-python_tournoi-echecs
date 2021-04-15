# coding=utf-8
from typing import Union

from models.models_utils.superfactory import super_factory as sf
from models.models_utils.factory import Factory
from models.tournament import Tournament


class TournamentManager(Factory):

    def __init__(self):
        self.registry = sf.factories[Tournament].registry

    def list_registered_tournaments(self) -> list[Tournament]:
        tournaments_list = []
        for identifier in self.registry:
            tournament_obj = self.from_identifier_to_tournament_obj(identifier)
            tournaments_list.append(tournament_obj)
        return tournaments_list

    def from_identifier_to_tournament_obj(self, identifier):
        tournament_obj = self.registry[identifier]
        return tournament_obj
