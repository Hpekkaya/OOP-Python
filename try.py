class CoffeeMaker:
    def __init__(self):
        self.resorces = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    def report(self):
        """Print all the quantity of resources"""
        print(f"Water  : {self.resorces["water"]} ml")
        print(f"Milk   : {self.resorces["milk"]} ml")
        print(f"Coffee : {self.resorces["coffee"]} ml")

    def is_resources_sufficient(self,drink):
        can_make=True
        for item in drin