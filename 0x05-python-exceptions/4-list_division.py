#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two list element by element.
    Args:
        my_list_1 (list): The first list
        my_list_2 (list): The second list
        list_length: The number of elements to divide
    Returns:
        A new list of list length containing all the
        divisions """
    new_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong tpe")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return (new_list)
