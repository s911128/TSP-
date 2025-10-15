import math
import random
import sorting

sequency = [27, 22 ,20, 25]
sequency_bubble_sort = sorting.Bubble_sort(list.copy(sequency))
sequency_selection_sort = sorting.Selection_sort(list.copy(sequency))
sequency_insertion_sort = sorting.Insetion_sort(list.copy(sequency))
sequency_quick_sort = sorting.Quick_sort(list.copy(sequency))
print(sequency)
print(sequency_bubble_sort)
print(sequency_selection_sort)
print(sequency_insertion_sort)
print(sequency_quick_sort)

    