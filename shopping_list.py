shopping = [ "milk", "bread", "coffee", "cheese", "apples" ]
item1 = input("Please enter the item 1: ")
shopping.append(item1)
item2 = input("Please enter the item 2: ")
shopping.append(item2)  
item3 = input("Please enter the item 3: ")
shopping.append(item3)
item4 = input("Please enter the item 4: ")
shopping.append(item4)
item5 = input("Please enter the item 5: ")
shopping.append(item5)
print("Your shopping list is: ")
for item in shopping:
    print(item)
