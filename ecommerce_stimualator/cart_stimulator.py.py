items_catalogue = {"Watch": 10000,
                   "Tv": 25000,
                   "Airpods": 3500,
                   "Perfume": 2500,
                   "Clock": 1500,
                   "Shoes": 6500}
your_cart = []

def display_menu():
    print("Please choose an option:")
    print("1. View product catalogue.")
    print("2. Add Item to cart.")
    print("3. Remove item from cart.")
    print("4. View cart.")
    print("5. Apply discount code.")
    print("6. Checkout.")
    print("7. Exit")

def view_catalogue():
    for key , value in items_catalogue.items():
        print(f"{key:10}: Rs{value}")


def add_to_cart(your_cart):
    item = input("What item would u like to buy? ").title()
    if item == "":
        print("❌ Please Enter an item to buy!")
    elif item in items_catalogue:
        your_cart.append(item)
        print(f"✅ {item} has been added to the cart.")
    else :
        print(f"❌ {item} is not available at the moment.")
        
        

def remove_from_cart(your_cart):
    item = input("Which item to u want to remove?").title()
    if item not in your_cart:
        print(f"{item} is already not in the cart.")
    else:
        your_cart.remove(item)
        print(f"{item} is removed from ur cart.")

def view_cart(your_cart):
    if not your_cart:
        print("Your cart is empty!")
    else:
        print("Your cart is:")
        total = 0
        for item  in your_cart:
            price = items_catalogue[item]
            print(f"{item:10}: Rs.{price}")
            total += price
        print(f"Your total till now is: Rs.{total}")

def apply_discount(your_cart, cart_total):
    valid_codes = {"SAVE10": 10 , "SAVE20" : 20 , "SAVE30": 30}
    if not your_cart:
        print("Cart is empty. \nAdd items to your cart first.\n")
        return 0 
    
    cart_total = sum(items_catalogue[item] for item in your_cart)
    print(f"Your current total is: Rs.{cart_total}")

    discount = input("Enter a valid discount code:").upper()
    if discount not in valid_codes:
        print("Invalid Discount code!")
        return cart_total
    else:
        discount_percentage = valid_codes[discount]
        discounted_price = cart_total - (cart_total * discount_percentage / 100)
        print (f"The discount applied: {discount_percentage}%")
        print(f"Your Total now is: Rs.{discounted_price}")
        return discounted_price
        

def checkout(your_cart , cart_total):
    print("Order summary:")
    for item in your_cart:
        print(f"{item:10}:Rs.{items_catalogue[item]}")
    cart_total = sum(items_catalogue[item] for item in your_cart)
    print (f"Your total is:Rs.{cart_total}")

def main():
    is_running = True
    cart_total = 0
    print("Welcome to Python Ecommerce Store!")
    while is_running:
       
        display_menu()
        try:
            menu_choice = int(input("Please choose from 1-7: "))
        except ValueError:
            print("❌ Invalid choice! Please enter a number between 1-7")
            continue

        if menu_choice < 1 or menu_choice > 7:
            print("Option not avalaible!")
            continue

        if menu_choice == 1:
            print("This the product catalogue:\n")    
            view_catalogue()
            input("Press Enter to continue..")

        elif menu_choice == 2:
            view_catalogue()
            add_to_cart(your_cart)
            input("Press Enter to continue..")

        elif menu_choice == 3:
            remove_from_cart(your_cart)
            input("Press Enter to continue..")
        elif menu_choice == 4:
            view_cart(your_cart)
            input("Press Enter to continue..")
        elif menu_choice == 5:
            #view_cart(your_cart)
           cart_total = apply_discount(your_cart , cart_total)
           input("Press Enter to continue..")

        elif menu_choice == 6:
            checkout(your_cart , cart_total)
            input("Press Enter to continue..")
        elif menu_choice == 7:
            print("Thanks for shopping")
            print(f"Your total is: Rs.{cart_total}")
            print("Goodbye")
            is_running = False





if __name__ == "__main__":
    main()

