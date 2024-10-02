def product_of_digits(n):
    product = 1
    for digit in str(n):
        if digit != '0':
            product *= int(digit)
    return product

def process_tests():
    t = int(input())
    for _ in range(t):
        n = input().strip()
        print(product_of_digits(n))

# Test case
process_tests()
