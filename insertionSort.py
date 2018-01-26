# INSERTION SORT

def insertionSort(the_list):

    for i in range(1, len(the_list)): # Starting from index 1 and ends after all items:
        
        checkpoint = the_list[i] # Checkpoint item
        pos = i # current position

        while pos > 0 and the_list[pos - 1] > checkpoint: # When position > 0 and previous position item > checkpoint item:
            the_list[pos] = the_list[pos - 1] # replace the current position item with the previous position item,
            pos = pos - 1 # and its index as well.

        the_list[pos] = checkpoint # After each iteration, make sure the checkpoint item is on its new position.

    return the_list


the_list = [54,26,93,17,77,31,44,55,20]

print( insertionSort(the_list) )