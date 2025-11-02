
print("Welcome to ChatBite Restaurant!")

menu = {
    "Pizza": 250,
    "Burger": 150,
    "Pasta": 200,
    "Sandwich": 120,
    "Coffee": 80
}

order_id = 100  

while True:
    print("\nHow can I help you today?")
    order_list = []
    total = 0
    order_id += 1

    print(f"\nYour Order ID: ORD{order_id}")
    
    # --- Order Taking Loop ---
    while True:
        print("\n----- MENU -----")
        for item, price in menu.items():
            print(f"{item} : ₹{price}")
        
        choice = input("\nEnter the item you want to order (or type 'done' to finish): ").title()

        if choice == "Done":
            break
        elif choice in menu:
            order_list.append(choice)
            total += menu[choice]
            print(f"✅ {choice} added to your order.")
        else:
            print("Sorry, that item is not available.")

    # --- Display Order Summary ---
    print("\n----- ORDER SUMMARY -----")
    print(f"Order ID: ORD{order_id}")
    if order_list:
        for item in order_list:
            print(f"- {item} : ₹{menu[item]}")
        print(f"Total Bill: ₹{total}")
        print("Order Confirmed! Thank you for ordering with ChatBite Restaurant! ")
    else:
        print("No items ordered. Visit again!")

    # --- Ask for another customer ---
    again = input("\nWould you like to take another order? (yes/no): ").lower()
    if again != "yes":
        print("\n Thank you for visiting ChatBite Restaurant! Have a great day! ")
        break
