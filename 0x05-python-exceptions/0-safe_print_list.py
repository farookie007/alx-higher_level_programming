#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    no = 0
        for element in my_list[:x]:
            try:
                print("{}".format(element), end="")
                no += 1
            except:
                break
            finally:
                print()
                return no
