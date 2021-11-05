import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_finds_player_with_right_name(self):
        name = "Kurri"
        player = self.statistics.search(name)
        string = "Kurri EDM 37 + 53 = 90"
        self.assertAlmostEqual(str(player), string)

    def test_search_gets_a_player_that_dont_exists(self):
        name = "Mika Häkkinen"
        player = str(self.statistics.search(name))
        self.assertEqual(player, "None")

    def test_team_have_right_players(self):
        players = self.statistics.team("EDM")
        team = ["Semenko EDM 4 + 12 = 16",
                "Kurri EDM 37 + 53 = 90",
                "Gretzky EDM 35 + 89 = 124"]
        self.assertEqual(len(players), 3)
        for i in range(3):
            self.assertEqual(str(players[i]), team[i])

    def test_top_scorers_gets_right_players(self):
        top = ["Gretzky EDM 35 + 89 = 124",
               "Lemieux PIT 45 + 54 = 99"]
        players = self.statistics.top_scorers(1)
        self.assertEqual(len(players), 2)
        for i in range(2):
            self.assertEqual(str(players[i]), top[i])
