import math

# Inverse square root is 1 / square root of number
# Relatively time consuming
def get_inverse_square(num):
    ans = 1 / math.sqrt(num)
    print(ans)
    return ans

# We need to constantly get the inverse square roots of numbers between 1 and 1000

get_inverse_square(500)


# What should our lookup table look like?
# Keys will be numbers
# Value will be results of get_inverse_square

def build_lookup_table():
    lookup_table = {}
    for i in range(1, 1000):
        lookup_table[i] = get_inverse_square(i)
    return lookup_table


sqrt_lookup_table = build_lookup_table()

print(f'inverse square of 3 is {sqrt_lookup_table[3]}')
print(f'inverse square of 82 is {sqrt_lookup_table[82]}')
print(f'inverse square of 234 is {sqrt_lookup_table[234]}')
print(f'inverse square of 1 is {sqrt_lookup_table[1]}')
print(f'inverse square of 999 is {sqrt_lookup_table[999]}')
print(f'inverse square of 4 is {sqrt_lookup_table[4]}')
