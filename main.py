from player import Player
from sort import quicksort
from search import binary_search
import csv


def read_file(filename):
    """
    Read a csv file containing list of chess players
    and return a sorted list using quicksort

    :param filename: csv file path ('chess-players.csv')
    :return: list: list of players read from file
    """
    # empty list that will hold list of players
    list = []

    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            last_name = row['Last name']
            first_name = row['First name']
            full_name = row['Full name']
            countries = row['Countries'].split(',')
            dob = row['born']
            died = row['died']
            player = Player(first_name, last_name, full_name, countries, dob, died)
            list.append(player)

    # return a list of chess player that has been sorted using quicksort
    return quicksort(list)


# Beware of the underscores here
if __name__ == '__main__':
    list_players = read_file('chess-players.csv')
    # for x in list_players:
    # print(x.last_name, x.first_name, x.full_name, x.country, x.date_of_birth, x.died)
    name = str(input("Enter player Last name to find: "))
    result = binary_search(list_players, name)