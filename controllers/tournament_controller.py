# coding=utf-8

from models.tournament import Tournament


"""
Controller file for Tournament
"""

# unicité
# pour tournoi
# propriete getter qui return : name, location, date_pod (lecture seule) dans la Classe Tournament
# pour ne pas instancier deux foisplayer_controller.py


class TournamentCreator:  # est ce que je mets tout ca dans une classe (cf Factory Method)???
    """
    Subclass of Creator to create and manage Tournament instances
    à continuer ...
    """

    # doit etre au courant de la création des instances de Player
    # tenir un registre des differents players créés





# Tournament
# players_identifier [UUID, UUID]


#  Comment gère t-on la reference à Tournament dans Round ? à voir -> Round n'existe pas hors de Tournament
#-> dans le controller Tournament !? à voir

# Le Round doit etre identifié dans Tournament ( dans la liste de Rounds)
# // Le Match doit etre identifié dans Round ( dans la liste de matchs)


# pour ajouter un round ou des rounds à Tournament
def add_round(self, round_info): # voir si utile à un moment
    """
    This method enables to add the list of Matches of a Round to the Tournament Object
    """
    pass

# pour ajouter un match à Round
def add_match(self, match):  # est ce qu'une méthode est utile ici ? plutot dans controller Tournament je pense
    """
    This getter enables to add the information of a Match to the list of matches of the Round Object
    """
    pass