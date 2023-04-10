MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 500,
    "Milk": 400,
    "Coffee": 150,
    "Money": 0.00
}

# Function to power down machine
def power_down():
    print("\n------ *MACHINE POWERING DOWN* ------\n")
    quit()

# Function to print report for machine
def print_report():
    # Print table
        for k, v in resources.items():
            resource = k
            supply = v
            # If statements for different units
            if k == "Water":
                print(k + ":", str(v) + "mL")
            elif k == "Milk":
                print(k + ":", str(v) + "mL")
            elif k == "Coffee":
                print(k + ":", str(v) + "g")
            else:
                print(k + ":", "$" + str("{:.2f}".format(v)))

# Function to check if there are enough resources for a given drink
def check_resources(input):
    # Espresso ingredients
    if input == "espresso":
        # Water AND Coffee
        if resources["Water"] < MENU["espresso"]["ingredients"]["water"] and resources["Coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            # Error message
            print("\nSorry, there is not enough water and coffee in the machine to make your espresso.")
            print("Please contact the vending manager to refill machine.\n")
        # Water
        elif resources["Water"] < MENU["espresso"]["ingredients"]["water"]:
            print("\nSorry, there is not enough water in the machine to make your espresso.")
            print("Please contact the vending manager to refill machine.\n")
        # Coffee
        elif resources["Coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough coffee in the machine to make your espresso.")
            print("Please contact the vending manager to refill machine.\n")
    elif input == "latte":
        # Water, Coffee, Milk
        if resources["Water"] < MENU["latte"]["ingredients"]["water"] and resources["Coffee"] < MENU["latte"]["ingredients"]["coffee"] and resources["Milk"] < MENU["latte"]["ingredients"]["milk"]:
            # Error message
            print("\nSorry, there is not enough water, coffee, and milk in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
        # Water and milk
        elif resources["Water"] < MENU["latte"]["ingredients"]["water"] and resources["Milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("\nSorry, there is not enough water and milk in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
        # Water and coffee
        elif resources["Water"] < MENU["latte"]["ingredients"]["water"] and resources["Coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough water and coffee in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
        # Milk and coffee
        elif resources["Milk"] < MENU["latte"]["ingredients"]["milk"] and resources["Coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough milk and coffee in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
        # Water
        elif resources["Water"] < MENU["latte"]["ingredients"]["water"]:
            print("\nSorry, there is not enough water in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
        # Milk
        elif resources["Milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("\nSorry, there is not enough water and milk in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
        # Coffee
        elif resources["Coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough water and coffee in the machine to make your latte.")
            print("Please contact the vending manager to refill machine.\n")
    elif input == "capuccino":
        # Water, Coffee, Milk
        if resources["Water"] < MENU["capuccino"]["ingredients"]["water"] and resources["Coffee"] < MENU["capuccino"]["ingredients"]["coffee"] and resources["Milk"] < MENU["capuccino"]["ingredients"]["milk"]:
            # Error message
            print("\nSorry, there is not enough water, coffee, and milk in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Water and milk
        elif resources["Water"] < MENU["capuccino"]["ingredients"]["water"] and resources["Milk"] < MENU["capuccino"]["ingredients"]["milk"]:
            print("\nSorry, there is not enough water and milk in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Water and coffee
        elif resources["Water"] < MENU["capuccino"]["ingredients"]["water"] and resources["Coffee"] < MENU["capuccino"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough water and coffee in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Milk and coffee
        elif resources["Milk"] < MENU["capuccino"]["ingredients"]["milk"] and resources["Coffee"] < MENU["capuccino"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough milk and coffee in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Water
        elif resources["Water"] < MENU["capuccino"]["ingredients"]["water"]:
            print("\nSorry, there is not enough water in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Milk
        elif resources["Milk"] < MENU["capuccino"]["ingredients"]["milk"]:
            print("\nSorry, there is not enough water and milk in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Coffee
        elif resources["Coffee"] < MENU["capuccino"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough water and coffee in the machine to make your capuccino.")
            print("Please contact the vending manager to refill machine.\n")

# Bool to terminate program
machine_off = False

# Prompt User
while machine_off == False:
    # Get input
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # Shut down machine upon request
    if user_input == "off":
        power_down()

    # Print report upon request
    if user_input == "report":
        print_report()

    # Check if resources are sufficient
    check_resources(user_input)


