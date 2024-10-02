def read_words(lines):
    words_set = set()
    for line in lines:
        words = line.split()
        for word in words:
            words_set.add(word.lower())
    return words_set
n=int(input())
group1_lines = [input() for _ in range(n)]
m=int(input())
group2_lines = [input() for _ in range(m)]
group1_words = read_words(group1_lines)
group2_words = read_words(group2_lines)
only_in_group1 = sorted(group1_words - group2_words)
only_in_group2 = sorted(group2_words - group1_words)
print(" ".join(only_in_group1))
print(" ".join(only_in_group2))