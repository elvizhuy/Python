test_cases = int(input())

for _ in range(test_cases):
    N = input().strip()
    first_two = N[:2]  
    last_two = N[-2:]  
    if first_two == last_two[::-1]:  
        print("YES")
    else:
        print("NO")
