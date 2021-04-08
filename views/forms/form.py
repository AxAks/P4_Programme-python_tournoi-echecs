# coding=utf-8

"""
Generic Class for Forms
"""


class Form:
    """
    This class is a parent Class for all Forms
    It enables the user to enter data and return the data as dicts.
    """

    def __init__(self, properties):
        self.properties = properties
