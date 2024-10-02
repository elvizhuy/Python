def is_increasing_decreasing(s):
    n = len(s)

    # Phải có đúng 8 ký tự
    if n != 8:
        return "NO"

    found_decreasing_point = False
    for i in range(1, n):
        if s[i] < s[i - 1]:
            found_decreasing_point = True
        elif found_decreasing_point and s[i] <= s[i - 1]:
            return "NO"

    if found_decreasing_point:
        return "YES"
    else:
        return "NO"


def process_tests():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(is_increasing_decreasing(s))


# Test case
process_tests()
