import unittest
from src.coffee_shop import CoffeeShop
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCoffeeShop(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("Cappuccino",20,30)
        self.drink2 = Drink("Espresso",10,70)
        self.food1 = Food("Croissant",10,15)
        self.food2 = Food("Ham Sandwitch",20,50)
        stock = {self.drink1:5,self.drink2:5,self.food1:5,self.food2:5}
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
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_enough_money(self):
        test_customer = Customer("Jo",10,100,10)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_above_16(self):
        test_customer = Customer("John",500,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,120)
    
    def test_customer_below_16(self):
        test_customer = Customer("Johnathan",500,10,10)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_adds_energy(self):
        test_customer = Customer("Janice",500,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(test_customer.energy_level,40)
    
    def test_customer_energy_too_high(self):
        test_customer = Customer("John",500,20,1000)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_customer_reduce_energy(self):
        test_customer = Customer("Jessie",500,20,50)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.assertEqual(test_customer.energy_level,35)
    
    def test_item_in_menu(self):
        test_customer = Customer("Jo",100,20,10)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,120)
    
    def test_item_not_in_menu(self):
        test_customer = Customer("Jo",100,20,10)
        test_drink = Drink("Mocha",10,10)
        self.coffee_shop.sell_drink_to_customer(test_drink,test_customer)
        self.assertEqual(self.coffee_shop.till,100)
    
    def test_drink_runs_out(self):
        test_customer = Customer("Jo",1000,20,-1000)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)
        self.assertEqual(self.coffee_shop.till,200)
    
    def test_food_runs_out(self):
        test_customer = Customer("Jo",1000,20,100)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)
        self.assertEqual(self.coffee_shop.till,150)
    
    def test_stock_value(self):
        self.assertEqual(self.coffee_shop.stock_value(),300)
    
    def test_integration1(self):
        test_customer = Customer("Joe",100,20,75)                            # START: 100 wallet, 75 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)   # SUCCEEDS -> 80 wallet, 105 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)   # FAILS -> high energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)   # FAILS -> high energy
        self.coffee_shop.sell_food_to_customer(self.food2,test_customer)     # SUCCEEDS -> 60 wallet, 55 energy
        self.coffee_shop.sell_food_to_customer(self.food2,test_customer)     # SUCCEEDS -> 40 wallet, 5 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)   # SUCCEEDS -> 20 wallet, 35 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)   # SUCCEEDS -> 0 wallet, 65 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)   # FAILS -> no money
        test_stock = {self.drink1:2,self.drink2:5,self.food1:5,self.food2:3}
        self.assertEqual(self.coffee_shop.stock,test_stock)
        self.assertEqual(test_customer.energy_level,65)
        self.assertEqual(test_customer.wallet,0)
    
    def test_integration1(self):
        test_customer = Customer("Jeremiah",200,20,0)                       # START: 200 wallet, 0 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)  # SUCCEEDS -> 180 wallet, 30 energy
        self.coffee_shop.sell_drink_to_customer(self.drink2,test_customer)  # SUCCEEDS -> 170 wallet, 100 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)  # FAILS -> high energy
        self.coffee_shop.sell_food_to_customer(self.food1,test_customer)    # SUCCEEDS -> 160 wallet, 85 energy
        self.coffee_shop.sell_food_to_customer(self.food2,test_customer)    # SUCCEEDS -> 140 wallet, 35 energy
        self.coffee_shop.sell_drink_to_customer(self.drink2,test_customer)  # SUCCEEDS -> 130 wallet, 105 energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)  # FAILS -> high energy
        self.coffee_shop.sell_drink_to_customer(self.drink1,test_customer)  # FAILS -> high energy
        test_stock = {self.drink1:4,self.drink2:3,self.food1:4,self.food2:4}
        self.assertEqual(self.coffee_shop.stock,test_stock)
        self.assertEqual(test_customer.energy_level,105)
        self.assertEqual(test_customer.wallet,130)



    
