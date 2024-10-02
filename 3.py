def product_of_digits(n):
    product = 1
    found_non_zero = False

    for digit in n:
        if digit != '0':
            product *= int(digit)
            found_non_zero = True

    if found_non_zero:
        return product
    else:
        return 0


t = int(input())
for _ in range(t):
    n = input().strip()
    print(product_of_digits(n))



