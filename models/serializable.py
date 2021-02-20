# coding=utf-8


class Serializable:
    """
    This class enables to serialize Python Object to simple types handled by TinyDB
    """

    def serialize(self):
        attributes_dict = {}
        for attribute in self.__dict__.keys():
            cleaned_attribute_name = attribute.replace(f"_{self.__class__.__name__}__", '')
            try:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name + '_pod')()
            except AttributeError:
                attributes_dict[cleaned_attribute_name] = getattr(self, cleaned_attribute_name)
        return attributes_dict

    def serialize_list_of_objects(self, _obj_dict_list): # foireux, à corriger
        # [self.serialize() for _obj_dict in _obj_dict_list]
        serialized_objs_list = []
        for _obj_dict in _obj_dict_list:
            serialized_obj = self.serialize(_obj_dict)
            serialized_objs_list.append(serialized_obj)
        return serialized_objs_list
