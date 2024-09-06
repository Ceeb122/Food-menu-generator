# Simple Food Menu Generator Script

def add_menu_item(menu):
    food_item = input("Enter food item name: ")
    price = input(f"Enter price for {food_item}: ")
    menu[food_item] = price
    print(f"{food_item} added to the menu with price {price}.\n")

def show_menu(menu):
    if not menu:
        print("Menu is empty.")
    else:
        print("\n--- Food Menu ---")
        for item, price in menu.items():
            print(f"{item}: ${price}")
        print("\n")

def main():
    print("Welcome to the Food Menu Generator!")
    menu = {}
    while True:
        print("1. Add food item to menu")
        print("2. Show menu")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_menu_item(menu)
        elif choice == '2':
            show_menu(menu)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
