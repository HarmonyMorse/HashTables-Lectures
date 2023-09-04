"""
Summary:
You're given strings `J` representing the types of stones that are jewels, and `S` representing the stones you *have*.
Each character in `S` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Examples
Input: J = "aA", S = "aAAbbbb"
Output: 3
-
Input: J = "z", S = "ZZ"
Output = 0

Notes:
`S` and `J` wll consist of letters and have a length of at most 50.
The characters in `J` are distinct.
All characters in `J` and `S` are letters.
Letters are case-sensitive: so stone `a` is considered a difference type of stone from `A`.


U.P.E.R.:
Understand:
    Return a number
    Input will be strings
    Return # of jewels
    Count how many times each character in J appears in S
Plan:
    Naive solution:
        for letter in J { for letter in S { check if J_letter == S_letter } } return count
Evaluate:
    Naive:
        We're going over S over and over
Repeat ;)




Hash the stones you have
Then go to the jewel stones, and see how many there are at the hash of each letter

for stone in stones:
    find hash
    get index
    increase counter at index
for jewel in jewels
    find hash
    get index
    add counter to final response counter
return final response counter
"""


def naive(J: str, S: str) -> int:  # O(n^2)
    count = 0

    for char_j in J:  # O(n)
        for char_s in S:  # O(n)
            if char_j == char_s:  # O(1)
                count += 1  # O(1)

    return count

"""
for stone in stones:
    find hash
    get index
    increase counter at index
for jewel in jewels
    find hash
    get index
    add counter to final response counter
return final response counter
"""

def with_hash(J: int, S: int):
    jewels_dict = {}
    count = 0

    for char_j in J:
        jewels_dict[char_j] = 0

    # for char_s in S:
    #     if char_s in jewels_dict:
    #         jewels_dict[char_s] += 1
    #
    # for v in jewels_dict.values():
    #     count += v

    # Even better:
    for char_s in S:
        if char_s in jewels_dict:
            count += 1

    return count


ex_1_j = "aA"
ex_1_s = "aAAbbbb"

ex_2_j = "ZZ"
ex_2_s = "z"

print(naive(ex_1_j, ex_1_s))
print(naive(ex_2_j, ex_2_s))

print(with_hash(ex_1_j, ex_1_s))
print(with_hash(ex_2_j, ex_2_s))
