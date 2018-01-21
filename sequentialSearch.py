# SEQUENTIAL SEARCH / LINEAR SEARCH
the_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]

def sequentialSearch(the_list, item):
    position = 0
    found = False

    while position < len(the_list) and not found:
        if the_list[position] == item:
            found = True
        
        position += 1

    return found


print(sequentialSearch(the_list, 3)) # This should print False
print(sequentialSearch(the_list, 8)) # This should print True



# ORDERED SEQUENTIAL SEARCH
the_ordered_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]

def orderedSequentialSearch(the_ordered_list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(the_ordered_list) and not found and not stop:
        if the_ordered_list[pos] == item:
            found = True
            
        elif the_ordered_list[pos] > item:
            stop = True
        
        else:
            pos += 1

    return found, stop


print(orderedSequentialSearch(the_ordered_list, 2))
print(orderedSequentialSearch(the_ordered_list, 100))
print(orderedSequentialSearch(the_ordered_list, 3))
