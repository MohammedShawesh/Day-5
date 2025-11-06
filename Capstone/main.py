from product import Product, Electronics, Clothing, Inventory

inventory = Inventory()
print("Welcome to the GadgetGrove Inventory System")

is_running = True
while is_running:
    print("\n--- Main Menu ---")
    print("1. Add a new product")
    print("2. Look up a product")
    print("3. Update product stock")
    print("4. See all products")
    print("5. Exit")
    print("-"*20)
    choice = input("Please enter your choice (1-5): ")

    if choice == '1':
        # Add a new product
        try:
            prod_type = input("Enter product type (standard, electronic, clothing): ").lower()
            p_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))

            if prod_type == 'standard':
                new_product = Product(p_id, name, price, quantity)
            elif prod_type == 'electronic':
                warranty = int(input("Enter warranty period (months): "))
                new_product = Electronics(p_id, name, price, quantity, warranty)
            elif prod_type == 'clothing':
                size = input("Enter size: ")
                color = input("Enter color: ")
                new_product = Clothing(p_id, name, price, quantity, size, color)
            else:
                print("Invalid product type. Please choose 'standard', 'electronic', or 'clothing'.")
                continue

            inventory.add_product(new_product)

        except ValueError:
            print("Invalid input. Please enter the correct data types.")

    elif choice == '2':
        # Look up a product
        search_term = input("Enter product ID or name to look up: ")
        product = None
        if search_term.isdigit():
            product = inventory.find_product_by_id(int(search_term))
        else:
            product = inventory.find_product_by_name(search_term)

        if product:
            print("\n--- Product Details ---")
            print(product.get_summary())
            print("-----------------------")
        else:
            print("Product not found.")

    elif choice == '3':
        # Update stock
        try:
            p_id = int(input("Enter the ID of the product to update: "))
            new_qty = int(input("Enter the new stock quantity: "))
            inventory.update_stock(p_id, new_qty)
        except ValueError:
            print("Invalid input. Please enter numbers for ID and quantity.")

    elif choice == '4':
        inventory.list_all_products()

    elif choice == '5':
        # Exit
        print("Thank you for using the GadgetGrove Inventory System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")