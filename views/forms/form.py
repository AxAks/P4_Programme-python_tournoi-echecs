# coding=utf-8

"""
Generic Class for Forms
"""
from views.menus.menu import Menu


class Form(Menu):
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """
    def __init__(self):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Form')
