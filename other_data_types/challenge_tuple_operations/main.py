# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#1. Counting an apple in inventory
apple_count = shelf.count("apples")
print("Number of Apples: ", apple_count)

#2. Find first occurence of banana
banana_index = shelf.index("bananas")
print("First Banana Index: ", banana_index)


#3. number of apples
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked")

#4. count grapes appear
grapes_count = shelf.count("grapes")
if grapes_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked")

#5. check oranges in the shelf
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index: ", orange_index)
else:
    print("Oranges are out of stock")
