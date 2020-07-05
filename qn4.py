#Create a list. Append the names of your colleagues and friends to it.
#Has the id of the list changed? Sort the list. What is the first item on
#the list? What is the second item on the list?

lsts = []
size=int(input("Enter the no. of friend list you want to add:"))

for items in range(size):
    name=input("Enter the name:")
    lsts.append(name)

print(lsts)

lsts.sort()
#A=[''.join (sorted(word)) for word in lsts]

print(lsts)


print(f'first item {lsts[0]} and second item {lsts[1]}')

