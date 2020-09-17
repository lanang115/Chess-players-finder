from unittest import TestCase
from player import Player
from search import binary_search
from sort import quicksort


class Test(TestCase):
    def setUp(self):
        self.test_players = []
        self.player1 = Player('Lanang', 'Wisnugiri', 'Lanang Wisnugiri', 'Indonesia', 2000, '')
        self.player2 = Player('Christian', 'Ponce', 'Christian Ponce', 'Philippines', 1993, '')
        self.player3 = Player('Lam', 'Fok', 'Lam Fok', 'Hong Kong', 1993, '')
        self.player4 = Player('Marcus', 'Petersen', 'Marcus Petersen', 'Australia', 1998, '')
        self.test_players.append(self.player1)
        self.test_players.append(self.player2)
        self.test_players.append(self.player3)
        self.test_players.append(self.player4)

    def test_search_found(self):
        result = binary_search(self.test_players, 'Petersen')
        self.assertEqual(result, self.player4)

    def test_quicksort(self):
        expected = [self.player3, self.player4, self.player2, self.player1]
        sorted_list = quicksort(self.test_players)

        for i in range(0, 3):
            self.assertEqual(sorted_list[i], expected[i])

    def test_search_not_found(self):
        result = binary_search(self.test_players, 'Jack')
        self.assertEqual(result, None)
