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


def get_state(capital):
    if capital in capital_cities.values():
        capital = [key for key, value in capital_cities.items() if value == capital]
        print(*[key for key, value in states.items() if value == capital[0]])
    else:
        print('Unknown capital city')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_state(sys.argv[1])
    else:
        pass