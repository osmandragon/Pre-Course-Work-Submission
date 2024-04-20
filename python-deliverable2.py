def main():
    # Ask for user's name
    print("Welcome to the GC Fruit Market!")
    name = input("What is your name? ")

    # Display list of fruits and their prices
    fruit_prices = {
        "Apple": 2,
        "Grape": 1,
        "Orange": 3
    }

    # Initialize variables to track fruit purchases
    fruit_quantities = {fruit: 0 for fruit in fruit_prices}

    # Initialize variables for subtotal and total
    subtotal = 0
    tax_rate = 0.05

    # Buying process
    while True:
        # Display welcome message
        print(f"\nWelcome {name}. Which fruit would you like to buy?")

        # Display list of fruits and their prices
        print("Fruit List:")
        for i, (fruit, price) in enumerate(fruit_prices.items(), 1):
            print(f"{i}. {fruit}: ${price}")

        # Ask user which fruit they want to buy
        choice = input("> ")
        while not choice.isdigit() or int(choice) not in range(1, len(fruit_prices) + 1):
            print("Invalid choice. Please enter a number from the list.")
            choice = input("> ")

        choice = int(choice)
        fruit_name = list(fruit_prices.keys())[choice - 1]
        fruit_price = fruit_prices[fruit_name]

        # Update fruit quantities
        fruit_quantities[fruit_name] += 1

        # Update subtotal
        subtotal += fruit_price

        # Display message after purchasing a fruit
        print(f"You bought 1 {fruit_name} at ${fruit_price}")

        # Ask if user wants to buy more fruit
        choice = input("Would you like to buy another piece of fruit? (y/n) ").lower()
        if choice != 'y':
            break

    # Calculate tax
    tax = subtotal * tax_rate

    # Calculate total
    total = subtotal + tax

    # Print receipt
    print(f"\nOrder for {name}:")
    for fruit, quantity in fruit_quantities.items():
        if quantity > 0:
            print(f"{quantity} {fruit}(s) at ${fruit_prices[fruit]} apiece")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
