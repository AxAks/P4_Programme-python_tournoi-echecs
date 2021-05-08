# coding=utf-8
from utils import clear_terminal
from views.view import View


class Form(View):
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """

    def __init__(self, program_name, menu_name, previous_page_ctrl,
                 properties, cls, not_asked_properties, data=None,):
        super().__init__(program_name=program_name, menu_name=f'-{menu_name}-', data=data,
                         previous_page_ctrl=previous_page_ctrl, exiting_message='Exiting Form')
        self.properties = properties
        self.cls = cls
        self.not_asked_properties = not_asked_properties
        self.data = data

    def ask_property(self, property_name):
        """
        This generic method is used to ask the properties of a object in the subclasses of Form.
        It also enables to quit the form to go back to previous menu
        """
        method_name = f'ask_{property_name}'
        method = getattr(self.cls, method_name)
        attribute = method()
        try:
            self.print_hard_separator()
            if method_name == 'ask_identifiers_list':
                players_list = []
                for identifier in attribute:
                    players_list.append(attribute[identifier])
                print('Tournament Players List is:')
                self.print_soft_separator()
                for player in players_list:
                    self.print_player_general_infos(player)
            else:
                print(f'{property_name.replace("_", " ").title()} is:\n"{attribute}"')
        except AttributeError:
            self.print_error_occurred()
            self.print_to_previous_menu()
            self.previous_page_ctrl().run()

        valid_entry = False
        choices_info = '1: YES, 2: NO, 0: CANCEL FORM'
        input_info = f'Please confirm this information: ({choices_info}): '
        valid_choices = (0, 1, 2)
        wrong_input = 'Invalid choice (1, 2 or 0)'
        while not valid_entry:
            try:
                self.print_hard_separator()
                _input = input(input_info)
                _input = int(_input)
                if _input in valid_choices:
                    if _input == 2:
                        attribute = method()
                    elif _input == 1:
                        valid_entry = True
                    else:
                        self.print_cancelled()
                        self.print_to_previous_menu()
                        if self.data:
                            clear_terminal()
                            self.previous_page_ctrl(self.data).run()
                        else:
                            clear_terminal()
                            self.previous_page_ctrl().run()
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
        self.general_header_menu()
        new_dict = {}
        for _property in self.properties:
            if _property not in self.not_asked_properties:
                new_dict[_property] = self.ask_property(_property)
        return new_dict
