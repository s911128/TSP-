import math
#import random
#import sorting
import numpy as np
import mathFunction

sequency = [26,5,77,1,61,11,59,15,48,19]

#sequency_bubble_sort = sorting.Bubble_sort(list.copy(sequency))
#sequency_selection_sort = sorting.Selection_sort(list.copy(sequency))
#sequency_insertion_sort = sorting.Insetion_sort(list.copy(sequency))
#sorting.Quick_sort(sequency, 0, len(sequency)-1)
#sequency = sorting.Merge_sort(sequency)
#print(sequency)
#print(sequency_bubble_sort)
#print(sequency_selection_sort)
#print(sequency_insertion_sort)

# 1. 地點數據：[X 座標, Y 座標]
# 順序：D0, C1, C2, C3, C4, C5, C6, C7
coordinates = np.array([
    [10, 10],  # D0 (倉庫) -> 索引 0
    [15, 22],  # C1 -> 索引 1
    [8, 18],   # C2 -> 索引 2
    [20, 5],   # C3 -> 索引 3
    [3, 12],   # C4 -> 索引 4
    [25, 15],  # C5 -> 索引 5
    [18, 30],  # C6 -> 索引 6
    [12, 2]    # C7 -> 索引 7
])
NUM_CITIES = len(coordinates)

cities = np.array([
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
])

distance_matrix = np.zeros((NUM_CITIES, NUM_CITIES))

for i in range(NUM_CITIES-1):
    for j in range(i+1,NUM_CITIES):
        distance = mathFunction.euclidean_distance(coordinates[i], coordinates[j])
        distance_matrix[i][j] = distance
        distance_matrix[j][i] = distance

#print("距離矩陣 (Distance Matrix):")
#print(np.round(distance_matrix, 2))

print(mathFunction.nearest_neighbor_tsp(cities,0))














    