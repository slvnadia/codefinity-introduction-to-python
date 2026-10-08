# Step 1: Create the grocery_inventory dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# Step 2: Check "Eggs" price
eggs_category, eggs_price, eggs_stock = grocery_inventory["Eggs"]
if eggs_price > 5:
    eggs_price -= 1
    grocery_inventory["Eggs"] = (eggs_category, eggs_price, eggs_stock)
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")

# Step 3: Add "Tomatoes"
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:")
print(grocery_inventory)

# Step 4: Check "Milk" stock
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    milk_category, milk_price, milk_stock = grocery_inventory["Milk"]
    milk_stock += 20
    grocery_inventory["Milk"] = (milk_category, milk_price, milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

# Step 5: Check "Apples" price
if grocery_inventory["Apples"][1] > 2:
    del grocery_inventory["Apples"]
    print("Apples removed from inventory due to high price.")

# Step 6: Print final inventory
print("Updated inventory:")
print(grocery_inventory)