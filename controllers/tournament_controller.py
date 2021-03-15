# coding=utf-8
"""
Controller file for Tournament
"""

from models.tournament import Tournament
from controllers.controller import Creator

# unicité
# pour tournoi
# propriete getter qui return : name, location, date_pod (lecture seule) dans la Classe Tournament
# pour ne pas instancier deux foisplayer_controller.py


# class TournamentCreator(Creator):  # est ce que je mets tout ca dans une classe (cf Factory Method)???
"""
Subclass of Creator to create and manage Tournament instances
à continuer ...
"""

# doit etre au courant de la création des instances de Player
# tenir un registre des differents players créés


def create(tournament_dict):  #  à voir !
    """
    This method receives dicts from the abstract Creator for Tournament instances to be created
    and hold a registry of the created Tournaments.
    à continuer ...
    """
    # return new Tournament instance
    new_tournament = Tournament(**tournament_dict)
    Creator.tournament_registry[
        new_tournament.identifier] = new_tournament  # registry = {} : key = Tournamment.identifier, value = instance
    print('New Tournament Created and stored !')
    return new_tournament


# on donne les infos d'un tournoi , il doit renvoyer le Tournament
def get_tournament(search):
    """
    This method enables to get a Tournament instance from its identifier attributes : Name, Location or Dates.
    """
    registry = Creator.tournament_registry  # string de 4 attributs, la recherche doit etre améliorée !
    results = []
    for key in registry:
        for search_match in re.finditer(search, key):
            results.append(registry[key])
    return results

# attention ! l'idée est de pouvoir faire des tournois sur plusieurs jours : date_debut, date_fin et par defaut date_debut = date_fin (1 jour)
# -> à faire dans les inputs input je pense.

# Tournament
# players_identifier [UUID, UUID]


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