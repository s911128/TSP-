def Bubble_sort(original_array):
    array = list.copy(original_array)
    for i in range(1,len(array)):
        temp = 0
        isSorted = False
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                isSorted = True
        if not isSorted:
            break
        
    return array

def Selection_sort(original_array):
    array = list.copy(original_array)
    for i in range(len(array)-1):
        minimum = array[i]
        index = i
        isSorted = False
        for j in range(i+1,len(array)):
            if array[j] < minimum:
                minimum = array[j]
                index = j
                isSorted = True
        if isSorted:
            array[index] = array[i]
            array[i] = minimum
        
    return array

def Insetion_sort(original_array):
    array = list.copy(original_array)
    for i in range(1,len(array)):
        temp = array[i]
        j = i
        isStop = False
        while((not isStop) and j!=0):
            if temp < array[j-1]:
                array[j] = array[j-1]
                j = j-1
            else:
                isStop = True
        array[j] = temp

    return array
        


