def check_lucky_number(n):
    count_3 = str(n).count('3')
    count_5 = str(n).count('5')
    if count_3 + count_5 == 3 or count_3 + count_5 == 5:
        return "YES"
    return "NO"

# Test case
n = int(input())
print(check_lucky_number(n))
