# coding=utf-8


def quit(self) -> None:
    """
    This method directs to the controller to quit the program at any point in the menu
    It calls the save function before quitting to save the state of the program.
    """
    self.save()
    print(self.exiting_message)
    menu_controller.quit()