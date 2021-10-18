def search(my_list, element):
    for i in range(len(my_list)):
        if element == my_list[i]:
            return i
    return -1
