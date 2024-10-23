import math

def euclidean_distance(v1, v2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(v1, v2)))

def manhattan_distance(v1, v2):
    return sum(abs(x - y) for x, y in zip(v1, v2))

def minkowski_distance(v1, v2, p=3):
    return sum(abs(x - y) ** p for x, y in zip(v1, v2)) ** (1 / p)

def jaccard_similarity(v1, v2):
    set_v1 = set(v1)
    set_v2 = set(v2)
    intersection = len(set_v1.intersection(set_v2))
    union = len(set_v1.union(set_v2))
    if union == 0:
        return 0
    return intersection / union

test_cases = int(input())

for _ in range(test_cases):
    metric = input().strip()
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    
    if len(v1) != len(v2):
        print("Invalid")
    else:
        if metric == "euclidean":
            result = euclidean_distance(v1, v2)
        elif metric == "manhattan":
            result = manhattan_distance(v1, v2)
        elif metric == "minkowski":
            result = minkowski_distance(v1, v2)
        elif metric == "jaccard":
            result = jaccard_similarity(v1, v2)
        else:
            result = None
        
        if result is not None:
            print(f"{result:.5f}")
        else:
            print("Invalid")
