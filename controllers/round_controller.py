# coding=utf-8

from models.round import Round


"""
Controller file for Round
"""

# on en aura peut etre pas besoin car Round est géré dans Tournament
# unicité
# pour tournoi
# propriete getter qui return : name, location, date_pod (lecture seule) dans la Classe Tournament
# pour ne pas instancier deux foisplayer_controller.py


class RoundCreator:
    """
    Subclass of Creator to create and manage Round instances
    à continuer ...
    """
    def create(self, round_dict):  # à voir !
        """
        This method receives dicts from the abstract Creator for Rounds instances to be created
        and hold a registry of the created Rounds.
        à continuer ...
        """
        new_round = Round(**round_dict)
        Round.registry[new_round.identifier] = new_round
        print('New Round created and stored!')
        return new_round
