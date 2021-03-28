# coding=utf-8

from controllers import menu_controller


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
        self.choices = [self.home, self.back,  self.load, self.save, self.quit,]

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

    def home(self) -> None:
        """
        This method enables to go back to Home page
        from any point of the program menu.
        """
        menu_controller.to_home_menu()

    def back(self) -> None:
        """
        This method enables to go back to the previous screen
        if the screen is the root menu, it directs to the controller to make the program quit.
        """
        if self.root_page:
            self.quit()
        else:
            self.previous_page.run()

    def quit(self) -> None:
        """
        This method directs to the controller to quit the program at any point in the menu
        It calls the save function before quitting to save the state of the program.
        """
        self.save()
        print(self.exiting_message)
        menu_controller.quit()

    def load(self, database_file) -> None:  # on chargera depuis TinyDB/JSon file : deserialisation de tous les Players et Tournaments (instanciation via creators)
        """
        This method directs to the controller
        to load a previously saved state of the program from a database file at any time.
        """
        menu_controller.load()


    def save(self) -> None:  # on enregistrera dans TinyDB apres serialisation de tous les Players et Tournaments (via les registres)
        """
        This method directs to the controller to save the state of the program at any at any point in the menu.
        """
        print(f'Saving current program state')
        menu_controller.save()
        print('Program state saved')  # passer le print dans Menu().save() quand fonction ecrite
