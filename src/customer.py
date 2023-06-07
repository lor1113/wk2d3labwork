class Customer:
    def __init__(self,name,wallet,age,energy_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.energy_level = energy_level
    
    def remove_cash(self,amount):
        self.wallet -= amount
    
    def increase_energy(self,amount):
        self.energy_level += amount
    
    def decrease_energy(self,amount):
        self.energy_level -= amount