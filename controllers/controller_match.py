# coding=utf-8


from models.match import Match


"""
Controller file for Match
"""

# on en aura peut etre pas besoin car match est géré dans Round
# unicité
# pour tournoi
# propriete getter qui return : name, location, date_pod (lecture seule) dans la Classe Tournament
# pour ne pas instancier deux foisplayer_controller.py


class MatchCreator:
    """
    Subclass of Creator to create and manage Round instances
    à continuer ...
    """
    def create_match(self, match_dict): # à voir !
        """
        This method receives dicts from the abstract Creator for Match instances to be created
        and hold a registry of the created Rounds.
        à continuer ...
        """
        new_match = Match(**match_dict)
        Match.registry[new_match.identifier] = new_match
        print('New Match created and stored!')
        return new_match
