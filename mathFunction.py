import math

def euclidean_distance(x1, x2):
    try:
        norm = len(x1)
        sum_of_squre = 0
        for i in range(norm):
            sum_of_squre = sum_of_squre + math.pow(x1[i]-x2[i],2)

        return math.sqrt(sum_of_squre)

    except Exception as e:
        print("兩點範數不同")

def nearest_neighbor_tsp(matrix, start_node):
    route = [start_node]
    not_visited_cities = [1,2,3]
    k = start_node
    while len(route) < 4:
        next_node = not_visited_cities[0]
        minimum = matrix[k][next_node]
        for i in range(len(not_visited_cities)):
            if minimum > matrix[k][not_visited_cities[i]]:
                next_node = not_visited_cities[i]
                minimum = matrix[k][next_node]
        k = next_node

        list.append(route, k)
        list.remove(not_visited_cities,k)
        
    
    return route


    
