import sys
from pprint import pprint

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}

capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}


def get_capital(state):
    if state in states.keys():
        state = [value for key, value in states.items() if key == state]
        print(*[value for key, value in capital_cities.items() if key == state[0]])
    else:
        print('Unknown state')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_capital(sys.argv[1])
    else:
        pass