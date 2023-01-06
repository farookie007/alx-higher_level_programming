#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    n_args = len(sys.argv) - 1
    print(f"{n_args} argument{'' if n_args == 1 else 's'}{'.' if n_args == 0 else ':'}")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
