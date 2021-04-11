def search_one_tournament(self) -> Union[dict[Tournament], Tournament]:  #  A revoir réécrire !!
    _input = input('Search a tournament by name, location or dates: ')
    results = sf.factories[Tournament].search(_input)

    while len(results) > 1:
        print(f'{len(results)} Tournaments returned:')
        for identifier in results:
            tournament_obj = results[identifier]
            print(f'{tournament_obj.name}, '  #  les prints sont dans les views !!!
                  f' {tournament_obj.location}, '
                  f' {tournament_obj.start_date}, '
                  f' {tournament_obj.end_date}\n'
                  f'-> {tournament_obj.description}')
        results = sf.factories[Tournament].search(input('Please be more specific: '))
        print('---')
