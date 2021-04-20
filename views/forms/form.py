# coding=utf-8
from utils import validate_input
from views.menus.menu import Menu


class Form:
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """

    def __init__(self, properties, cls, not_asked_properties, data=None, form_name=None):
        self.properties = properties
        self.cls = cls
        self.not_asked_properties = not_asked_properties
        self.data = data
        self.form_name = form_name

    def ask_property(self, property_name):
        """
        This generic method is used to ask the properties of a object in the subclasses of Form.
        """
        method_name = f'ask_{property_name}'
        method = getattr(self.cls, method_name)
        attribute = method()
        try:
            print(f'{property_name.replace("_", " ").title()} is :\n"{attribute}"')
        except AttributeError:
            print('An Error has occurred, back to home menu')
            # doit ramener au Home Menu et non quitter le programme ! possible si heritage de Menu
        attribute = validate_input(attribute, method)  # ajouter la possibilité de sortir du formulaire
        return attribute

    def add_new(self) -> dict:
        """
        This method asks all the required info about a specific object.
        It returns the info as a dict
        """
        print('========================')
        print(self.form_name)
        print('========================')
        new_dict = {}
        for _property in self.properties:
            if _property not in self.not_asked_properties:
                new_dict[_property] = self.ask_property(_property)  # gere l'erreur ici !
        return new_dict
