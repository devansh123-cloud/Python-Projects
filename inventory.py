# 🛍️ Inventory Management System
# 1. Add Item
# 2. Search Item
# 3. Edit Item
# 4. Delete Item
# 5. Show All Items
# 6. Exit

# Enter your choice: 1
# Enter Item Name: pen
# Enter Quantity: 50
# Enter Price: 10
# ✅ Item added successfully!


inventory = {}

while True : 
    print("🛍️ Inventory Management System")
    print("1. Add Item")
    print("2. Search Item")
    print("3. Edit Item")
    print("4. Delete Item")
    print("5. Show All Items")
    print("6. Exit")

    choice = input("Enter your choice : ")
    
    if choice == "1":
        item = input("Enter Item Name : ")
        quantity = input("Enter Quantity :")
        price = input("Enter Price :")
        
        inventory[item] = {
            "quantity" : quantity,
            "price" : price
        }
        
        print("✅ Item added successfully!")
        
    elif choice == "2":
            search_item = input("Enter Item to Search :")
            
            if search_item in inventory:
             
              print("Item Found! ")
              print(f"Quantity: {inventory[search_item]['quantity']}")
              print(f"Price : {inventory[search_item]['price']}")
              
            else :
                print("Item Not Found")