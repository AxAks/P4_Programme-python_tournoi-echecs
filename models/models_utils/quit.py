# coding=utf-8
import sys

from models.models_utils import save


def quit() -> None:
    """
    This method directs to the controller to quit the program at any point in the menu
    It calls the save function before quitting to save the state of the program.
    """
    save.save()
    print(exiting_message)
    quit.quit()


def quit():
    """
    This function exits the program
    """
    sys.exit(0)
