vegetables = ["tomatoes", "potatoes", "onions"]
print("vegetable list:", vegetables)

vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()

is_carrot="carrots" in vegetables
is_cucumber="cucumbers" in vegetables

print("updated Vegetable Inventory:", vegetables)
if is_carrot==True:
    print("carrots are already in the list.")
else:
    print("carrots aren't in the list")

if is_cucumber == True:
    print("cucumber are already in the list.")
else:
    print("cucumber aren't in the list")


    