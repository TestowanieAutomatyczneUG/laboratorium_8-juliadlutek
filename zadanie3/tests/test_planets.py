import unittest
# from '../src/planets.py' import *
from src.sample.planets import *


class PlanetsTest(unittest.TestCase):
    def setUp(self):
        self.temp = Planets()
        
    def test_planets_ziemia(self):
        self.assertEqual('31.69', self.temp.func(1000000000, "Ziemia"))

    def test_planets_merkury(self):
        self.assertEqual('280.88', self.temp.func(2134835688, "Merkury"))
        
    def test_planets_int_none(self):
        self.assertRaises(Exception, self.temp.func, 267829, None)

    def test_planets_array_string(self):
        self.assertRaises(Exception, self.temp.func, [], "Ziemia")

    def test_planets_string_int(self):
        self.assertRaises(Exception, self.temp.func, "Ala", 12)
        
    def test_planets_wrong_planet_name(self):
        self.assertRaises(Exception, self.temp.func, 267829, "Zzziemia")
        
    def test_planets_wrong_age(self):
        self.assertRaises(Exception, self.temp.func, -267829, "Ziemia")
        
    def tearDown(self):
        self.temp = None
