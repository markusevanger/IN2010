from shuffled_list import make_shuffled_list



#
# BUBBLE SORT
# Har o(n^2) kjøretid
#

def bubbleSort(ul):

    for i in range(len(ul)):
        for j in range(len(ul)):
            if ul[i] != ul[j]:
                if ul[i] < ul[j]:
                    ul[i], ul[j] = ul[j], ul[i]

    return ul

if __name__ == "__main__":

    SIZE_OF_LIST_TO_SORT = 10

    unsortedList = make_shuffled_list(SIZE_OF_LIST_TO_SORT)
    print(unsortedList)
    
    sortedList = bubbleSort(unsortedList)
    print(sortedList)