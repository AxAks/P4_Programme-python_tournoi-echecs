# coding=utf-8

"""
Form file for the creation of a new player in the database.
"""
from views.forms.form import Form


class NewPlayerForm(Form):
    """
    This class asks the required data for the creation of a player instance.
    and returns a dict.
    """
    def __init__(self):
        pass

    def add_new_player(self) -> dict:  # mettre des verifs champs par champs!
        last_name = self.ask_player_last_name()
        first_name = self.ask_player_first_name()
        birthdate = self.ask_player_birthdate()
        gender = self.ask_player_gender()
        ranking = self.ask_player_ranking()
        new_player_dict = {
            'last_name': last_name,
            'first_name': first_name,
            'birthdate': birthdate,
            'gender': gender,
            'ranking': ranking
        }
        return new_player_dict
        """
        print(f'\nNew Player Information\n', new_player_dict)
        player_factory = Factory(Player)
        new_player = player_factory.create(**new_player_dict)
        print(player_factory.registry)
        print(new_player.__dict__)
        return new_player
        """

    def ask_player_last_name(self) -> str:
        """
        This method asks for the player's last name
        """
        return input("Enter Player Last Name: ")

    def ask_player_first_name(self) -> str:
        """
        This method asks for the player's first name
        """
        return input("Enter Player First Name: ")

    def ask_player_birthdate(self) -> str:
        """
        This method asks for the player's birthdate
        """
        return input("Enter Player Birthdate(YYYY-MM-DD): ")

    def ask_player_gender(self) -> str:
        """
        This method asks for the player's gender
        """
        return input("Enter Player Gender: ")

    def ask_player_ranking(self) -> str:
        """
        This method asks for the player's ranking
        """
        return int(input("Enter Player Ranking: "))