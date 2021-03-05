# coding=utf-8

"""
This file contains sample dict values for testing purposes
"""

#  player dicts
player1_dict = {
    'identifier': '3be40089-64ff-48c2-8e6e-bc005ad378d2',
    'last_name': 'aKONdé',
    'first_name': 'Axel',
    'birthdate': '1986-05-02',
    'gender': 'MALE',
    'ranking': 2500
}
player2_dict = {
    'identifier': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
    'last_name': 'Berd',
    'first_name': 'Bernard',
    'birthdate': '1983-03-01',
    'gender': 'MALE',
    'ranking': 2400
}

player3_dict = {
    'identifier': '4f4e8869-fbd2-48d7-b759-fafd725df22f',
    'last_name': 'CERAS',
    'first_name': 'Cédric',
    'birthdate': '1978-04-26',
    'gender': 'MALE',
    'ranking': 1400
}

player4_dict = {
    'identifier': '1bcb740a-3ca1-49e8-889f-30ca3c1bc293',
    'last_name': 'Deflar',
    'first_name': 'Didier',
    'birthdate': '1991-12-21',
    'gender': 'MALE',
    'ranking': 1300
}

player5_dict = {
    'identifier': 'f1d63919-1d15-4784-a724-5554dccdb076',
    'last_name': 'Edourd',
    'first_name': 'Emilie',
    'birthdate': '1922-05-01',
    'gender': 'FEMALE',
    'ranking': 1290
}

player6_dict = {
    'identifier': '6246d2f8-dab2-452e-b994-2c3e8aaedcef',
    'last_name': 'Ferrat',
    'first_name': 'Fanny',
    'birthdate': '1985-09-12',
    'gender': 'FEMALE',
    'ranking': 120
}

player7_dict = {
    'identifier': '6cd402fb-9e79-4e23-a326-5b7e215de205',
    'last_name': 'GRAND',
    'first_name': 'Gérard',
    'birthdate': '1982-03-01',
    'gender': 'MALE',
    'ranking': 1300
}

player8_dict = {
    'identifier': '96b0887a-58f0-4aa6-a68f-9b845a7c9ec1',
    'last_name': 'Harry',
    'first_name': 'Henriette',
    'birthdate': '1972-11-21',
    'gender': 'FEMALE',
    'ranking': 150
}

player9_dict = {
    'identifier': '23ed1860-bd10-42e1-b7b7-9b4c114a5d5c',
    'last_name': 'Isidore',
    'first_name': 'Isabelle',
    'birthdate': '1984-03-01',
    'gender': 'FEMALE',
    'ranking': 200
}

player10_dict = {
    'identifier': '11438f73-64b8-491b-8290-17548a794f58',
    'last_name': 'Junot',
    'first_name': 'Juliette',
    'birthdate': '1982-03-01',
    'gender': 'FEMALE',
    'ranking': 500
}

#  Tournament dicts
tournament24_dict = {
    'name': 'Best Tournament Ever',
    'location': 'Geneve',
    'dates': '1987-02-28',
    'players_identifier': [
        '3be40089-64ff-48c2-8e6e-bc005ad378d2',
        'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
        '4f4e8869-fbd2-48d7-b759-fafd725df22f',
        '1bcb740a-3ca1-49e8-889f-30ca3c1bc293'],
    'time_control': 'BULLET',
    'description': 'a very nice tournament with four outstanding players',
    'rounds_list': [],
    'rounds': 3
}

tournament35_dict = {
    'name': 'Best Tournament Ever',
    'location': 'Genève',
    'dates': '1987-02-28',
    'players_identifier': [
        '3be40089-64ff-48c2-8e6e-bc005ad378d2',
        'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
        '4f4e8869-fbd2-48d7-b759-fafd725df22f',
        '1bcb740a-3ca1-49e8-889f-30ca3c1bc293'],
    'time_control': 'BULLET',
    'description': 'a very nice tournament with four outstanding players',
    'rounds_list': [
        {'name': 'Round 1',
         'matches': [
             {'player1_id': '3be40089-64ff-48c2-8e6e-bc005ad378d2',
              'player2_id': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
              'player1_score': 1.0, 'player2_score': 0.0},
             {'player1_id': '4f4e8869-fbd2-48d7-b759-fafd725df22f',
              'player2_id': '1bcb740a-3ca1-49e8-889f-30ca3c1bc293',
              'player1_score': 0.5, 'player2_score': 0.5}
         ],
         'end_time': '2021-02-26T11:34:07',
         'start_time': '2021-02-26T11:33:07'
         },
        {
            'name': 'Round 2',
            'matches': [
                {'player1_id': 'f1d63919-1d15-4784-a724-5554dccdb076',
                 'player2_id': '6246d2f8-dab2-452e-b994-2c3e8aaedcef',
                 'player1_score': 0.0, 'player2_score': 1.0},
                {'player1_id': '6cd402fb-9e79-4e23-a326-5b7e215de205',
                 'player2_id': '96b0887a-58f0-4aa6-a68f-9b845a7c9ec1',
                 'player1_score': 1.0, 'player2_score': 0.0}
            ],
            'end_time': '2021-02-26T11:34:07',
            'start_time': '2021-02-26T11:33:07'
        }],
    'rounds': 3
}

# Round dicts
round1_dict = {
    'name': 'Round 1',
    'matches': [
        {'player1_id': '3be40089-64ff-48c2-8e6e-bc005ad378d2', 'player2_id': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
         'player1_score': 1.0, 'player2_score': 0.0},
        {'player1_id': '4f4e8869-fbd2-48d7-b759-fafd725df22f', 'player2_id': '1bcb740a-3ca1-49e8-889f-30ca3c1bc293',
         'player1_score': 0.5, 'player2_score': 0.5}
    ],
    'end_time': '2021-02-26T11:34:07',
    # doit etre enregistrée automatiquement quand l'utilisateur marque le tournoi comme terminé
    'start_time': '2021-02-26T11:33:07'  # doit etre enregistrée automatiquement quand l'utilisateur créé le tournoi
}

round2_dict = {
    'name': 'Round 2',
    'matches': [
        {'player1_id': 'f1d63919-1d15-4784-a724-5554dccdb076', 'player2_id': '6246d2f8-dab2-452e-b994-2c3e8aaedcef',
         'player1_score': 0.0, 'player2_score': 1.0},
        {'player1_id': '6cd402fb-9e79-4e23-a326-5b7e215de205', 'player2_id': '96b0887a-58f0-4aa6-a68f-9b845a7c9ec1',
         'player1_score': 1.0, 'player2_score': 0.0}
    ],
    'end_time': '2021-02-26T11:34:07',
    # doit etre enregistrée automatiquement quand l'utilisateur marque le tournoi comme terminé
    'start_time': '2021-02-26T11:33:07'  # doit etre enregistrée automatiquement quand l'utilisateur créé le tournoi
}

# ex : tuple
round91_dict = {
    'name': 'Round 1',
    'matches': [
        (
            ['3be40089-64ff-48c2-8e6e-bc005ad378d2', 1.0],
            ['ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b', 0.0]
        ),
        (
            ['4f4e8869-fbd2-48d7-b759-fafd725df22f', 0.5],
            ['1bcb740a-3ca1-49e8-889f-30ca3c1bc293', 0.5]
        )
    ],
    'start_time': '2021-02-26T11:33:07',
    'end_time': '2021-02-26T11:34:07'
}

#  Match dicts
match28_dict = {
    'player1': {'identifier': '3be40089-64ff-48c2-8e6e-bc005ad378d2', 'last_name': 'Akondé', 'first_name': 'Axel',
                'birthdate': '1986-05-02', 'gender': 'MALE', 'ranking': 2500},
    'player2': {'identifier': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b', 'last_name': 'Berd', 'first_name': 'Bernard',
                'birthdate': '1982-03-01', 'gender': 'MALE', 'ranking': 2400},
    'player1_score': 1.0,
    'player2_score': 0.0
}

match16_dict = {
    'player1_id': '3be40089-64ff-48c2-8e6e-bc005ad378d2',
    'player2_id': 'ce0258eb-cfeb-45e6-a56d-8f5d7260bd9b',
    'player1_score': 1.0,
    'player2_score': 0.0
}
