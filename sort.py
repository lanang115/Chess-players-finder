from random import randint


def quicksort(list):
    """
    the quicksort algorithm applies the divide-and-conquer
    principle to divide the input array into two lists,
    the first with small items and the second with large items.

    :param list: it's the list of chess players that we want to sort
    :return: sorted list, from low to high
    """
    # If the input list contains fewer than two elements,
    # then return it as the result of the function
    if len(list) < 2:
        return list

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = list[randint(0, len(list) - 1)]

    for item in list:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)
