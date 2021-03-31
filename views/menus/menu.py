# coding=utf-8


class Menu:
    """
    This class is a parent Class for all Menu screens
    It enables to navigate through the program.
    """
    def __init__(self, program_name, menu_name,
                 previous_page=None, root_page=False, exiting_message='Program Terminated'):
        self.program_name = program_name
        self.menu_name = f'-{menu_name}-'
        self.previous_page = previous_page
        self.root_page = root_page
        self.exiting_message = exiting_message

    def menu(self) -> None:
        """
        This method displays the different options of the menu.
        """
        for choice in self.choices:
            reformatted_choice_str = choice.__name__.replace('_', ' ').title()
            print(f"{self.choices.index(choice)}: {reformatted_choice_str}")

    def run(self) -> None:
        """
        This method displays the menu and responds to choices made.
        """
        while True:
            print(self.program_name, '\n', self.menu_name, '\n')
            valid_choices = range(len(self.choices))
            choice = -1
            while choice not in valid_choices:
                self.menu()
                _input = input('\nEnter an option: ')
                try:
                    choice = int(_input)
                    if choice not in valid_choices:
                        print(f'-> "{choice}" is not a valid choice <-')
                except ValueError:
                    print(f'-> "{_input}" is not a valid choice <-')

            action = self.choices[choice]
            action()

    def show(self, choices):
        for choice in choices:
            return choice
