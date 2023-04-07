names = ["James", "Bob", "Mike"]

def write_names_to_file(names):
    with open("names.txt", "w") as f:
        for name in names:
            f.write(f"Your name is {name}\n")

write_names_to_file(names)
