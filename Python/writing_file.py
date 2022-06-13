names = ["James", "Bob", "Mike"]

with open("names.txt", "w") as f:
    for name in names:
        f.write(f"Your name is {name}\n")
print(names)


