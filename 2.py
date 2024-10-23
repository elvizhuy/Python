def digit_product(n):
    product = 1
    has_non_zero_digit = False
    for digit in str(n):
        if digit != '0':
            product *= int(digit)
            has_non_zero_digit = True
    return product if has_non_zero_digit else 0

test_cases = int(input())

for _ in range(test_cases):
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort(key=lambda x: (digit_product(x), x))
    
    print(*A)
