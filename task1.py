def merge_list(list1: list, list2: list) -> list:
    """
    This function takes two lists as arguments and
    returns a new list merging first list with the
    odd indexes of second list.

    Args:
        list1 (list): first list of numbers
        list2 (list): second list of numbers

    Returns:
        list: new list formed by first list extended
        with odd indexes of second list 
    """
    new_list = list1 + [list2[x] for x in range(len(list2)) if x % 2 != 0]
    return new_list


list1 = [1, 2, 3, 4, 5, 6]  # defined first list
list2 = [10, 20, 30, 40, 50, 60]  # defined second list
print(merge_list(list1, list2))  # merge_list function call
