class Cashier:
    def __init__(self):
        pass

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
