# coding=utf-8

"""
File for different tests on the features of the class Match
"""

from models.match import Match
from tests import sample_values as test_sample


# résultats possibles d'un match :
# 1.0 - 0.0
# 0.5 -  0.5
# 0.0 - 1.0
# est ce qu'on créé une règle pour ca ?

match16 = Match(**test_sample.match16_dict)
match_test_serialized = match16.serialize()
match_test_tuple = match16.get_match_as_tuple()

print("Start: Test Serialization/Deserialization Match")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
print(f'Match Dict: {test_sample.match16_dict}')
print(f'Match Object Dict: {match16.__dict__}')
print(f'Deserialized Match: {match_test_serialized}')
print(f'Match Tuple: {match_test_tuple}')

assert test_sample.match16_dict == match_test_serialized
print("End: Test Serialization/Deserialization Match")

print(f'Match 16 Identification: {match16.identifier}')
