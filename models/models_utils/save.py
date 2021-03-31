# coding=utf-8

def save() -> None:
    """
    This method directs to the controller to save the state of the program at any at any point in the menu.
    """
    print(f'Saving current program state')
    save.save()
    print('Program state saved')


def save():  # à continuer, bien tester et checker si erreurs et si on peut choisir le nom du fichier sauvegardé
    """
    This function saves the program state using tinyDB.
    It serializes the instances of Player et Tournament
    and create a db.json file to store them as dicts
    """
    serialized_player_instances = \
        [sf.factories[Player].registry[key].serialize() for key in sf.factories[Player].registry]
    serialized_tournament_instances = \
        [sf.factories[Tournament].registry[key].serialize() for key in sf.factories[Tournament].registry]
    players_table = db.table('players')
    tournaments_table = db.table('tournaments')
    players_table.truncate()
    tournaments_table.truncate()
    players_table.insert_multiple(serialized_player_instances)
    tournaments_table.insert_multiple(serialized_tournament_instances)