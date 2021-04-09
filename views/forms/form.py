# coding=utf-8


class Form():
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """

    def __init__(self, properties, cls):
        self.properties = properties
        self.cls = cls

    def ask_property(self, property_name):  # fonctionne un peu mais pas fini : comment est ce que je lui passe les args   # appelé par Form.add_new, doit etre generique et renvoyer vers une fonction particuliere selon l'objet
        """
        This generic method is used to ask the Player and Tournament in the forms.
        """
        method_name = f'ask_{property_name}'
        method = getattr(self.cls, method_name)
        attribute = method()
        try:
            print(f'{property_name.replace("_", " ").title()} is  : "{attribute}"') # un vieux print illisible pour identifier list de tournament ...
        except AttributeError:
            raise Exception()
        return attribute
