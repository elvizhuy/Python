def odd_position_digit_product(num):
    num_str = str(num)
    product = 1
    has_non_zero_digit = False
    for i in range(0, len(num_str), 2):
        digit = int(num_str[i])
        if digit != 0:
            product *= digit
            has_non_zero_digit = True
    return product if has_non_zero_digit else 1

test_cases = int(input())

for _ in range(test_cases):
    N = int(input())
    A = list(map(int, input().split()))
    
    A.sort(key=lambda x: (odd_position_digit_product(x), x))
    
    print(*A)
