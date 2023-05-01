import unittest
from models.platform import Platform

class TestPlatform(unittest.TestCase):

    def setUp(self):
        self.platform = Platform("PC", "Half-Life 2")

    def test_platform_has_name(self):
        self.assertEqual("PC", self.platform.platform_name)

