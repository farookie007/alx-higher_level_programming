#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        no = 0
        for element in my_list[:x]:
            print("{}".format(element), end="")
    except:
        pass
