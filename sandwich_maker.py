class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.machine_resources["bread"] -= order_ingredients["bread"]
        self.machine_resources["ham"] -= order_ingredients["ham"]
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        print(sandwich_size + " sandwich is ready. Bon appetit!")
