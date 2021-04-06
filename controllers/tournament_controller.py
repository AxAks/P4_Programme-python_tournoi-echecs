# coding=utf-8

"""
Controller file for Tournament
"""

from models.tournament import Tournament
from models.models_utils.superfactory import super_factory as sf
from views.menus.tournament_menu import TournamentMenu


def run():
    """
    This method displays the menu and responds to choices made.
    """
    valid_choices = range(len(TournamentMenu().choices))
    choice = -1
    while choice not in valid_choices:
        TournamentMenu().show()
        _input = input('Enter an option: ')
        try:
            choice = int(_input)
            if choice not in valid_choices:
                print(f'-> "{choice}" is not a valid choice <-')
        except ValueError:
            print(f'-> "{_input}" is not a valid choice <-')

    action = TournamentMenu().choices[choice]
    action()

def sort_by_name():
    """
    This function lists the tournament instances alphabetically sorted by name
    """
    tournaments_list = []
    for identifier in sf.factories[Tournament].registry:
        tournament_obj = sf.factories[Tournament].registry[identifier]
        tournaments_list.append(tournament_obj)
    sorted_by_name = sorted(tournaments_list, key=lambda x: x.name)
    return sorted_by_name


def sort_by_location():
    """
    This function lists the tournament instances alphabetically sorted by location
    """
    tournaments_list = []
    for identifier in sf.factories[Tournament].registry:
        tournament_obj = sf.factories[Tournament].registry[identifier]
        tournaments_list.append(tournament_obj)
    sorted_by_location = sorted(tournaments_list, key=lambda x: x.location)
    return sorted_by_location


def sort_by_start_date():
    """
    This function lists the tournament instances sorted by reverse chronological start date
    """
    tournaments_list = []
    for identifier in sf.factories[Tournament].registry:
        tournament_obj = sf.factories[Tournament].registry[identifier]
        tournaments_list.append(tournament_obj)
    sorted_by_start_date = sorted(tournaments_list, key=lambda x: x.start_date, reverse=True)
    return sorted_by_start_date


def search_by_id(search):
    """
    This function lists the tournament instances matching the given input
    (identifier: Name, Location, Start date, End date)
    """
    results = sf.factories[Tournament].search(search)
    found_tournaments_list = []
    for identifier in results:
        tournament_obj = sf.factories[Tournament].registry[identifier]
        found_tournaments_list.append(tournament_obj)
    return found_tournaments_list


def display_tournament_players():
    """
    This function lists all the players of a given tournament
    """
    #  à faire
    pass


def display_tournament_rounds():
    """
    This function lists all the rounds of a given tournament
    """
    #  à faire
    pass


def display_tournament_matches():
    """
    This function lists all the matches of a given tournament
    """
    #  à faire
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