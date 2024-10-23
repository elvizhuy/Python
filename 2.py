def digit_product(n):
    product = 1
    for digit in str(n):
        if digit != '0':
            product *= int(digit)
    return product

test_cases = int(input())

for _ in range(test_cases):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(key=lambda x: (digit_product(x), x))
    print(*A)
