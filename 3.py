def product_of_digits(n):
    product = 1
    has_non_zero_digit = False

    for digit in n:
        if digit != '0':
            product *= int(digit)
            has_non_zero_digit = True

    if not has_non_zero_digit:
        return 0
    return product


def process_tests():
    t = int(input())
    for _ in range(t):
        n = input().strip()
        print(product_of_digits(n))


process_tests()
