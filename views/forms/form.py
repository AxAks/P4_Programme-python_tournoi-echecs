# coding=utf-8
from views.menus.menu import Menu


class Form(Menu):
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """

    def __init__(self, properties, cls, not_asked_properties):
        self.properties = properties
        self.cls = cls
        self.not_asked_properties = not_asked_properties

    def ask_property(self, property_name):  # fonctionne un peu mais pas fini : # appelé par Form.add_new, doit etre generique et renvoyer vers une fonction particuliere selon l'objet
        """
        This generic method is used to ask the properties of a object in the subclasses of Form.
        """
        method_name = f'ask_{property_name}'
        method = getattr(self.cls, method_name)
        attribute = method()
        try:
            print(f'{property_name.replace("_", " ").title()} is : "{attribute}"') # un vieux print illisible pour identifier list de tournament ...
        except AttributeError:
            raise Exception()  # doit ramener au Home Menu et non quitter le programme !
        attribute = self.validate_input(attribute, method)
        return attribute

    # à travailler, l'idée est d'extraire une méthode generale de verification des inputs:mais pb de attribute = method()
    # et à mettre dans generic_inputs en tant que fonction
    def validate_input(self, attribute, method):
        valid_entry = False
        choices_info = '1: YES, 2: NO'
        input_info = f'Please confirm this entry? ({choices_info}): '
        valid_choices = (1, 2)
        wrong_input = 'Invalid choice (1 or 2), please retry...'
        while not valid_entry:
            try:
                _input = input(input_info)
                _input = int(_input)
                if _input in valid_choices:
                    if _input == 2:
                        attribute = method()
                    else:
                        valid_entry = True
                else:
                    print(wrong_input)
            except ValueError:
                print(wrong_input)
        return attribute

    def add_new(self) -> dict:
        """
        This method asks all the required info about a specific object.
        It returns the info as a dict
        """
        new_dict = {}
        for _property in self.properties:
            if _property not in self.not_asked_properties:
                new_dict[_property] = self.ask_property(_property)
        return new_dict