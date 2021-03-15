# coding=utf-8

from controllers.creator import Creator


class SuperCreator: # fonctionne pas je ne sais pas pourquoi
    def __init__(self):
        self.creators = {}

    def create_creator(self, factored: type, identifier: str = None) -> Creator:
        creator = Creator(factored,
                          (lambda x: getattr(x, identifier)) if identifier else None)
        if factored not in self.factories:
            self.creators[factored] = creator
        return creator


