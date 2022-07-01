def get_input():
    name = input("what is your name: ")
    age = input("what is your age: ")
    return name, age


def calculate():
    name, age = get_input()
    print(f"Provided name is: {name}")
    print(f"Provided age is: {age}")
    try:
        age = int(age)
        x = 100 - age
        if x < 0:
            print("provided age {} is out of scope for {}".format(age, name))
        else:
            print(f"{name} will get 100 after {x} years")
    except:
        raise Exception("Provided value is not correct.")


if __name__ == "__main__":
    calculate()