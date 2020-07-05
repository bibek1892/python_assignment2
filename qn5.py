#5. Create a tuple with your first name, last name, and age. Create a list,
#people, and append your tuple to it. Make more tuples with the
#corresponding information from your friends and append them to the
#list. Sort the list. When you learn about sort method, you can use the
#key parameter to sort by any field in the tuple, first name, last name,
#or age.

tuple_1 = ('Bibek', 'Khatiwada', 22)
list_people = []
list_people.append(tuple_1)
#print(list_people)
tuple_2 = ('Saroj', 'Khatiwada', 22)
tuple_3 = ('Basbin', 'Wagle', 25)
tuple_4 = ('Ashok', 'Dahal', 24)
list_people.append(tuple_2)
list_people.append(tuple_3)
list_people.append(tuple_4)
sorted_list_people= sorted(list_people, key=lambda x: x[2] )
print(list_people)
print(sorted_list_people)
