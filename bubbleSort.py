# BUBBLE SORT
def bubbleSort(the_list):
    for num in range(len(the_list)-1, 0, -1):
        for i in range(num):
            if the_list[i] > the_list[i+1]:
                temp_item = the_list[i]
                the_list[i] = the_list[i+1]
                the_list[i+1] = temp_item
    
    return the_list

the_list = [54,26,93,17,77,31,44,55,20]

print( bubbleSort(the_list) )



# SHORT BUBBLE SORT
def shortBubbleSort(ano_list):
    exchange = True
    num  = len(ano_list) - 1
    
    while num > 0 and exchange:
        exchange = False
        for i in range(num):
            if ano_list[i] > ano_list[i+1]:
                exchange = True
                temp = ano_list[i]
                ano_list[i] = ano_list[i+1]
                ano_list[i+1] = temp
        num -= 1

    return ano_list


ano_list = [20,30,40,90,50,60,70,80,100,110]

print( shortBubbleSort(ano_list) )