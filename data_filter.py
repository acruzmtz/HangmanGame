from data import DATA

def run():
    # lists comprehensions
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    all_platzi_workers_using_list_c = [worker["name"] for worker in DATA if worker["organization"] == 'Platzi']

    print("Workers that domain python: ", all_python_devs)
    print("All adults +18: ", all_adults)
    print("All Platzi Team", all_platzi_workers_using_list_c)

    # FILTER, MAP
    all_python_devs_using_filter = list(filter(lambda worker: worker["language"] == 'python', DATA))
    all_python_devs_using_filter = list(map(lambda worker: worker["name"], all_python_devs_using_filter))
    print("All Python Developers", all_python_devs_using_filter)

    all_platzi_workers = list(filter(lambda user: user['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda user: user["name"], all_platzi_workers))
    print("All Platzi Team", all_platzi_workers)

    all_adults_using_filter = list(filter(lambda worker: worker["age"] > 18, DATA))
    all_adults_using_filter = list(map(lambda worker: worker["name"], all_adults_using_filter))
    print("All adults in DATA: ", all_adults_using_filter)


    # Challenge: return new dict with extra key called {old: True or False}

    # using list comprehension
    old_people = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA]
    print(old_people)

    # using high orders functions

    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))
    print(old_people)


if __name__ == '__main__':
    run()
