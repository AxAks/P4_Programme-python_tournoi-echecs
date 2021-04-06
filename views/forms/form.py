# coding=utf-8

"""
Generic Class for Forms
"""


class Form:
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """
    def __init__(self, program_name, menu_name, previous_page_ctrl, root_page, exiting_message, properties):
        super().__init__(program_name=program_name, menu_name=menu_name,
                         previous_page_ctrl=previous_page_ctrl, root_page=root_page,
                         exiting_message=exiting_message)
        self.properties = properties
