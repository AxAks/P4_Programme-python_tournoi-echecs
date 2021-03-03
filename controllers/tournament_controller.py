# coding=utf-8

from models.tournament import Tournament

"""
Controller file for Tournament
"""

# unicité
# pour tournoi
# propriete getter qui return : name, location, date_pod
# pour ne pas instancier deux foisplayer_controller.py


def get_name_location_date(tournament):
    """
    The unicity of a tournament is based upon the following three criteria : name, location and date
    This function returns a Tournament object's name, location and date
    in order to identify the Tournament.
    """
    return Tournament.tournament_name, Tournament.location, Tournament.dates_pod()