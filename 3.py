def product_of_odd_position_digits(n):
    product = 1
    found_non_zero = False
    for i in range (len(n)):
        if i % 2 == 0:
            digit = int(n[i])
            if digit != 0:
                product *= digit
                found_non_zero = True
    return product if found_non_zero else 0
t = int(input())
results = []
for _ in range(t):
    N = input()
    result = product_of_odd_position_digits(N)
    results.append(result)
for result in results:
    print (result)


