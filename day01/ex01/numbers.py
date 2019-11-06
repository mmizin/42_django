
def print_numbers_from_file():
    with open('numbers.txt', 'r') as file:
        l_numbers = file.read().split(',')
        for num in l_numbers:
            print(num)


if __name__ == '__main__':
    print_numbers_from_file()