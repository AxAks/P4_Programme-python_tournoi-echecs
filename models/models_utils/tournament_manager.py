# coding=utf-8

from models.models_utils.supermanager import super_manager as sm
from models.models_utils.manager import Manager
from models.tournament import Tournament


class TournamentManager(Manager):

    def __init__(self):
        self.registry = sm.managers[Tournament].registry

    def list_registered_tournaments(self) -> list[Tournament]:
        tournaments_list = []
        for identifier in self.registry:
            tournament_obj = self.from_identifier_to_tournament_obj(identifier)
            tournaments_list.append(tournament_obj)
        return tournaments_list

    def from_identifier_to_tournament_obj(self, identifier):
        tournament_obj = self.registry[identifier]
        return tournament_obj
