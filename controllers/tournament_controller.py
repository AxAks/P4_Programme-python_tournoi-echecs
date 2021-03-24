# coding=utf-8

"""
Controller file for Tournament
"""


class TournamentFactory:  # est ce que je mets tout ca dans une classe (cf Factory Method)???
    """
    Subclass of Factory to create and manage Tournament instances
    à continuer ...
    """
    """
    tournament_factory = Factory(Tournament)  # copié des tests, à voir si je peux en faire quelque chose
    """

    def create_tournament(self):
        pass

# attention ! l'idée est de pouvoir faire des tournois sur plusieurs jours : date_debut, date_fin et par defaut date_debut = date_fin (1 jour)
# -> à faire dans les inputs je pense.


#  Comment gère t-on la reference à Tournament dans Round ? à voir -> Round n'existe pas hors de Tournament
#-> dans le controller Tournament !? à voir

# Le Round doit etre identifié dans Tournament ( dans la liste de Rounds)
# // Le Match doit etre identifié dans Round ( dans la liste de matchs)


# pour ajouter un round ou des rounds à Tournament
def add_round(self, round_info):  # voir si utile à un moment
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