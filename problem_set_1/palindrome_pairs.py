def is_palindrome(s):
    return s == s[::-1]

def palindrome_pairs(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                if is_palindrome(words[i] + words[j]):
                    result.append([i, j])
    return result

input_words = ["bat", "tab", "cat"]
one_output_sample = ["batt", "tab", "cat"]
no_output_sample = ["pancit", "canton", "with", "egg"]
multiple_output_sample = ["race", "car", "ecar"]

result = palindrome_pairs(input_words)
print(result)