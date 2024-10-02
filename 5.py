def process_text_group():
    n = int(input())
    group_1_words = set()
    for _ in range(n):
        group_1_words.update(input().split())

    m = int(input())
    group_2_words = set()
    for _ in range(m):
        group_2_words.update(input().split())

    only_in_group_1 = sorted(group_1_words - group_2_words)
    only_in_group_2 = sorted(group_2_words - group_1_words)

    print(' '.join(only_in_group_1))
    print(' '.join(only_in_group_2))


process_text_group()

