# coding=utf-8

class Model:
    """
    The Model class is set as a common/factorized Parent Class for child Objects and serializable properties
    It shares the principe of heritage with its subclasses : Player, Tournament, Round and Match.
    """

    def __init__(self, properties, **data):
        """
        The initialization of all classes is done in this parent class Model
        The initialization for Model checks whether the properties of the child Class object exist in the
        provided data and assign them the matching value.
        properties : properties of the child objects
        data : information provided for the object to be initialized
        """
        self.properties = properties
        errors = []
        for _property in properties:
            try:
                setattr(self, _property, data[_property] if _property in data else None)
            except AttributeError:
                errors.append(_property)
        if errors:  #  il ne faut pas que le programme s'arrete mais plutot redirige au Home Menu ex : dates de tournamenr debut/fin
            raise Exception(f'Error detected '
                            f'in the following fields for {self.__class__.__name__}: {", ".join(errors)}')

    def serialize(self, properties=None):
        """
        This generic method, along with getters and setters in the child classes,
        enables to serialize Python Objects to simple types object (PODs or plain old data) handled by TinyDB.
        """
        if not properties:
            properties = self.properties
        return {_property: getattr(self, f"{_property}_pod" if hasattr(self, f"{_property}_pod") else _property)
                for _property in self.properties if _property in properties}
