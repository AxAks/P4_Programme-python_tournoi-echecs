# coding=utf-8

import re
from datetime import date
from uuid import UUID

from constants import ALPHABETICAL_STRING_RULE, RANKING_RANGE, ALPHA_NUMERICAL_STRING_RULE

from controllers.factory import Factory


class GenericInputs:
    """
    Generic Parent Class for all possible inputs
    """
    def __init__(self):
        pass

    """
    def __init__(self, properties, *args):
        self.properties = properties
        errors = []
        try:
            [setattr(self, _property, f'aks_{args}') for _property in properties]
        except AttributeError:
            errors.append(f'aks_{args}')
        if errors:
            raise Exception(f'The following Method(s)'
                            f' could not be found in {self.__class__.__name__}: {", ".join(errors)}')
    """

    def ask_properties(self, *args):  # fonctionne un peu mais pas fini : comment est ce que je lui passe les args   # appelé par Form.add_new, doit etre generique et renvoyer vers une fonction particuliere selon l'objet
        for arg in args:
            method_name = f'ask_{arg}'
            my_cls = GenericInputs() # voir comment rendre la classe variable ou générique Player, Tournament, (Round et Match)
            try:
                method = getattr(my_cls, method_name)
            except Exception as e:
                raise Exception(e)
        return method #f'ask{arg}()' #pb si deux objets ont des attributs identiques -> surement qu'ils font la meme chose, à voir

    @property
    def ask_last_name(self) -> str:
        """
        This method asks for the player's last name
        and checks the formatting of the string
        """
        input_info = "Enter Last Name: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    @property
    def ask_first_name(self) -> str:
        """
        This method asks for the player's first name
        and checks the formatting of the string
        """
        input_info = "Enter First Name: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input


GenericInputs().ask_properties('last_name', 'first_name')  # Ne pas passer les éléments manuellement !
