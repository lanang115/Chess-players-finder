from unittest import TestCase
from player import Player


class TestPlayer(TestCase):
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

    def test_lt(self):
        self.assertLess(self.player3, self.player1)

    def test_gt(self):
        self.assertGreater(self.player1, self.player2)

    def test_ne(self):
        self.assertTrue(self.player3, self.player4)

    def test_eq(self):
        self.assertTrue(self.player1, self.player1)