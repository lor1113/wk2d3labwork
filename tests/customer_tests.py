import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John",500,20,10)
    
    def test_customer_has_name(self):
        self.assertEqual("John",self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(500,self.customer.wallet)
    
    def test_customer_has_energy_level(self):
        self.assertEqual(10,self.customer.energy_level)
    
    def test_customer_remove_cash(self):
        self.customer.remove_cash(50)
        self.assertEqual(450,self.customer.wallet)
    
    def test_customer_increase_energy(self):
        self.customer.increase_energy(90)
        self.assertEqual(100,self.customer.energy_level)
    
    def test_customer_decrease_energy(self):
        self.customer.decrease_energy(5)
        self.assertEqual(5,self.customer.energy_level)
