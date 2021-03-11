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


tournament35 = Tournament(**test_sample.tournament35_dict)
serialized_tournament35 = test_serialize_tournament(tournament35)
deserialized_tournament35 = test_deserialize_tournament(serialized_tournament35)


print("Start: Test Serialization/Deserialization Tournament")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
print(f'Dict: {test_sample.tournament35_dict}')
print(f'Object 1:{tournament35.__dict__}')
print(f'Object 2: {deserialized_tournament35.__dict__}')
print(f'Serialized: {serialized_tournament35}')

assert test_sample.tournament35_dict == serialized_tournament35
# assert tournament35.__dict__== deserialized_tournament35.__dict__

print("End: Test Serialization/Deserialization Tournament")

print(f'Tournament Identification: {tournament35.identifier}')