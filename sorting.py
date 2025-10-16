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

def Quick_sort(array, first_term, last_term):
    if first_term < last_term :
        i = first_term
        j = last_term
        k = array[first_term]
        while(i<j):
            while(True):
                i = i+1
                if i == last_term or array[i]>=k:
                    break
            while(True):
                if j == first_term or array[j]<=k:
                    break
                else:
                    j = j-1
            if i<j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        array[first_term] = array[j]
        array[j] = k
        Quick_sort(array,first_term,j-1)
        Quick_sort(array,j+1,last_term)

def Merge_sort(array, first_term, last_term):
    if first_term < last_term:
        merge_array = []
        mid = (first_term+last_term)//2
        Merge_sort(array, first_term, mid)
        Merge_sort(array, mid+1, last_term)
        i = first_term
        j = mid+1
        k = first_term
        while(i<=mid and j<=last_term):
            if array[i] <= array[j]:
                list.append(merge_array, array[i])
                i = i+1
            else:
                list.append(merge_array, array[j])
                j = j+1
        if i>mid:
            list.extend(merge_array, array[j:last_term])
        else:
            list.extend(merge_array, array[i:mid+1])
        for i in range(len(merge_array)):
            array[first_term+i] = merge_array[i]



