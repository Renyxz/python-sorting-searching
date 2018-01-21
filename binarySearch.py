# BINARY SEARCH (Divide & Conquer strategy)
the_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

def binarySearch(the_list, item):
    first = 0
    last = len(the_list) - 1
    pos = None
    found = False

    while first <= last and not found:
        mid = int(round((first + last) / 2))

        if the_list[mid] == item:
            found = True
            pos = mid

        elif the_list[mid] < item:
            first = mid + 1

        else:
            last = mid - 1

    return found, pos

print(binarySearch(the_list, 2))
print(binarySearch(the_list, 13))
print(binarySearch(the_list, 45))
