# Given a string, can we figure out how many times each letter appears in it?

def letter_count(s):
    # Dict where keys are letters and values will be an incrementing counter
    d = {}
    for char in s:
        if char.isspace():
            continue
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1

    return d


print(letter_count("aaabbc"))
print(letter_count("Hello!"))
print(letter_count("The quick brown fox jumps over the lazy dog"))


def double_letter(s):
    d = set()
    # store letters as keys and a counter as value
    # find all letters where value > 1
    for char in s:
        if char.isspace():
            continue
        if char not in d:
            d.add(char)
        else:
            return char
    # for key.value in d.items():
    #     if value == 2:
    #         return key
    print(d)


print(double_letter("abcdeef"))