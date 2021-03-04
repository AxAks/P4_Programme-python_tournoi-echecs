# coding=utf-8

"""
File for different tests on the features of the class Tournament
"""

from models.tournament import Tournament
from tests import sample_values as test_sample


# Tests Serialization/Deserialization Tournament
def test_serialize_tournament(tournament_object):
    return tournament_object.serialize()


def test_deserialize_tournament(attributes_dict):
    _obj = Tournament(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Tournament")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
tournament24 = Tournament(**test_sample.tournament24_dict)
serialized_tournament24 = test_serialize_tournament(tournament24)
deserialized_tournament24 = test_deserialize_tournament(serialized_tournament24)
print(f'Dict: {test_sample.tournament24_dict}')
print(f'Object: {deserialized_tournament24.__dict__}')
print(f'Serialized: {serialized_tournament24}')
assert test_sample.tournament24_dict == serialized_tournament24  # le test ne fonctionne plus mais les données sont bonnes
print("End: Test Serialization/Deserialization Tournament")
print(tournament24.identifier)
