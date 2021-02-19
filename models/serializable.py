# coding=utf-8


class Serializable:
    """
    This class enables to serialize Python Object to simple types handled by TinyDB
    """

    def serialize(self):
        attr_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            try:
                attr_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            except AttributeError:
                attr_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        print(attr_dict)
