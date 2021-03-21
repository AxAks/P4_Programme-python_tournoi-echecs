# coding=utf-8

"""
File listing all possible inputs
"""
# à scinder surement ensuite !


# Inputs Player
from models.tournament import Tournament


class PlayerInputs:

    def __init__(self):
        pass

    def ask_player_last_name(self) -> str:
        """
        This method asks for the player's last name
        """
        _input = input(
            "Enter Player Last Name: ")  #  mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input


    def ask_player_first_name(self) -> str:
        """
        This method asks for the player's first name
        """
        _input = input(
            "Enter Player First Name: ")  #  mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input


    def ask_player_birthdate(self) -> str:
        """
        This method asks for the player's birthdate
        """
        _input = input(
            "Enter Player Birthdate(YYYY-MM-DD): ")  #  mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input


    def ask_player_gender(self) -> str:
        """
        This method asks for the player's gender
        """
        _input = input(
            "Enter Player Gender: ")  #  mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input


    def ask_player_ranking(self) -> str:
        """
        This method asks for the player's ranking
        """
        _input = int(input(
            "Enter Player Ranking: "))  #  mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
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
        return _input

    def ask_tournament_location(self) -> str:
        """
        This method asks for the tournament's location
        """
        _input = input("Enter Tournament Location: ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input

    def ask_tournament_start_date(self) -> str:
        """
        This method asks for the tournament's start date
        """
        _input = input("Enter Tournament's start date (YYYY-MM-DD): ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input

    def ask_tournament_end_date(self) -> str:
        """
        This method asks for the tournament's end date
        """
        _input = input("Enter Tournament's end date (YYYY-MM-DD): ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        return _input

    def ask_tournament_players_identifier(
            self) -> str:  #  ce serait sympa de pouvoir faire une recherche dans la base des joueurs !
        # si on a des string vide ca pete derriere à l'instanciation des Players ...
        """
        This method asks for the list of 8 players for the tournament
        """
        tournament_players_identifier = []  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
        n = 1
        while n < 9:
            _input = input(f"Enter Player ID {n}/8:")
            tournament_players_identifier.append(_input)
            n += 1
        return tournament_players_identifier

    def ask_tournament_time_control(self) -> str:
        """
        This method asks for the time control format of the tournament
        """
        choices = {}
        for key in Tournament.Time_control:
            choices[key.name] = key.value
        _input = input(f"Enter Time Control Format {choices}: ")  # mettre un choix ici ! 1, 2 ou 3 avec affichage des choix
        return _input

    def ask_tournament_description(self) -> str:
        """
        This method asks for a description of the tournament
        """
        _input = input("Enter Tournament Description: ")  # mettre des verifs  de formatage de l'input ici et demander de resaisir si pas bon
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

