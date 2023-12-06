#Create a dictionary representing a person's information (name, age, city), and then print each item individually.
person={
    "name":"richa",
    "age": 30,
    "city" : "amsterdam"
}
#Given a list of names, count the occurrences of each name and store the result in a dictionary.
names= ["cat", "cat" , "dog","bird", "horse", "horse","dog","cat"]
 
nameDic1 ={}

for name in names:
    if  nameDic1.get(name):
         nameDic1[name]= nameDic1.get(name)+1
    else:
         nameDic1[name]=1   
print( nameDic1)

#Given a dictionary of students and their test scores, calculate and print the average score.
person={
    "n1":101.4,
    "n2": 30,
    "n3" : 100.6,
    "n4":100,
    "n5": 30,
    "n6" : 20.2
}

max_values = max(person.values())
print(max_values)

#Write a function that takes a sentence as input and returns a dictionary with the count of each word.



def convert (sentence):
    nameDic={}
    for letter in sentence:
      if nameDic.get(letter):
        nameDic[letter]=nameDic.get(letter)+1
      else:
        nameDic[letter]=1   
    return nameDic

print(convert("helloooo world this is great"))       

#Given two dictionaries, merge them into a single dictionary. If a key exists in both dictionaries, sum the values
obj1={
    "n1":101.4,
    "n2": 30,
    "n3" : 100.6,
}
obj2={
    "n2": 30,
    "n4":100,
    "n5": 30,
    "n6" : 20.2
}

new_obj={}

for key,value in obj1.items():
   if new_obj.get(key):
      new_obj[key] =new_obj.get(key)+ value
   else :
      new_obj[key]= value

for key,value in obj2.items():
   if new_obj.get(key):
      new_obj[key] =new_obj.get(key)+ value
   else :
      new_obj[key]= value      

print(new_obj)      


#Given a dictionary of students and their test scores, calculate and print the average score.

marks={
    "n1":101.4,
    "n2": 30,
    "n3" : 100.6,
}
total=0
for keys in marks:
   total=total+marks[keys]
length=len(marks) 

print(total/length)

