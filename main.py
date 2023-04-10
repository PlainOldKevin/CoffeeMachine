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

# Bool to terminate program
machine_off = False

# TODO Prompt User
while machine_off == False:
    # Get input
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO Shut down machine upon request
    if user_input == "off":
        print("\n------ *MACHINE POWERING DOWN* ------\n")
        quit()

    # TODO Print report upon request
    if user_input == "report":
        # Print table
        for k, v in resources.items():
            resource = k
            supply = v
            # If statements for different units
            if k == "Water" or "Milk":
                print(k + ":", str(v) + "mL")
            # TODO fix this printing mL for eveything instead of intended
            elif k == "Coffee":
                print(k + ":", str(v) + "g")
