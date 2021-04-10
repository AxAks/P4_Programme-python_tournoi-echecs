# coding=utf-8
from controllers import list_tournaments_controller, tournament_infos_controller
from views.menus.menu import Menu


class TournamentInfosMenu(Menu):
    """
    This class is the Menu for the management of one selected Tournament.
    It enables to display informations about this tournament or update it.
    """

    def __init__(self, selected_tournament):
        super().__init__(program_name='Chess Tournament Manager', menu_name='Tournaments Menu',
                         data=selected_tournament,
                         root_page=False, previous_page_ctrl=list_tournaments_controller.ListTournamentsCtrl,
                         current_page_ctrl=tournament_infos_controller.TournamentInfosCtrl,
                         exiting_message='Now Leaving Chess Tournament Manager')
        specific_menu_choices = [self.sort_players_by_last_name, self.sort_players_by_result,
                                 self.display_rounds_and_matches,
                                 self.add_round, self.add_match]
        [self.choices.append(choice) for choice in specific_menu_choices]

    def sort_players_by_last_name(self) -> None:  # for one selected tournament
        players_list = self.current_page_ctrl(self.data).sort_players_by_last_name()
        print('========================')
        print(f'Players by last name for "{self.data.name}": ')
        print('========================')
        for player in players_list:
            print(f'- {player.last_name}, {player.first_name}, {player.identifier_pod},\n'
                  f'{player.birthdate_pod}, {player.gender_pod}, {player.ranking}')
        self.current_page_ctrl(self.data).run()

    def sort_players_by_result(self) -> None:  # for one selected tournament
        pass

    def display_rounds_and_matches(self) -> None:  # for one selected tournament
        rounds_list = self.current_page_ctrl(self.data).display_rounds_and_matches()
        print('========================')
        print(f'All Rounds and Matches for "{self.data.name}": ')
        print('========================')
        if len(rounds_list) == 0:
            print('No registered Matches for this Tournament yet')
        else:
            for _round in rounds_list:
                print(f'-> {_round.name}: from {_round.start_time} to {_round.end_time}')
                n = 1
                for match in _round.matches:
                    print(f'Match {n}:\n'
                          f'- {match.player1_id}: {match.player1_score_pod}\n'
                          f'- {match.player2_id}: {match.player2_score_pod}')
                    n += 1
        self.current_page_ctrl(self.data).run()

    def add_round(self) -> None:
        self.current_page_ctrl(self.data).add_round()

        self.current_page_ctrl(self.data).run()

    def add_match(self) -> None:
        self.current_page_ctrl(self.data).add_match()

        self.current_page_ctrl(self.data).run()
