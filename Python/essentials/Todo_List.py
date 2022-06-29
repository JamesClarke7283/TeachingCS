def print_todos(lst):
    for index, value in enumerate(lst):
        print(f"{index + 1}. {value}")
lst = ["Hi", "Bye", "Waddup", "Nice"]
print_todos(lst)