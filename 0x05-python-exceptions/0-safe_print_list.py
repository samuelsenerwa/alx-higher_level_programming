#!/usr/bin/python3

def safe_print_lst(my_list=[], x=0):
    """Print x elements of a list

    Args:
    my_list (list): The list to print elements from
    x (nt): The number of elements of my_list to prnt

    Retunrns:
    The number of elements to be printed.
    """
    ret = 0
    for in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
