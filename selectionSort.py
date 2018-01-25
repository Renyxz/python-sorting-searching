# SELECTION SORT

def selectionSort(the_list):

    for i in range(len(the_list)-1, 0, -1): # Loop starts from the last index of the list and ends at index 0.
        posOfLargestNum = 0 # Starting from 0 we mark the largest number through the looping process.
        for pos in range(1, i+1): # Loop starts from index 1 of the list and ends at its latest last index (the compare point).
            if the_list[pos] > the_list[posOfLargestNum]: # If the current item is greater than the current largest item,
                posOfLargestNum = pos # assign the position of the current item as the position of the largest number.
                # Thus, the current item would become the current largest item.

        temp_item = the_list[i] # Save the current compare point item as a temporary item.
        the_list[i] = the_list[posOfLargestNum] # assign the largest item to the compare point item.
        the_list[posOfLargestNum] = temp_item # assign the old compare point item as the largest item

    return the_list

the_list = [54,26,93,17,77,31,44,55,20]

print( selectionSort(the_list) )