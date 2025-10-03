# Taco tuesday special

item_names = ["Taco", "Burrito", "Nachos", "Soft Drink"]
item_prices = [5.70, 6.25, 4.99, 1.75]

def print_menu():
    print()
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")
    print()

def get_name(selection):
    return item_names[selection - 1] # -1 because index starts at: 0, 1, 2 , 3

def get_price(selection):
    return item_prices[selection - 1]

print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

ordered_items = [] # user will fill up with choice
total_due = 0.0
done = False # will loop until its True.

while not done: # our humble loop
    print_menu() # calling our menu like u asked!
    choice = int(input("Enter your selection (1-5): "))   #integer because I dont have a secret menu.

    if choice == 5: # Quit will change the statement to true so we can end the loop.
        print("You ordered:"," and ".join(ordered_items), "Your total is $", round(total_due, 2)) # rounded so my menu stays clean
        done = True
    elif choice >= 1 and choice <= 4:
        name = get_name(choice)
        price = get_price(choice)
        print("You selected a", name)
        ordered_items.append(name) # adds the user choice to our list
        total_due = total_due + price
    else:
        print("Invalid option.")