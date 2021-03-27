# coding=utf-8

"""
This file contains reusable general tool functions
"""

from uuid import UUID


def check_uuid4_format(string_to_check: str) -> bool:

    valid_uuid4 = False
    try:
        string_to_check = UUID(str(string_to_check), version=4)
        valid_uuid4 = True
    except ValueError:
        print('Invalid uuid')
