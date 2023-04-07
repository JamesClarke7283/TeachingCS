names = ["James", "Bob", "Mike"]

def write_names_to_file(names):
    with open("names.txt", "w") as f:
        for name in names:
            f.write(f"Your name is {name}\n")

shopping_lst = ["Butt Cream", "Chicken", "Rice"]

def write_items_to_file(shopping_lst):
    with open("shopping_list.txt", "w") as l:
        for item in shopping_lst:
            l.write(f"{item}\n")

write_items_to_file(shopping_lst)