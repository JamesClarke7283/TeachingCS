""" Teaching about For Loops
for ::=  "for" [single_element_name] "in" starred_list ":"
              [code here]

Other useful methods covered:

range - creates a list in range of numbers in (start, stop)
enumerate - provides both the index and item of the number in format (index, item)
zip - enables you to combine or zip lists together, age = [1,3] and name = ["Bob", "Mike"] becomes (1,"Bob"),(3, "Mike")

"""

print("Example 1")
print("--------------------")

# Example 1, iterating through a list
names = ["James", "Elliot", "Mike", "Bob"]
for name in names:
    print(name)

print("--------------------")

# Example 2, using range
print("Example 2")
print("--------------------")

# As you can see, it's a list from 1 to 9
r = list(range(1, 10))
print(r)

# We Iterate through range and print off each element in the list
for count in range(1, 10):
    print(count)

print("--------------------")
# Iterating through a list by index
for index in range(0, len(names)):
    print(names[index])
print("--------------------")

# Example 3, using enumerate
print("Example 3: Shopping List")
print("--------------------")

shopping_list = ["Bread", "Milk", "Apple's", "Tomato's", "Beef"]
for index, item in enumerate(shopping_list):
    print(f"{index+1}.\t{item}")


print("--------------------")
print("Looking at enumerate:")
print("--------------------")

e = enumerate(shopping_list)
print(list(e))

print("--------------------")

print("--------------------")
print("Example 4, using zip")
print("--------------------")

shopping_list = ["Apple", "Tomato", "Beef"]
shopping_qty = [4, 6, 2]

print("Item\tQuantity")
print("--------------------")
for item, qty in zip(shopping_list, shopping_qty):
    print(f"{item}\t{qty}")
print("--------------------")

print("Exploring Zip:")

z = zip(shopping_list, shopping_qty)
print(list(z))