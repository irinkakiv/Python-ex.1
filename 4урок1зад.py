
from sys import argv
def sal():

    try:
        time, salary, bonus = map(float,argv[1:])
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        print('Not a number')
sal()