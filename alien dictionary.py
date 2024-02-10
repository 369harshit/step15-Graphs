from itertools import permutations

def is_valid_order(order, words):
    order_dict = {}
    for idx, char in enumerate(order):
        order_dict[char] = idx
        
        
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)

        for j in range(min_len):
            if word1[j] != word2[j]:
                if order_dict[word1[j]] > order_dict[word2[j]]:
                    return False
                break

    return True

def alienOrder(N, dict):
    characters = set("".join(dict))
    all_permutations = permutations(characters)

    for order in all_permutations:
        order_str = "".join(order)
        if is_valid_order(order_str, dict):
            return order_str

    return ""

# Example usage:
N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]

output = alienOrder(N, dict)
print(output)
