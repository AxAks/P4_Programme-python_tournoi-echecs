# coding=utf-8

class Model:
    """
    The Model class is set as a common/factorized Parent Class for child Objects and serializable properties
    It shares the principe of heritage with its subclasses : Player, Tournament, Round and Match.
    """

    def __init__(self, properties, **data):
        """
        The initialization in Model checks whether the properties of the child Class object exist in the
        provided data and assign them the matching value.
        properties : properties of the child objects
        data : information provided for the object to be initialized
        """
        self.properties = properties
        errors = []
        for property in properties:
            try:
                setattr(self, property, data[property] if property in data else None)
                # et uuid (quand on trouve pas l'attribut dans data : pb ! pas géré) on met la valeur à None mais ca pose pb derriere
                # on met None si on ne trouve pas la property : gerer le cas if None dans setter de chaque property
            except AttributeError:
                errors.append(property)

        if errors:
            raise Exception(f'Error detected in the following fields for {self.__class__.__name__}: {", ".join(errors)}')

    def serialize(self, properties=None):
        """
        This method enables to serialize Python Objects to simple types handled by TinyDB
        It uses introspection to access the object's attributes and methods.
        """

        # à adapter
        if not properties:
            properties = self.properties
        return {property: getattr(self, f"{property}_pod" if hasattr(self, f"{property}_pod") else property)
                for property in self.properties if property in properties}
