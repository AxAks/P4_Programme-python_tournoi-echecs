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
                setattr(self, property, data[property] if property in data else None) # à verifier ! erreur sur last_name
                # on met None si on ne trouve pas la property : gerer le cas if None dans setter de chaque property
            except AttributeError:
                errors.append(property)

        if errors:
            raise Exception(f'Error detected in the following fields: {", ".join(errors)}')

    def serialize(self, properties=None):
        """
        This method enables to serialize Python Objects to simple types handled by TinyDB
        It uses introspection to access the object's attributes and methods.
        """

        # à adapter
        if not properties:
            properties = self.properties
        return {property: getattr(self, f"{property}_POD" if hasattr(self, f"{property}_POD") else property)
                for property in self.properties if property in properties}

        """
        # à supprimer !??
        properties_dict = {}
        for property in self.__dict__.name :
            cleaned_property_name = property.replace(f"_{self.__class__.__name__}__", '')
            if hasattr(self, cleaned_property_name + '_pod'):
                properties_dict[cleaned_property_name] = getattr(self, cleaned_property_name + '_pod')()
            else:
                properties_dict[cleaned_property_name] = getattr(self, cleaned_property_name)
        return properties_dict
        """