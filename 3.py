def product_of_digits(n):
    product = 1
    has_non_zero_digit = False

    for digit in n:
        if digit != '0':
            product *= int(digit)
            has_non_zero_digit = True

    # Nếu không có chữ số khác 0, trả về 0
    if not has_non_zero_digit:
        return 0
    return product


def process_tests():
    t = int(input())  # Số bộ test
    for _ in range(t):
        n = input().strip()  # Đọc số N dưới dạng chuỗi
        print(product_of_digits(n))


# Test case
process_tests()

