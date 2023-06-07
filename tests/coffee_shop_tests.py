import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Cappuccino",20,30)
        self.food = Food("Croissant",10,15)
        stock = {self.drink:5,self.food:5}
        self.coffee_shop = CoffeeShop("The Prancing Pony",100.00,stock)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony",self.coffee_shop.name)
    
    def test_coffee_shop_has_till(self):
        self.assertEqual(100.00,self.coffee_shop.till)
    
    def test_increase_till(self):
        self.coffee_shop.increase_till(2.50)
        self.assertEqual(102.50,self.coffee_shop.till)
    
    def test_customer_no_money(self):
        test_customer = Customer("John",10,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_enough_money(self):
        test_customer = Customer("Jo",10,100,10)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_above_16(self):
        test_customer = Customer("John",500,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,120)
    
    def test_customer_below_16(self):
        test_customer = Customer("Johnathan",500,10,10)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_adds_energy(self):
        test_customer = Customer("Janice",500,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(test_customer.energy_level,40)
    
    def test_customer_energy_too_high(self):
        test_customer = Customer("John",500,20,1000)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_reduce_energy(self):
        test_customer = Customer("Jessie",500,20,50)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.assertEqual(test_customer.energy_level,35)
    
    def test_item_in_menu(self):
        test_customer = Customer("Jo",100,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,120)
    
    def test_item_not_in_menu(self):
        test_customer = Customer("Jo",100,20,10)
        test_drink = Drink("Mocha",10,10)
        self.coffee_shop.sell_drink_to_customer(test_drink,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_drink_runs_out(self):
        test_customer = Customer("Jo",1000,20,-1000)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink,test_customer)
        self.assertEqual(self.coffee_shop.till,200)
    
    def test_food_runs_out(self):
        test_customer = Customer("Jo",1000,20,100)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food,test_customer)
        self.assertEqual(self.coffee_shop.till,150)
    
    def test_stock_value(self):
        self.assertEqual(self.coffee_shop.stock_value(),150)
    
