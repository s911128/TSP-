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

def nearest_neighbor_tsp(matrix, start_node=0):
    route = [start_node]
    unvisited_cities = set(range(len(matrix))) # 尚未訪問的城市集合
    unvisited_cities.remove(start_node)
    k = start_node
    total_distance = 0.0
    while unvisited_cities:
        minimum = math.inf
        next_node = k
        for node in unvisited_cities:
            if minimum > matrix[k][node]:
                next_node = node
                minimum = matrix[k][node]
        k = next_node
        list.append(route, k)
        unvisited_cities.remove(k)
        total_distance = total_distance + minimum
        
    
    return route


    
