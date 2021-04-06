# coding=utf-8
from controllers.controller import Controller
from views.menus.home_menu import HomeMenu


class HomeCtrl(Controller):
    def __init__(self):
        self.menu = HomeMenu()
