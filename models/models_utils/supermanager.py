# coding=utf-8

from models.models_utils.manager import Manager


class SuperManager:

    def __init__(self):
        self.managers = {}

    def create_manager(self, factored: type) -> Manager:
        """
        This method creates factories
        """
        manager = Manager(factored)
        if factored not in self.managers:
            self.managers[factored] = manager
        return manager


super_manager = SuperManager()
