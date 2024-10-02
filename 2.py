def is_increasing_decreasing(s):
    n = len(s)
    if n != 8:
        return "NO"

    i = 1

    while i < n and s[i] < s[i - 1]:
        i += 1


    while i < n and s[i] > s[i - 1]:
        i += 1


    if i == n:
        return "YES"
    else:
        return "NO"


def process_tests():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        print(is_increasing_decreasing(s))



process_tests()

