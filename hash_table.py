
# INTRO

# I have a banana, what is the color?

# dictionary
#     O(n):
# {
#     apple: is green,
#     banana: is yellow,
#     tomato: is red,
#     egg: is white
#     ...
# }

# array
#     O(n):
# ["apple: is green", "banana: is yellow", "tomato: is red", "egg is white", ...]


# HASH

# ASCII and Unicode are two ways to hash

# Hash function:
#     a function that turns strings into numbers
#     must be deterministic (always output the same value for the same input)

def hash_fn(s):  # O(n) where n is len(s)
    encoded_string = s.encode()
    result = 0
    for byte_char in encoded_string:
        result += byte_char
    return result


# print(hash_fn("banana"))  # -> 609
# print(hash_fn("apple"))  # -> 530


hash_array = [None] * 8
# Let's map the result of hash_fn to an index in some array
# use modulo to bind the number from hash_fn to 0 -> length of the array
# 609 % 8 == the remainder of 609/8

# Store banana inside hash_array:
# hash_value = hash_fn("banana")
# index = hash_value % len(hash_array)
# hash_array[index] = ("banana", "banana is yellow")

# Store apple inside hash_array
# key: "apple", value: "apple is green"
# hash_value = hash_fn("apple")
# index = hash_value % len(hash_array)
# hash_array[index] = ("apple", "apple is green")

# Look up banana in hash_array
# O(n) where n is len("banana")

# Get the index value of banana
# hash_value = hash_fn("banana")  # 609
# index = hash_value % len(hash_array)

# print(hash_array[index])

# Hash function + array = hash table

# To insert a key and value to this hash_table
# - hash the key to convert it to a number
# - take that number and MOD it by the size of hash_table
# - insert the VALUE into the index given by the MOD operation on KEY
def insert_to_hash_table(key, value):
    hash_value = hash_fn(key)
    index = hash_value % len(hash_array)
    print(f'{key} hashed to {hash_value} which is index {index}')
    hash_array[index] = (key, value)

# To retrieve a value given a specific key from hash_table
# - hash the key to convert it to a number
# - use MOD to find the index within the underlying array
# - use this new index to find the value in the array
def get_from_hash_table(key):
    hash_value = hash_fn(key)
    index = hash_value % len(hash_array) # convert the number into a new number between 0 - len(array)
    return hash_array[index]

insert_to_hash_table("banana", "banana is yellow")
insert_to_hash_table("apple", "apple is green")
insert_to_hash_table("tomato", "tomato is red")
insert_to_hash_table("eggg", "this will replace apple")
insert_to_hash_table("egg", "egg is white")

print(hash_array)

print(f'banana: {get_from_hash_table("banana")}')
print(f'apple: {get_from_hash_table("apple")}')
print(f'tomato: {get_from_hash_table("tomato")}')
print(f'eggg: {get_from_hash_table("eggg")}')
print(f'egg: {get_from_hash_table("egg")}')