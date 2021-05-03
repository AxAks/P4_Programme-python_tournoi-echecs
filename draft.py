# tournament_info_controller

"""
sans tentative de verif de tounament already played matches
round_couples = [[upper_ranking_players_list[i], lower_ranking_players_list[i]]
                 for i in range(0, len(upper_ranking_players_list))]
"""

"""
 if lower_ranking_players_list[i].identifier_pod
    in self.data.not_played_yet[upper_ranking_players_list[i].identifier_pod]
 else [upper_ranking_players_list[i], upper_ranking_players_list[i+2]]
 #  pas fiable du tout !! ...
 for i in range(0, len(upper_ranking_players_list))]
"""

"""
if len(upper_ranking_players_list) == len(lower_ranking_players_list):            
    for identifier in self.data.not_played_yet:
        if len(self.data.not_played_yet[identifier]) == len(self.data.identifiers_list) - 1: # je veux verifier qu'il n'y a pas eu de match encore
            round_couples = [[upper_ranking_players_list[i], lower_ranking_players_list[i]]  # pb le resultat est bon mais ca boucle pour rien!! 
                             for i in range(0, len(upper_ranking_players_list))]
        else:
            round_couples = [[upper_ranking_players_list[i], lower_ranking_players_list[i]]
                             if lower_ranking_players_list[i].identifier_pod
                                not in self.data.already_played[upper_ranking_players_list[i].identifier_pod]
                             else [upper_ranking_players_list[i], lower_ranking_players_list[i]]  # pas fiable du tout !! ...
                             for i in range(0, len(upper_ranking_players_list))]
    return round_couples
else:
    return 'These lists do not have the same number of items'
"""

