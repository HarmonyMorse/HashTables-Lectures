records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Sarah", "Sales"),
    ("Pranjal", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing"),
    ("Charles", "Marketing"),
    ("Brian", "Marketing"),
    ("Jordan", "Marketing"),
]


# Proposed dictionary:
# Keys will be departments
# values will be arrays of names
def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record

        # if department is already in list
        if dept in index:
            # add name to list
            index[dept].append(name)
        else:  # else create new key with list with the name in it
            index[dept] = [name]

    return index


department_index = build_index(records)

# Print all the departments
print(department_index.keys())

# Print everyone in Engineering - O(1)
print(department_index['Engineering'])

# Print everyone in Sales - O(1)
print(department_index['Sales'])
