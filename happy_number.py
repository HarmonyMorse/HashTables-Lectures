"""
Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false


Constraints:
1 <= n <= 231 - 1


U.P.E.R.:
Understand:
    Input - some number that's positive
    Output - boolean
    if n transforms to 1, return True
    if n returns to an already calculated number, return False
Plan:
    Recursion because we just delve into deeper and deeper repeated problems
    Base cases:
        n = 1 -> True
    Return False at some point here.
    If n is seen before, return False
    Else: recurse(new_n = sum_of_numbers_squared)
"""


def is_happy(n: int, cache = set()) -> bool:
    if n == 1:
        return True

    # if n was seen before, return False
    if n in cache:
        return False

    # Break into digits
    # -Turn n into a string
    # string_of_digits = str(n)
    # Square each digit -> digits_squared = [int(digit)**2 for digit in  string_of_digits]
    # Sum all the squares up -> sum(digits_squared)
    new_num = sum([int(digit)**2 for digit in str(n)])

    # Store new_sum into a cache
    # We now have "seen" this number before
    cache.add(n)
    print(cache)

    # Else, recurse
    return is_happy(new_num, cache)


# 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100
happy_num_1 = 23

# 2, 8, 15, 39, 50, 98
unhappy_num_1 = 98


print(is_happy(happy_num_1))

print(is_happy(unhappy_num_1))


"""
/Users/harm/Desktop/Dev/DataAlgs/HashTables/HashTables-Lectures/venv/bin/python /Users/harm/Desktop/Dev/DataAlgs/HashTables/HashTables-Lectures/happy_number.py 
{23}
{13, 23}
{10, 13, 23}
True
{98}
{145, 98}
{145, 98, 42}
{145, 98, 42, 20}
{98, 4, 42, 145, 20}
{98, 4, 42, 16, 145, 20}
{98, 4, 37, 42, 16, 145, 20}
{98, 4, 37, 42, 16, 145, 20, 58}
{98, 4, 37, 42, 16, 145, 20, 89, 58}
False
"""