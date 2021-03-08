# coding=utf-8

from models.model import Model

# si besoin
# supprimer si pas utile au final


class Creator:
    """
    The Creator class is set as a common/factorized Parent Class for child Objects
    à continuer ....
    """
    def create_object(self, _obj_dict):
        """
        This method creates Object instances
        and hold a registry of the created objects.
        à continuer ...
        """
        # return new object instance
        _obj = self.__class__()
        new_obj = Model(**_obj_dict)
        _obj.registry[
            new_obj.identifier_pod] = new_obj  # registry = {} : key = Player.identifier, value = instance
        return new_obj
        # object = factory_method()