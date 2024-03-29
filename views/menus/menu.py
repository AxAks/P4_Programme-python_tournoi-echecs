# coding=utf-8

from controllers import home_controller
from controllers.controller import Controller
from views.view import View


class Menu(View):
    """
    This class is a parent Class for all Menu screens
    It enables to navigate through the program.
    """

    def __init__(self, program_name, menu_name, data=None,
                 previous_page_ctrl=None, current_page_ctrl=None,
                 root_page=False, exiting_message='Program Terminated'):
        super().__init__(program_name=program_name, menu_name=f'-{menu_name}-', data=data,
                         previous_page_ctrl=previous_page_ctrl, exiting_message=exiting_message)
        self.current_page_ctrl = current_page_ctrl
        self.root_page = root_page
        self.choices = [self.quit, self.home, self.back, self.load, self.save]

    def show(self) -> None:
        """
        This method displays the different options of the menu.
        The options are set in the attributes of the class ("choices" and "specific_menu_choices")
        """
        self.general_header_menu()
        for choice in self.choices:
            reformatted_choice_str = choice.__name__.replace('_', ' ').title()
            print(f"{self.choices.index(choice)}: {reformatted_choice_str}")
        self.print_hard_separator()

    @staticmethod
    def home() -> None:
        """
        This method leads to the Home Menu via the Home controller
        """
        home_controller.HomeCtrl().run()

    def back(self) -> None:
        """
        This method enables to go back to the previous screen
        if the screen is the root menu, it calls the quit method to make the program quit.
        """
        if self.root_page:
            self.quit()
        else:
            self.previous_page_ctrl().run()

    def quit(self) -> None:
        """
        This method directs to the controller to quit the program at any point in the menu
        It calls the save function before quitting to save the state of the program.
        """
        Controller().save()
        print(f'{self.exiting_message}')
        Controller().quit()

    def load(self) -> None:
        """
        This method directs to the controller to load a program state from the database file at any point in the menu
        It then reloads the current menu screen
        """
        Controller().load()
        if self.data is None:
            self.current_page_ctrl().run()
        else:
            self.current_page_ctrl(self.data).run()

    def save(self) -> None:
        """
        This method directs to the controller to save the program state at any point in the menu
        It then reloads the current menu screen.
        """
        Controller().save()
        if self.data is None:
            self.current_page_ctrl().run()
        else:
            self.current_page_ctrl(self.data).run()
