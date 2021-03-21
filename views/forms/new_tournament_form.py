# coding=utf-8

"""
Form file for the creation of a new tournament in the database.
"""

from views.forms.form import Form


class NewTournamentForm(Form):  # faire heriter de Menu aussi ? (fonction de navigation : back, etc)
    """
    This class asks the required data for the creation of a Tournament instance
    and returns a dict.
    """
    def __init__(self):
        pass

        #  Tournament : Pour la création des tournois
        #  'name', 'location', 'start_date', 'end_date', 'players_identifier',
        # 'time_control', 'description', 'rounds_list', 'rounds'

    def add_new_tournament(self) -> dict:  # mettre des verifs champs par champs!
        """
        This method asks all the required info about a specific tournament.
        It returns the info as a dict
        """
        name = self.ask_tournament_name()
        location = self.ask_tournament_location()
        start_date = self.ask_tournament_start_date()
        end_date = self.ask_tournament_end_date()  #  demander si le tournoi est sur un jour si oui attribuer la meme date que start_date
        players_identifier = self.ask_tournament_players()
        time_control = self.ask_tournament_time_control()
        description = self.ask_tournament_description()
        new_tournament_dict = {
            'name': name,
            'location': location,
            'start_date': start_date,
            'end_date': end_date,
            'players_identifier': players_identifier,
            'time_control': time_control,
            'description': description
        }
        return new_tournament_dict
        """
        print(f'\nTournament Information\n', new_tournament_dict)
        tournament_factory = Factory(Tournament)
        new_tournament = tournament_factory.create(**new_tournament_dict)
        print(tournament_factory.registry)
        print(new_tournament.__dict__)
        return new_tournament
        """

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
        _input = input("Enter Time Control Format: ")  # mettre un choix ici ! 1, 2 ou 3 avec affichage des choix
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

