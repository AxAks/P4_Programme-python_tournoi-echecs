# coding=utf-8

import re
from datetime import date
from uuid import UUID

from constants import ALPHABETICAL_STRING_RULE, RANKING_RANGE, ALPHA_NUMERICAL_STRING_RULE

from models.superfactory import super_factory as sf
from models.player import Player
from models.tournament import Tournament


class GenericInputs:
    """
    Class for all inputs
    """
    def __init__(self):
        pass

    def ask_properties(self, *args):  # fonctionne un peu mais pas fini : comment est ce que je lui passe les args   # appelé par Form.add_new, doit etre generique et renvoyer vers une fonction particuliere selon l'objet
        for arg in args:
            method_name = f'ask_{arg}'
            my_cls = GenericInputs() # voir comment rendre la classe variable ou générique Player, Tournament, (Round et Match)
            try:
                method = getattr(my_cls, method_name)
                print(f'{arg.replace("_", " ").title()} is  : "{method}"') # un vieux print illisible pour identifier list de tournament ...
            except Exception as e:
                raise Exception(e)
        return method #f'ask{arg}()' #pb si deux objets ont des attributs identiques -> surement qu'ils font la meme chose, à voir

    @property
    def ask_last_name(self) -> str:
        """
        This method asks for the player's last name
        and checks the formatting of the string
        """
        input_info = "Enter Last Name: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    @property
    def ask_first_name(self) -> str:
        """
        This method asks for the player's first name
        and checks the formatting of the string
        """
        input_info = "Enter First Name: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    @property
    def ask_birthdate(self) -> date:
        """
        This method asks for the player's birthdate,
        checks the format of the string entered
        and forces it into a date format
        """
        valid_date = False
        input_info = "Enter Player Birthdate(YYYY-MM-DD): "
        _input = input(input_info)
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input(input_info)
        return _input

    @property
    def ask_gender(self) -> str:
        """
        This method asks for the player's gender using digits
        and returns a formatted string
        """
        valid_gender = False
        choices_info = '(1: MALE, 2: FEMALE)'
        input_info = f'Enter Player Gender {choices_info}: '
        wrong_input = 'Invalid choice (1 or 2), please retry...'

        _input = input(input_info)
        while not valid_gender:
            try:
                _input = int(_input)
                if _input in (1, 2):
                    if _input == 1:
                        _input = 'MALE'
                    else:
                        _input = 'FEMALE'
                    valid_gender = True
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
        return _input

    @property
    def ask_ranking(self) -> int:
        """
        This method asks a ranking between 100 and 3000
        """
        valid_ranking = False
        input_info = "Enter Player Ranking: "
        wrong_input = 'Ranking must be a digit between 100 and 3000, please retry...'
        while valid_ranking is False:
            try:
                _input = int(input(input_info))
                if _input in RANKING_RANGE:
                    valid_ranking = True
                else:
                    print(wrong_input)
            except ValueError:
                print(wrong_input)
        return _input

    @property
    def ask_name(self) -> str:
        """
        This method asks for a name
        """
        input_info = "Enter name: "
        _input = input(input_info)
        while not re.match(ALPHA_NUMERICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    @property
    def ask_location(self) -> str:
        """
        This method asks for a location
        """
        input_info = "Enter Location: "
        _input = input(input_info)
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input(input_info)
        return _input

    @property
    def ask_start_date(self) -> date:
        """
        This method asks for a start date
        """
        valid_date = False
        input_info = "Enter start date (YYYY-MM-DD): "
        _input = input(input_info)
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input(input_info)
        return _input

    @property
    def ask_end_date(self) -> date:
        """
        This method asks for an end date
        """
        valid_date = False
        input_info = "Enter end date (YYYY-MM-DD): "
        _input = input(input_info)
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input(input_info)
        return _input


    @property
    def ask_identifiers_list(self) -> list: # pas generique actuellement...!
        # liste d'UUID de Players et le nombre est fixé à 8 joueurs : mal nommée non explicite
        """
        This method asks for a list of 8 players for a tournament
        """
        tournament_players_identifier = {}
        n = 1
        print("Please, select players to add")
        while n < 9:
            player_dict = search_one_player()
            if len(player_dict) == 0:
               player_dict = search_one_player() # utile ? à testé !! (pb prints entre les deux fonctions)
            for key in player_dict:
                if key not in tournament_players_identifier:
                    tournament_players_identifier[key] = player_dict[key]
                    print(f"Player {n}/8 added")
                    print(f"{player_dict[key].last_name_pod}, "
                          f"{player_dict[key].first_name_pod}: "
                          f"{player_dict[key].identifier_pod}")
                    n += 1
                else:
                    print('Player already entered in the list, please retry...')
        return tournament_players_identifier


    @property
    def ask_time_control(self) -> str:
        """
        This method asks for the time control format of a tournament using digits for choice
        and returns the matching formatted string
        """
        valid_time_control = False
        choices_info = '(1: BULLET, 2: BLITZ, 3: RAPIDE)'
        input_info = f'Enter Time Control Format {choices_info}: '
        wrong_input = 'Invalid choice (1, 2 or 3), please retry...'
        _input = input(input_info)
        while not valid_time_control:
            try:
                _input = int(_input)
                if _input in (1, 2, 3):
                    if _input == 1:
                        _input = 'BULLET'
                    elif _input == 2:
                        _input == 'BLITZ'
                    else:
                        _input = 'RAPIDE'
                    valid_time_control = True
                else:
                    print(wrong_input)
                    _input = input(input_info)
            except ValueError:
                print(wrong_input)
                _input = input(input_info)
        return _input # retourne "2" au lieu de BLITZ (l'int au leiu du str)

    @property
    def ask_description(self) -> str:
        """
        This method asks for a description text
        """
        input_info = "Enter Description: "
        _input = input(input_info)
        while _input == '':
            print('Description cannot be empty, please retry...')
            _input = input(input_info)
        return _input

    # -> on pourrait passer tout ca dans PlayerInputs !
    # -> et generate_matchups dans Tournament_controller

    # en fait on le recupere de generate_matchups() + c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    # et également ask_identifier ou search_by_id dans player_inputs
    @property
    def ask_identifier(self):  # _player1
        """
        This method asks for player1's ID at the begining of a match/round
        """
        return input("Select Player1: ")

    #  en fait on le recupere de generate_matchups() + c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    #  et également ask_identifier ou search_by_id dans player_inputs
    @property
    def ask_identifier(self):  # _player2  + # en fait on le recupere de generate_matchups()
        """
        This method asks for player2's ID at the begining of a match/round
        """
        return input("Select Player2: ")

    # c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    @property
    def ask_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        return input("Enter Player1 Score: ")

    # c'est la meme methode deux fois, seul le numero de joueur change (1 ou 2)
    @property
    def ask_match_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        return input("Enter Player2 Score: ")

    #  pas ici, dans un controller !!
    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass

    """
    @property
    def ask_name(self):  # Comme la methode de Tournament !!!!  ancien comm pour round : #  si le format est round+n, on peut incrementer au fur et à mesure
    """
        #This method asks for the round's name at the beginning of the round
    """
        return input("Enter Name: ")
    """
    @property
    def ask_matches(self):  # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés //controller
        """"
        This method asks for the list of match results for a round
        """
        pass

    @property
    def ask_end_time(self):  # doit etre renseigné automatiquement en fait !
        pass

    @property
    def ask_start_time(self):  # doit etre renseigné automatiquement en fait !
        pass


def search_one_player(): # pas générique !
    results = sf.factories[Player].search(input('Search a player by id : '))
    while len(results) > 1:
        for identifier in results:
            print( f'{results[identifier].last_name},'
                    f' {results[identifier].first_name}:'
                    f' {results[identifier].identifier_pod}\n'
                    f'-> {results[identifier].birthdate_pod},'
                    f' {results[identifier].gender_pod.title()},'
                    f' {results[identifier].ranking}\n')
        print(f'{len(results)} Players returned,')

        results = sf.factories[Player].search(input('please be more specific: '))
        for identifier in results:
            print('1 Player found in Registry for this ID:')
            print(f'{results[identifier].last_name},'
                  f' {results[identifier].first_name}:'
                  f' {results[identifier].identifier_pod}\n'
                  f'-> {results[identifier].birthdate_pod},'
                  f' {results[identifier].gender_pod.title()},'
                  f' {results[identifier].ranking}')
    if len(results) == 0:
        print("No Player found in Registry for this ID")
        return results
    else:
        return results

def search_one_tournament(): # pas générique !, pas utilisé ! pas testé,
    results = sf.factories[Tournament].search(input('Search a Tournament by name, location or dates: '))
    while len(results) > 1:
        for identifier in results:
            print( f'{results[identifier].name},'
                    f' {results[identifier].location}:'
                    f' {results[identifier].start_date_pod}'
                    f' {results[identifier].end_date_pod}\n'
                    f'-> {results[identifier].description}')
        print(f'{len(results)} Players returned')

        results = sf.factories[Player].search(input('please be more specific: '))
        for identifier in results:
            print('1 Tournament found in Registry for this research:')
            print( f'{results[identifier].name},'
                    f' {results[identifier].location}:'
                    f' {results[identifier].start_date_pod}'
                    f' {results[identifier].end_date_pod}\n'
                    f'-> {results[identifier].description}')
    if len(results) == 0:
        print("No Tournament found in Registry for this research")
        return results
    else:
        return results
