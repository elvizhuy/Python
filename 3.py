def product_of_digits(n):
    product = 1
    found_non_zero = False

    for digit in n:
        if digit != '0':
            product *= int(digit)
            found_non_zero = True

    if not found_non_zero:
        return 0
    return product


def process_tests():
    t = int(input())
    for _ in range(t):
        n = input().strip()
        print(product_of_digits(n))


process_tests()

