import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Mohito",20,0)
    
    def test_drink_has_name(self):
        self.assertEqual("Mohito",self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(20,self.drink.price)