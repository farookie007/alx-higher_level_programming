#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    no = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end="")
            no += 1
        except (ValueError):
            continue
    print()
    return no
