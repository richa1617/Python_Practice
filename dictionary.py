
student = {
    "name": "Alice",  # if keys are string use ""
    "graduated": False,
    "married": False,
    "age": 23,
    "hobbies": ["Jogging", "Gym", "Boxing"]
}

# Access an entry
#print(student["age"])
# print(student.name) doesnt work

mixed_dictionary = {
    (0, 0): "Origin",
    1000: "A thousand",
    3.141: "Pi",
    True: "This is stupid",
    print: "A function for logging to console",
    "Why": "I dont know"
}

"""for keys in mixed_dictionary:
    print(keys)"""
"""
print(True in mixed_dictionary)    
print("Why" in mixed_dictionary)  
print("X" in mixed_dictionary)  
"""


# Printing the items of the dictionary
items = mixed_dictionary.items()
print(items)

# Printing the keys of the dictionary
keys = mixed_dictionary.keys()
print(keys)