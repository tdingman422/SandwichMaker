### Data ###
from contextlib import nullcontext

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] >= ingredients["bread"]:
            if self.machine_resources["ham"] >= ingredients["ham"]:
                if self.machine_resources["cheese"] >= ingredients["cheese"]:
                    return True
                else:
                    print("Sorry not enough cheese.")
                    return False
            else:
                print("Sorry not enough ham.")
                return False
        else:
            print("Sorry not enough bread.")
            return False

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = input("How many dollars?: ")
        half_dollars = input("How many half dollars?: ")
        quarters = input("How many quarters?: ")
        nickels = input("How many nickels?: ")
        return int(dollars) + (int(half_dollars) * 0.5) + (int(quarters) * 0.25) + (int(nickels) * 0.05)


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            if coins > cost:
                print("Here is $" + str(coins - cost) + " in change")
            return True
        else:
            print("Sorry, that’s not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(sandwich_size + " sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)
order_input = "blank"

while order_input != "off":
    order_input = input("What would you like? (small/ medium/ large/ off/ report):")

    if order_input == "small" or order_input == "medium" or order_input == "large":
        if machine.check_resources(recipes[order_input]["ingredients"]):
            money = machine.process_coins()
            if machine.transaction_result(money, recipes[order_input]["cost"]):
                machine.make_sandwich(order_input, recipes[order_input]["ingredients"])
    elif order_input == "report":
        print(machine.machine_resources)
    elif order_input == "off":
        print("Shutting Down")
