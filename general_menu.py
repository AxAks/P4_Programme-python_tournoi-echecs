# coding=utf-8

"""
Class for a generic Menu
"""

import sys

class GeneralMenu:
    """
    This class manages a general menu to navigate through the program.
    """
    def __init__(self):
        self.choices = {
            '1': self.create_tournament,
            '2': self.manage_players,
            '3': self.load_tournament,
            '4': self.save_tournament,
            # '...': self.action('...'),
            '0': self.quit
        }

    def general_menu(self):
        """
        This method displays the different options of the menu.
        """
        print('Chess Tournament Manager - Menu\n'
              '\n1. Create a New Tournament\n'
              '2. Player Database Management\n'
              '3. Load Tournament\n'
              '4. Save Tournament\n'
              '\n0. Quit')

    def run(self):
        """
        This method displays the menu and responds to choices made.
        """
        while True:
            self.general_menu()
            choice = input('\nEnter an option: ')
            action = self.choices.get(choice) # prend l'input et fait le lien avec le dict self.choices pour renvoyer vers la def()
            if action:
                action()
            else:
                print(f'"{choice}" is not a valid choice')

    def create_tournament(self):
        """
        This method enables to create a tournament.
        """
        pass

    def manage_players(self): # trop large , devra etre decoupé je pense
        pass

    def load_tournament(self):
        """
        This method enables to load a previously saved tournament
        """
        pass

    def save_tournament(self):
        """
        This method enables to save the state of a tournament
        """
        pass



    # General Prints :


    # General Inputs :

    # Tournament : Pour la création des tournois
    # 'name', 'location', 'start_date', 'end_date', 'players_identifier',
    # 'time_control', 'description', 'rounds_list', 'rounds'
    def ask_tournament_name(self):
        """
        This method asks for the tournament's name
        """
        pass

    def ask_tournament_location(self):
        """
        This method asks for the tournament's location
        """
        pass

    def ask_tournament_player(self):
        """
        This method asks for the list of 8 players for the tournament
        """
        pass

    def ask_tournament_time_control(self):
        """
        This method asks for the time control format of the tournament
        """
        pass

    def ask_tournament_description(self):
        """
        This method asks for a description of the tournament
        """
        pass

    # Player: Pour la Player Database
    # 'identifier', 'last_name', 'first_name', 'birthdate', 'gender', 'ranking'

    def ask_player_identifier(self):
        """
        This method asks for the player's identifier
        """
        pass
    def ask_player_last_name(self):
        """
        This method asks for the player's last name
        """
        pass

    def ask_player_first_name(self):
        """
        This method asks for the player's first name
        """
        pass

    def ask_player_birthdate(self):
        """
        This method asks for the player's birthdate
        """
        pass

    def ask_player_gender(self):
        """
        This method asks for the player's gender
        """
        pass

    def ask_player_ranking(self):
        """
        This method asks for the player's ranking
        """
        pass

    # Round: pour entrer les resultats d'un round
    # 'name', 'matches', 'end_time', 'start_time'

    def ask_round_name(self): # si le format est round+n, on peut incrementer au fur et à mesure
        """
        This method asks for the round's name at the beginning of the round
        """
        pass

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
        pass

    def ask_match_player2_id(self):  # en fait on le recupere de generate_matchups()
        """
        This method asks for player2's ID at the begining of a match/round
        """
        pass

    def ask_match_player1_score(self):
        """
        This method asks for player1's score at the end of a match/round
        """
        pass

    def ask_match_player2_score(self):
        """
        This method asks for player2's score at the end of a match/round
        """
        pass

    def generate_matchups(self):
        """
        This method randomly generates the tournament match-ups between the Players for the different rounds
        It takes into account the match-ups that have already been played in the previous rounds.
        """
        pass

    def quit(self):
        print('Chess Tournament Manager terminated')
        sys.exit(0)


if __name__ == '__main__':
    GeneralMenu().run()