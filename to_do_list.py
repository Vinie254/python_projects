to_do_list = []
list_length = len(to_do_list)


def view():
    num = 0
    for activity in to_do_list:
        num += 1
        print(f"{num}.{activity}")

while list_length < 100:
    control = input("Enter activity to do ((-) to remove (v) to view (q) to quit): ")
    to_do_list.append(control)
    if control == "-":
        to_do_list.remove("-")
        view()
        number_of_items = int(input("Enter number of items to remove: "))
        for x in range(number_of_items):
            control_1 = int(input("Enter task to remove: "))
            to_do_list.pop(control_1 - 1)
            view()
    elif control == "v":
        to_do_list.remove("v")
        view()
    elif control == "q":
        break

