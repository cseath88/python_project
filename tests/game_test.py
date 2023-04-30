import unittest
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game("Half-Life 2", "Half-Life 2 is a 2004 first-person shooter (FPS) game developed by Valve.", "10", "5.00", "9.00", "PC")

    def test_game_has_title(self):
        self.assertEqual("Half-Life 2", self.game.title)

    def test_game_has_description(self):
        self.assertEqual("Half-Life 2 is a 2004 first-person shooter (FPS) game developed by Valve.", self.game.description)

    def test_game_has_stock_level(self):
        self.assertEqual("10", self.game.stock_level)

    def test_game_has_buy_price(self):
        self.assertEqual("5.00", self.game.buy_price)

    def test_game_has_sell_price(self):
        self.assertEqual("9.00", self.game.sell_price)

    def test_game_has_platform(self):
        self.assertEqual("PC", self.game.platform)