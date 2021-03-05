# coding=utf-8

"""
File for different tests on the features of the class Serializable
"""

from models.tournament import Tournament
from tests import sample_values as test_sample

# Class Model
# Test Serialization / Deserialization General


def test_serialize_global(_obj):
    return _obj.serialize()


def test_deserialize_global(_obj_class, attributes_dict):
    _obj = _obj_class(**attributes_dict)
    return _obj



tournament24 = Tournament(**test_sample.tournament24_dict)
serialized_tournament24 = test_serialize_global(tournament24)
deserialized_tournament24 = test_deserialize_global(Tournament, serialized_tournament24)

print("Start: Test Serialization/Deserialization Global")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
print(tournament24.__dict__)
print(deserialized_tournament24.__dict__)
print(test_sample.tournament24_dict)
print(serialized_tournament24)

assert test_sample.tournament24_dict == serialized_tournament24
print("End: Test Serialization/Deserialization Global")
