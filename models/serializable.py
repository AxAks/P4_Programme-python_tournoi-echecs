# coding=utf-8

class Serializable:
    """
    The Serializable class is set as a common/factorized Parent Class for serializable Objects and Attributes
    It shares the principe of heritage with its Subclasses : Player, Tournament, Round and Match.
    """
    # def __init__(self, player_uuid, last_name, first_name, birthdate, gender, ranking):
    # je vais le construire après (tests avec Player)

    def serialize(self):
        """
        This method enables to serialize Python Objects to simple types handled by TinyDB
        It uses introspection to access the object's attributes and methods.
        """
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            if hasattr(self, cleaned_attribute_name + '_pod'):
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            else:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict
