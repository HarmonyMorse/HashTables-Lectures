hash_table = [None] * 8  # 8 slots, all initialized to None


def my_hash(s):  # gets the hash
    # Take every character in the string, and convert character to number
    # Convert each character into UTF-8 numbers
    string_utf = s.encode()

    total = 0
    for char in string_utf:
        total += char
        total &= 0xffffffff  # limit total to 32 bits
    return total


def hash_index(key):  # gets the index
    hash_num = my_hash(key)
    return hash_num % len(hash_table)


def put(key, val):
    # Hash the key and get an index
    i = hash_index(key)
    # Find the start of the linked list using the index
    # IF the key already exists in the linked list
    #     Replace the value
    # Else
    #     Add new HashTableEntry to the head of the linked list


def get(key):
    # Hash the key and get an index
    i = hash_index(key)
    # Get the linked list AT computet index
    # Search through the linked list for the key
    #     Compare keys until you find the right one
    # If it exists, return the value
    # Else, return None


def delete(key):
    # Hash the key and get an index
    i = hash_index(key)
    # Search through the linked list for the matching key
    # Delete that node
    # Return value of the deleted node


def resize():  # when load factor (# of items / # of slots) is over 0.7
    # Make a new_array that's DOUBLE the current size
    # Go through each linked list in the array
    #     Go through each item and re-hash it with % len(new_array)
    #     Insert the items into their new locations

    print("hello")


def shrink():  # when load factor (# of items / # of slots) is under 0.2
    # Make a new_array that's HALF the current size
    # Go through each linked list in the array
    #     Go through each item and re-hash it with % len(new_array)
    #     Insert the items into their new locations

    print("hello")



put("Hello", "Hello Value")
put("World", "World Value")
print(hash_table)

put("foo", "Foo Value")
print(hash_table)

value = get("Hello")
print(f'Hello value: {value}')

value = get("foo")
print(f'foo value: {value}')