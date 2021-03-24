# coding=utf-8



# defs à reprendre et reutiliser autre part !!!!!

# Round: pour entrer les resultats d'un round
# 'name', 'matches', 'end_time', 'start_time'
from views.inputs.generic_inputs import GenericInputs


class RoundInputs(GenericInputs):
    """
    Class listing all possible inputs related to Round
    """
    def __init__(self):
        super().init()

    def ask_name(self):  #  si le format est round+n, on peut incrementer au fur et à mesure
        """
        This method asks for the round's name at the beginning of the round
        """
        return input("Enter Round Name: ")

    def ask_matches(self): # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés
        """"
        This method asks for the list of match results for a round
        """
        pass

    def ask_end_time(self):  # doit etre renseigné automatiquement en fait !
        pass

    def ask_start_time(self):  # doit etre renseigné automatiquement en fait !
        pass
