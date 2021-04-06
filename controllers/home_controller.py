# coding=utf-8
from views.menus.home_menu import HomeMenu

def run() -> None:
    """
    This method displays the menu and responds to choices made.
    """
    valid_choices = range(len(HomeMenu().choices))
    choice = -1
    while choice not in valid_choices:
        HomeMenu().show()
        _input = input('Enter an option: ')
        try:
            choice = int(_input)
            if choice not in valid_choices:
                print(f'-> "{choice}" is not a valid choice <-')
        except ValueError:
            print(f'-> "{_input}" is not a valid choice <-')

    action = HomeMenu().choices[choice]
    action()
