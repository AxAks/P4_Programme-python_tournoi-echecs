# coding=utf-8

from constants import ROUND_PROPERTIES
from views.forms.form import Form
from views.inputs.generic_inputs import ask_alphanumerical_string


class NewRoundForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """

    def __init__(self):
        super().__init__(properties=ROUND_PROPERTIES, cls=self)

    def add_new_round(self) -> dict:  # à passer en tant que add_new (générique) dans Form, si possible, si générique
        new_round_dict = {}
        for _property in self.properties:
            # if _property != '':  # à voir!
            new_round_dict[_property] = self.ask_property(_property)
        return new_round_dict

    # à voir
    def ask_name(self, input_info="Enter name: "):
        # Comme la methode de Tournament !!!! #  si le format est round+n, on peut incrementer au fur et à mesure
        """
        This method asks for the round's name at the beginning of the round
        """
        return ask_alphanumerical_string(input_info)

    def ask_matches(self):
        # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés //controller
        """"
        This method asks for the list of match results for a round
        """
        pass

    def ask_end_time(self):  # doit etre renseigné automatiquement en fait !
        pass

    def ask_start_time(self):  # doit etre renseigné automatiquement en fait !
        pass

