# coding=utf-8

from datetime import date
from enum import Enum


class Tournament:
    """
    This is the class for the Python Object: Tournament
    """
    class Time_control(Enum):
        """
        Intermediate class for the tournaments's time control :
        only accept the strings "Bullet", " Blitz"  and "Coup rapide".
        """
        BULLET = "Bullet"
        BLITZ = "Blitz"
        RAPIDE = "Coup rapide"

    def __init__(self, name: str, location: str, date: date, rounds_count: int,
                 rounds: list, players: list, time_control: Time_control, description: str):
        self.name = name
        self.location = location
        self.date = date
        self.rounds_count = rounds_count
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description