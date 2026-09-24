import unittest
from challenge import lightsaber_color

class TestLightsaberColor(unittest.TestCase):
    def test_luke_skywalker(self):
        self.assertEqual(lightsaber_color("Luke Skywalker"), "green")


    def test_yoda(self):
        self.assertEqual(lightsaber_color("Yoda"), "green")

    def test_mace_windu(self):
        self.assertEqual(lightsaber_color("Mace Windu"), "purple")

    def test_darth_vader(self):
        self.assertEqual(lightsaber_color("Darth Vader"), "red")

    def test_darth_maul(self):
        self.assertEqual(lightsaber_color("Darth Maul"), "red")

    def test_obi_wan_kenobi(self):
        self.assertEqual(lightsaber_color("Obi-Wan Kenobi"), "blue")


    def test_unknown_character(self):
        self.assertEqual(lightsaber_color("Han Solo"), "unknown")

        
if __name__ == "__main__":
    unittest.main()