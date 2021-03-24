# coding=utf-8

from models.factory import Factory


class SuperFactory:
    def __init__(self):
        self.factories = {}

    def create_factory(self, factored: type) -> Factory:
        factory = Factory(factored)
        if factored not in self.factories:
            self.factories[factored] = factory
        return factory


super_factory = SuperFactory()
