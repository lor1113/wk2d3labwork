class CoffeeShop:
    def __init__(self,name,till,stock):
        self.name = name
        self.till = till
        self.stock = stock
        self.menu = list(stock.keys())
    
    def increase_till(self,amount):
        self.till += amount
    
    def sell_drink_to_customer(self, drink,customer):
        if drink in self.menu:
            if customer.age > 16:
                if customer.energy_level < 100:
                    if customer.wallet >= drink.price:
                        self.increase_till(drink.price)
                        customer.remove_cash(drink.price)
                        customer.increase_energy(drink.caffeine)
                        self.stock[drink] -= 1
                        self.update_menu()

        
    def sell_food_to_customer(self, food,customer):
        if food in self.menu:
            if customer.wallet >= food.price:
                self.increase_till(food.price)
                customer.remove_cash(food.price)
                customer.decrease_energy(food.rejuvenation)
                self.stock[food] -= 1
                self.update_menu()
    
    def update_menu(self):
        menu = []
        for x,y in self.stock.items():
            if y != 0:
                menu.append(x)
        self.menu = menu

    def show_menu(self):
        return self.menu

    def stock_value(self):
        total = 0
        for x,y in self.stock.items():
            total += x.price * y
        return total