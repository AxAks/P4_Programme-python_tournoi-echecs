# coding=utf-8

"""
File to launch the program:
from the terminal : python chess_tournament_manager.py
the file is located at the root of the project,
it redirects to the Home Menu file in the views directory.
"""

from views.menus.home_menu import HomeMenu

if __name__ == '__main__':
    HomeMenu().run()
