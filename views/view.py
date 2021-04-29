# coding=utf-8

class View:
    """
    This class is a parent Class for Menu and Form screens
    It enables them to  shared some common properties
    """
    def __init__(self, program_name, menu_name, data=None,
                 previous_page_ctrl=None, exiting_message='Program Terminated'):

        self.program_name = program_name
        self.menu_name = f'-{menu_name}-'
        self.data = data
        self.previous_page_ctrl = previous_page_ctrl
        self.exiting_message = exiting_message


    #  pour pouvoir ajouter le cancel sur la navigation formulaire
    #  + pouvoir utiliser des fonctions de menu vers form : View -> Menu ; View -> Form
    # Lister tous les prints ici en fonction ?

