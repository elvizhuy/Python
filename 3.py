import math

def euclidean(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def manhattan(v1, v2):
    return sum(abs(a - b) for a, b in zip(v1, v2))

# Input handling
test_cases = int(input())

for _ in range(test_cases):
    distance_type = input().strip()
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    
    if len(v1) != len(v2):
        print("Invalid")
    else:
        if distance_type == "euclidean":
            print(f"{euclidean(v1, v2):.5f}")
        elif distance_type == "manhattan":
            print(f"{manhattan(v1, v2):.5f}")
        else:
            print("Invalid")
