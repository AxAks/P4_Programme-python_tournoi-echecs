# coding=utf-8
"""
File for different tests on the features of the class Round
"""

from models.round import Round
from tests import sample_values as test_sample


# Serialization / Deserialization
def test_serialize_round(round_object):
    return round_object.serialize()


def test_deserialize_round(attributes_dict):
    _obj = Round(**attributes_dict)
    return _obj


print("Start: Test Serialization/Deserialization Round")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")

round1 = Round(**test_sample.round1_dict)
serialized_round1 = test_serialize_round(round1)
deserialized_round1 = test_deserialize_round(serialized_round1)


print('---')
print(f'ICI -> Round 1 Dict : {test_sample.round1_dict}')
print(f'ICI -> Round 1 serialized {serialized_round1}')
print('---')
print(f'Round 1 Object : {round1}')
print(f'Round 1 Object Details{round1.__dict__}')
print(f'Round 1 deserialized {deserialized_round1.__dict__}')
assert test_sample.round1_dict == serialized_round1
assert round1.__dict__ == deserialized_round1.__dict__
print("End: Test Serialization/Deserialization Round")
