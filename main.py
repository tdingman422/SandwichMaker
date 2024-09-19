import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    order_input = "blank"

    while order_input != "off":
        order_input = input("What would you like? (small/ medium/ large/ off/ report):")

        if order_input == "small" or order_input == "medium" or order_input == "large":
            if sandwich_maker_instance.check_resources(recipes[order_input]["ingredients"]):
                money = cashier_instance.process_coins()
                if cashier_instance.transaction_result(money, recipes[order_input]["cost"]):
                    sandwich_maker_instance.make_sandwich(order_input, recipes[order_input]["ingredients"])
        elif order_input == "report":
            print(sandwich_maker_instance.machine_resources)
        elif order_input == "off":
            print("Shutting Down")


if __name__=="__main__":
    main()