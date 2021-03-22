# coding=utf-8

"""
File listing all possible inputs
"""
# à scinder surement ensuite !
import re
from datetime import date
from uuid import UUID

from models.player import Player
from models.tournament import Tournament
from constants import ALPHABETICAL_STRING_RULE, RANKING_RANGE, ALPHA_NUMERICAL_STRING_RULE


# Inputs Player
class PlayerInputs:

    def __init__(self):
        pass

    def ask_player_identifier(self) -> str: # pas facile de copier un uuid4 , plutot une recherche !!
        valid_uuid4 = False
        _input = input(f"Enter Player ID")
        while not valid_uuid4:
            try:
                _input = UUID(str(_input), version=4)
                valid_uuid4 = True
            except ValueError:
                print('Invalid player Identifier, please retry...')
        return _input

    def ask_player_last_name(self) -> str:
        """
        This method asks for the player's last name
        and checks the formatting of the string
        """
        _input = input("Enter Player Last Name: ")
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input("Enter Player Last Name: ")  # Verif de formatage String saisie
        return _input

    def ask_player_first_name(self) -> str:
        """
        This method asks for the player's first name
        and checks the formatting of the string
        """
        _input = input("Enter Player First Name: ")
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')
            _input = input("Enter Player First Name: ")  # Verif de formatage String saisie lettres seulement
        return _input

    def ask_player_birthdate(self) -> date:
        """
        This method asks for the player's birthdate,
        checks the format of the string entered
        and forces it into a date format
        """
        valid_date = False
        _input = input("Enter Player Birthdate(YYYY-MM-DD): ")
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:  # Verif de formatage String saisie format date iso , + chiffres et pas des lettres
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input("Enter Player Birthdate(YYYY-MM-DD): ")
        return _input


    def ask_player_gender(self) -> str:
        """
        This method asks for the player's gender using digits
        and returns a formatted string
        """
        # valid_gender = False  # Verif tordue mais ca marche !!
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

    def ask_player_ranking(self) -> int:
        """
        This method asks for the player's ranking
        """
        valid_ranking = False
        while valid_ranking is False:
            try:
                _input = int(input("Enter Player Ranking: "))  #  Verif que string est integer btw 100 et 3000. pb quand lettre.
                if _input in RANKING_RANGE:
                    valid_ranking = True
                else:
                    print('Ranking must be a digit between 100 and 3000, please retry...')
            except ValueError:
                print('Ranking must be a digit between 100 and 3000, please retry...')
        return _input


# Inputs Tournament
class TournamentInputs:
    def __init__(self):
        pass


    def ask_tournament_name(self) -> str:
        """
        This method asks for the tournament's name
        """
        _input = input("Enter Tournament name: ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        while not re.match(ALPHA_NUMERICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')  # Verif de formatage String saisie
            _input = input("Enter Player Last Name: ")
        return _input

    def ask_tournament_location(self) -> str:
        """
        This method asks for the tournament's location
        """
        _input = input("Enter Tournament Location: ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        while not re.match(ALPHABETICAL_STRING_RULE, _input):
            print('Unauthorized characters found, please retry...')  # Verif de formatage String saisie
            _input = input("Enter Player Last Name: ")
        return _input


    def ask_tournament_start_date(self) -> str:
        """
        This method asks for the tournament's start date
        """
        valid_date = False
        _input = input("Enter Tournament's start date (YYYY-MM-DD): ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input("Enter Tournament's start date (YYYY-MM-DD): ")
        return _input

    def ask_tournament_end_date(self) -> str:
        """
        This method asks for the tournament's end date
        """
        valid_date = False
        _input = input("Enter Tournament's end date (YYYY-MM-DD): ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        while not valid_date:
            try:
                _input = date.fromisoformat(_input)
                valid_date = True
            except ValueError:
                print('Not in format YYYY-MM-DD, please retry...')
                _input = input("Enter Tournament's end date (YYYY-MM-DD): ")
        return _input


    def ask_tournament_players_identifier(self) -> str:  #  ce serait sympa de pouvoir faire une recherche dans la base des joueurs !
        # si on a des string vide ca pete derriere à l'instanciation des Players ...
        """
        This method asks for the list of 8 players for the tournament
        """
        #  mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon ( mais faire une recherche car impossible de taper un uuid4...)
        tournament_players_identifier = []
        n = 1
        while n < 9:
            valid_uuid4 = False
            _input = input(f"Enter Player ID {n}/8:") # mettre en place une recherche dans le registre plutot ! + ajouter une verif : que l'uuid n'est pas djà entré dans la liste!
            while not valid_uuid4:
                try:
                    _input = UUID(str(_input), version=4)
                    valid_uuid4 = True
                except ValueError:
                    print('Invalid player Identifier, please retry...')
                    _input = input(f"Enter Player ID {n}/8:")
            if _input not in tournament_players_identifier:
                tournament_players_identifier.append(_input)
            else:
                print('Player Identifier already entered, please retry...')
            n += 1
        return tournament_players_identifier

    def ask_tournament_time_control(self) -> str:
        """
        This method asks for the time control format of the tournament using digits
        and returns a formatted string
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
        return _input

    def ask_tournament_description(self) -> str:
        """
        This method asks for a description of the tournament
        """
        _input = input("Enter Tournament Description: ")
        while _input == '':
            print('Description cannot be empty, please retry...')
            _input = input("Enter Tournament Description: ")  # Verif que l'input n'est pas vide
        return _input


    # defs à reprendre et reutiliser autre part !!!!!

    # Round: pour entrer les resultats d'un round
    # 'name', 'matches', 'end_time', 'start_time'

    def ask_round_name(self): # si le format est round+n, on peut incrementer au fur et à mesure
        """
        This method asks for the round's name at the beginning of the round
        """
        return input("Enter Round Name: ")

    def ask_round_matches(self): # peut s'ajouter automatiquement lorsque les résultats des matches sont enregistrés
        """"
        This method asks for the list of match results for a round
        """
        pass

    def ask_round_end_time(self):  # doit etre renseigné automatiquement en fait !
        pass

    def ask_round_start_time(self):  # doit etre renseigné automatiquement en fait !
        pass


    # Match: pour entrer les resultats d'un match
    # 'player1_id', 'player2_id', 'player1_score', 'player2_score'

    def ask_match_player1_id(self):  # en fait on le recupere de generate_matchups()
        """
        This method asks for player1's ID at the begining of a match/round
        """
        return input("Select Player1: ")

    def ask_match_player2_id(self):  # en fait on le recupere de generate_matchups()
        """
        This method asks for player2's ID at the begining of a match/round
        """
        return input("Select Player2: ")

    def ask_match_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        return input("Enter Player1 Score: ")

    def ask_match_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        return input("Enter Player2 Score: ")

    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass


TournamentInputs().ask_tournament_players_identifier()


