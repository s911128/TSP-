def Bubble_sort(array):
    temp = 0
    for i in range(1,len(array)):
        isEnd = True
        for j in range(len(array)-i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
                isEnd = False
        if isEnd:
            break
        
    return array

def Selection_sort(array):
    temp = 0
    for i in range(len(array)-1):
        smallest = i
        for j in range(i+1,len(array)):
            if array[j] < array[smallest]:
                smallest = j
        
        if i != smallest:
            temp_smallest = array[smallest]
            array[smallest] = array[i]
            array[i] = temp_smallest

    return array

def Insetion_sort(array):
    for i in range(1,len(array)):
        temp = array[i]
        j = i
        while(temp < array[j-1] and j > 0):
            array[j] = array[j-1]
            j = j-1
        array[j] = temp

    return array

def Quick_sort(array):
    if len(array) > 1:
        i = 0
        j = len(array)
        k = array[0]
        while(i<j):
            while(True):
                i = i+1
                if i == len(array) or array[i]>k:
                    break
            while(True):
                j = j-1
                if j == 0 or array[j]<k:
                    break
            if i<j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        array[0] = array[j]
        array[j] = k
        if j == 0:
            return array
        else:
            Quick_sort(array[:j])
        if j == len(array)-1:
            return array
        else:
            Quick_sort(array[j+1:])

    else:
        return array


