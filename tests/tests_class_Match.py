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


match28 = Match(**test_sample.match28_dict)
match_test_serialized = match28.serialize()
match_test_tuple = match28.get_match_as_tuple()

print("Start: Test Serialization/Deserialization Match")
print("No AssertionError returned means the test passed\nA problem returns an Assertion Error")
print(f'Match Dict: {test_sample.match28_dict}')
print(f'Match Object Dict: {match28.__dict__}')
print(f'Deserialized Match: {match_test_serialized}')
print(f'Match Tuple: {match_test_tuple}')
print("End: Test Serialization/Deserialization Match")
assert test_sample.match28_dict == match_test_serialized
