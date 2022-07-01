# task1: Here is a employee database with key as employee name and value as employee id
employee_db = {"emp1": "101", "emp2": "102", "emp3": "103"}


for k, v in employee_db.items():
    print(k, v)


# write a function which will reverse the key and value into value:key example {"101": "emp1" ...}

def reverse_employee_db(_input: dict) -> dict:
    employee_map = {v:k for k, v in _input.items()}
    # employee_map = dict()
    # for k, v in _input.items():
    #     employee_map[v] = k
    return employee_map


name_list = ["Wasif", "Alam", "Mofiz", "Rabbi", "Sheikh"]

# Write a function will filter a list by and return the list of name which start with W and M
# python has a function string.start_with() which can return true or false if the string start with
# some word or not
print(name_list[0])


def filter_selected_name(names_list: list) -> list:
    output_list = list()
    for name in names_list:
        if name[0] == "W" or name[0] == "M":
            output_list.append(name)
        # print(name[0])
    return output_list


print(filter_selected_name(name_list))


print(reverse_employee_db(employee_db))

# Consider a file temp.txt now read the file line by line as text and print in the console

def read_file(path: str):
    pass


# consider there is a json file test.json read the json file into a dictionary

def read_json(path: str):
    pass


# def input_info(name: str, age: int):
#     name, age = input("what is your name, age").split()
#     return name, age


def input_info():
    name = input("what is your name")
    age = input("what is your age")
    # print(name, age)
    return name, age


def calculate_age():
    return[]


def i_return_what_i_get(given_to_me=5):
    _ = given_to_me
    return


def you_must_give_me_something(give_me: int):
    _ = give_me
    return



