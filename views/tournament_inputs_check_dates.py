# coding=utf-8


def check_one_day_tournament():  # est ce que je le garde ? à voir plutot dans controller
    """
    This method automatically sets the end date of a tournament to the already entered start date
    if the user indicates that it is a one-day tournament.
    The input of the end date is made easier : Yes or No
    """
    # start_date = ask_tournament_start_date()
    valid_choice = False
    choices_info = '(1: YES, 2: NO)'
    input_info = f'Is it a one-day Tournament ? {choices_info}: '
    wrong_input = 'Invalid choice (1 or 2), please retry...'
    _input = input(input_info)
    while not valid_choice:
        try:
            _input = int(_input)
            if _input in (1, 2):
                #if _input == 1:
                #    _input = start_date  # pas sûr de moi ! je veux que _input aie la valeur de start_date mais là je redemande la date de debut
                #else:
                    # ask_tournament_end_date()  # pas sûr de moi ! la ca doit etre bon ! ca renvoie vers ask_tournament_end_date
                    valid_choice = True  # bizarre !
            else:
                print(wrong_input)
                _input = input(input_info)
        except ValueError:
            print(wrong_input)
            _input = input(input_info)
        # return start_date, _input
