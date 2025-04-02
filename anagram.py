from collections import defaultdict

def anagram(words):
    anagrams = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        anagrams[key].append(word)

    anagram_groups = []
    single_words = []

    for group in anagrams.values():
        if len(group) > 1:
            anagram_groups.append(" ".join(sorted(group)))
        else:
            single_words.extend(group)

    for group in anagram_groups:
        print(group)

    for word in single_words:
        print(word)

input_file = "sample.txt"

with open(input_file, "r") as f:
    words = (line.strip() for line in f)
    anagram(words)