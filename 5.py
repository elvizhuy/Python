def process_text_group():
    n = int(input())
    group_1 = set()
    for _ in range(n):
        group_1.update(input().split())

    m = int(input())
    group_2 = set()
    for _ in range(m):
        group_2.update(input().split())

    diff_1_2 = sorted(group_1 - group_2)
    diff_2_1 = sorted(group_2 - group_1)

    print(' '.join(diff_1_2))
    print(' '.join(diff_2_1))

# Test case
process_text_group()
