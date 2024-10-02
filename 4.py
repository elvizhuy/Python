import math

def euclidean_distance(vec1, vec2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(vec1, vec2)))

def dot_product(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec2))

def process_tests():
    t = int(input())
    for _ in range(t):
        vec1 = list(map(int, input().split()))
        vec2 = list(map(int, input().split()))
        distance = euclidean_distance(vec1, vec2)
        dot_prod = dot_product(vec1, vec2)
        print(f"{distance:.2f} {dot_prod}")

# Test case
process_tests()
