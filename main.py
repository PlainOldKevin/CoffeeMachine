# Imports
import os


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
    # Header and new line bc it looks pretty
    print("\nRESOURCE-REPORT:")
    # Print table
    for k, v in resources.items():
        # If statements for different units
        if k == "Water":
            print(k + ":", str(v) + "mL")
        elif k == "Milk":
           print(k + ":", str(v) + "mL")
        elif k == "Coffee":
            print(k + ":", str(v) + "g")
        else:
            print(k + ":", "$" + str("{:.2f}".format(v)))
    print("\n")

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
    elif input == "cappuccino":
        # Water, Coffee, Milk
        if resources["Water"] < MENU["cappuccino"]["ingredients"]["water"] and resources["Coffee"] < MENU["cappuccino"]["ingredients"]["coffee"] and resources["Milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            # Error message
            print("\nSorry, there is not enough water, coffee, and milk in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Water and milk
        elif resources["Water"] < MENU["cappuccino"]["ingredients"]["water"] and resources["Milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("\nSorry, there is not enough water and milk in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Water and coffee
        elif resources["Water"] < MENU["cappuccino"]["ingredients"]["water"] and resources["Coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough water and coffee in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Milk and coffee
        elif resources["Milk"] < MENU["cappuccino"]["ingredients"]["milk"] and resources["Coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough milk and coffee in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Water
        elif resources["Water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("\nSorry, there is not enough water in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Milk
        elif resources["Milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("\nSorry, there is not enough water and milk in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")
        # Coffee
        elif resources["Coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("\nSorry, there is not enough water and coffee in the machine to make your cappuccino.")
            print("Please contact the vending manager to refill machine.\n")

# Check if drink input valid
def input_valid(drink):
    if drink == 'espresso':
        return True
    elif drink == 'latte':
        return True
    elif drink == 'cappuccino':
        return True
    elif drink == 'off':
        power_down()
    elif drink == 'report':
        return False
    elif drink == 'refill':
        return False
    else:
        return False

# Function to process coins
def process_coins(drink, q, d, n, p):
    money = round((q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01), 2)
    change = money - MENU[drink]["cost"]
    if MENU[drink]["cost"] > money:
        print("\nSorry, that is not enough money for your " + drink + ".")
        print("Your change is $" + str(money) + ". Have a nice day.\n")
        quit()
    elif MENU[drink]["cost"] < money:
        print("\nTransaction successful.")
        print("Your change is $" + str(round(change, 2)) + ". Have a nice day.\n")
        resources["Money"] += MENU[drink]["cost"]
    else:
        print("\nTransaction successful. No change will be dispensed.\n")

# Function to refill the machine's ingredients
def refill():
    print("Ingredients filled to maximum capacity.")
    resources["Coffee"] == 150
    resources["Water"] == 500
    resources["Milk"] == 400

# TODO finish this function for each coin

# Function to insert quarters into machine
def insert_quarters():
    quarters = int(input("Insert quarters into the machine: "))
    while quarters <= 0 or not isinstance(quarters, int):
        print("Invalid input. Try again.")
        quarters = int(input("Insert quarters into the machine: "))
    return quarters



# Bool to terminate program
machine_off = False

# Prompt User
while machine_off == False:
    # Get input
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Check input
    while input_valid(user_input) == False:
        # Print report
        if user_input == 'report':
            print_report()
            user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
            input_valid(user_input)
        # Refill machine
        elif user_input == 'refill':
            refill()
            user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
            input_valid(user_input)
        # Bad input
        else:
            print("Invalid input. Try again.")
            user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
            input_valid(user_input)

    # Check if resources are sufficient
    check_resources(user_input)

    # Prompt user for coins
    if user_input == 'espresso' or 'latte' or 'cappuccino':
        print("Your " + user_input + " costs $" + str("{:.2f}".format(MENU[user_input]["cost"])) + ".") 

    # Insert coins
    q = insert_quarters()
    d = int(input("Insert dimes into the machine: "))
    n = int(input("Insert nickels into the machine: "))
    p = int(input("Insert pennies into the machine: "))

    # Process the coins to proceed
    process_coins(user_input, q, d, n, p)

    # TODO Deduct coffee machine resources depending on drink of choice
