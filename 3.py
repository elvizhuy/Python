def product_of_digits(n):
    product = 1
    has_non_zero_digit = False

    for digit in n:
        if digit != '0':
            product *= int(digit)
            has_non_zero_digit = True

    if has_non_zero_digit:
        return product
    else:
        return 0


def process_tests():
    t = int(input())
    for _ in range(t):
        n = input().strip()  # Đọc số N dưới dạng chuỗi
        print(product_of_digits(n))


# Test case
process_tests()
