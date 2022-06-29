"""This is a module to manage your todos"""


def print_todos(lst):
    """Display your todos with an index

    :param lst: Your todos
    :return:
    """
    for index, value in enumerate(lst):
        print(f"{index + 1}. {value}")


def list_opt():
    """Lists your menu options

    :return:
    """
    opt = ["Print todos", "Add a new todo", "Remove a todo", "Exit the program"]
    print()
    print_todos(opt)
    print()


def menu_opt(opt_select, todos):
    """Executes menu options based on option selected

    :param opt_select: Menu option selected
    :param todos: Your todos
    :return:
    """
    match opt_select:
        case 1:
            print_todos(todos)
        case 2:
            new_todo = input("Enter your new todo:\n")
            todos.append(new_todo)
            print_todos(todos)
        case 3:
            del_todo = int(input("Please enter the index of the todo you would like to remove:\n"))
            del todos[del_todo - 1]
        case 4:
            exit()
        case _:
            print("Incorrect option, please try again\n")


def main():
    """Runs the application

    :return:
    """
    todos = ["Hi", "Bye", "Waddup", "Nice"]

    while True:
        list_opt()
        try:
            opt_select = int(input("Please choose an option:\n"))
            menu_opt(opt_select, todos)
        except ValueError:
            print("Please enter a whole number.", end="\n\n")


if __name__ == '__main__':
    main()
