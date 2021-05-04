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

    def menu_header(self):
        print('========================')
        print(self.program_name, '\n', self.menu_name)
        print('========================')

    def print_player_infos(self, player):
        print(f'Player: {player.last_name}, {player.first_name}, {player.identifier_pod}\n'
              f'More infos: {player.birthdate_pod}, {player.gender_pod}, {player.ranking}')