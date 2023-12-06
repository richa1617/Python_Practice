
student = {
    "name": "Alice",  # if keys are string use ""
    "graduated": False,
    "married": False,
    "age": 23,
    "hobbies": ["Jogging", "Gym", "Boxing"]
}




student["name"] ="Richa"
print(student)
#print(student["school"])
print(student.get("school"))
print(student.keys()) # dict_keys(['name', 'graduated', 'married', 'age', 'hobbies'])
#print (student.items())
#dict_items([('name', 'Alice'), ('graduated', False), ('married', False), ('age', 23), ('hobbies', ['Jogging', 'Gym', 'Boxing'])])

print(len(student))

person =["richa", "akash", "aman", "su"]

dic= dict.fromkeys(person)
print(dic) #{'richa': None, 'akash': None, 'aman': None, 'su': None}

dic2= dict.fromkeys(person,1)
print(dic2) #{'richa': 1, 'akash': 1, 'aman': 1, 'su': 1}

nums = [1, 2, 3, 4, 5, 6, 7, 8]

numDic={}

for num in nums:
    numDic[num]=str(num)

print(numDic)
