def is_increasing_decreasing(s):
    n = len(s)
    for i in range(1, n):
        if s[i] > s[i - 1]:
            break
    else:
        return False
    for j in range(i, n):
        if s[j] <= s[j - 1]:
            return False
    return True

def process_tests():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        if is_increasing_decreasing(s):
            print("YES")
        else:
            print("NO")

# Test case
process_tests()
