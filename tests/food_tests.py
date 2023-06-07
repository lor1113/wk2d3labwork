import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Croissant",10,15)
    
    def test_food_has_name(self):
        self.assertEqual(self.food.name,"Croissant")
    
    def test_food_has_price(self):
        self.assertEqual(self.food.price,10)
    
    def test_food_has_rejuvenation(self):
        self.assertEqual(self.food.rejuvenation,15)