from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word.lower()))  # Case-insensitive grouping
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    words = input("Enter words separated by spaces: ").split()
    result = group_anagrams(words)

    print("\nGrouped anagrams:")
    for group in result:
        print(", ".join(group))
