import math
import random
import sorting



sequency = [15, 22, 13, 27, 12, 10, 20, 25]


#sequency_bubble_sort = sorting.Bubble_sort(list.copy(sequency))
#sequency_selection_sort = sorting.Selection_sort(list.copy(sequency))
#sequency_insertion_sort = sorting.Insetion_sort(list.copy(sequency))
sorting.Quick_sort(sequency, 0, len(sequency)-1)
#print(sequency)
#print(sequency_bubble_sort)
#print(sequency_selection_sort)
#print(sequency_insertion_sort)
print(sequency)



    