def binary_search(arr, x):
    """
    Binary search, finding the corresponding last name inside the array

    :param arr: List of chess player array
    :param x: the input keywords for last name
    :return: found, which is the object that matches with the x value
    """
    # getting the middle index by dividing length of the array
    m = len(arr) // 2
    found = None

    while x.lower() != arr[m].last_name.lower():
        # if middle less than 1, it will break the loop
        if m < 1:
            break

        if arr[m].last_name.lower() > x.lower():
            arr = arr[:len(arr) // 2]

        else:
            start = len(arr) // 2 + 1

            if start >= len(arr):
                start = len(arr) // 2

            arr = arr[start:]

        m = len(arr) // 2
    # if the last name matches with x, print the object details
    if arr[m].last_name.lower() == x.lower():
        print('yay! Found this: ')
        found = arr[m]
        print(f' {found}')
    else:
        print('sorry :(')
        print(f'Player {x} not found')

    return found
