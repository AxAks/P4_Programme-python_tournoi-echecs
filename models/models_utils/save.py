# coding=utf-8

def save(self) -> None:
    """
    This method directs to the controller to save the state of the program at any at any point in the menu.
    """
    print(f'Saving current program state')
    menu_controller.save()
    print('Program state saved')