from collections import Counter

def read_file():
    name_list = []
    path = "data/names.txt"
    file = open(path)
    lines = file.readlines()
    file.close()
    for line in lines:
        name = line.strip()
        name_list.append(name)
        # print(name)
    return name_list


def count_repeated():
    all_names = read_file()
    # unique_names = Counter(all_names)
    # unique_names = dict(unique_names)
    unique_name_dict = {}
    for name in all_names:
        if name in unique_name_dict:
            count_value = unique_name_dict[name]
            unique_name_dict[name] = count_value + 1
        else:
            unique_name_dict[name] = 1

    print(unique_name_dict)


if __name__ == "__main__":
    count_repeated()