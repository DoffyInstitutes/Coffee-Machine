from tabnanny import check

#better in terms of syntax and reducing repeated logic; however, it would be more efficient to iterate through the drink["ingredients"]
# dictionary so that I can save lines of code instead of doing each thing one at a time

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(total):
    for resource, amount in resources.items():
        if resource in ["water", "milk"]:
            unit = "ml"
        else:
            unit = "g"
        print(f"{resource.capitalize()}: {amount}{unit}")
    print(f"Money: ${total:.2f}")

def coins_inserted():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    inserted = quarters*.25+dimes*.1+nickles*.05+pennies*.01
    return inserted

def check_change(response, inserted, total):
    cost = MENU[response]["cost"]
    if inserted>=cost:
        change=inserted - cost
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {response}. Enjoy!")
        total+=cost
    else:
        print("Sorry that's not enough money. Money refunded.")
    return total

def resource_check (response):
    sufficient = False
    milk=0
    if response != "espresso":
        milk = MENU[response]["ingredients"]["milk"]
    water = MENU[response]["ingredients"]["water"]
    coffee = MENU[response]["ingredients"]["coffee"]
    if resources["milk"]-milk<0:
        print("Sorry, there is not enough milk.")
    elif resources["water"]-water<0:
        print("Sorry, there is not enough water.")
    elif resources["coffee"]-coffee<0:
        print("Sorry, there is not enough coffee.")
    else:
        resources["milk"]-=milk
        resources["water"] -= water
        resources["coffee"]-=coffee
        sufficient = True
    return sufficient

def main():
    total = 0.00
    run = True
    while run:
        response = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if response == "report":
            report(total)
        elif response in ["cappuccino", "latte", "espresso"]:
            sufficient = resource_check(response)
            if sufficient:
                inserted = coins_inserted()
                total=check_change(response,inserted, total)
        elif response == "off":
            run=False
        else:
            print("Enter a valid option.")

main()