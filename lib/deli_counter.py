katz_deli = []

def line(katz_deli):
    list_names = list()
    count = 0
    if (not katz_deli):
        print ("The line is currently empty.")
    else:
        for i in katz_deli:
            count += 1
            list_names.append(f"{count}. {i}")
        join_names = " ".join(list_names)
        print(f"The line is currently: {join_names}")
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line." )
def now_serving(katz_deli):
    if (not katz_deli):
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        katz_deli.pop(0)