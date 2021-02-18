# coding=utf-8


class Serializable:
    """
    This class enables to serialize Python Object to simple types handled by TinyDB
    """
    def __init__(self, python_object):
        self.python_object = python_object

    def serialize(self):
        pass
