# Input handling
test_cases = int(input())

for _ in range(test_cases):
    N = input().strip()
    if N[:2] == N[-1:-3:-1]:
        print("YES")
    else:
        print("NO")
