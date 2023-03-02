#Sets are written with curly brackets{}.
a = {"apple", "banana", "cherry"}
print(a)







#1.Write a Python program to remove an item from a set if it is present in the set.
set1 = {"a", "b", "c","d"}
print("b" in set1)
set1.discard("b")
print(set1)


#2. wap to join two or more sets in Python program.
#for join two
a = {"a", "b" , "c"}
b = {1, 2, 3}
a.update(b)
print(a)

#for join two(union)
a = {"a", "b" , "c"}
b = {1, 2, 3}
c= a.union(b)
print(c)

#3. wap To remove an item in a set
a = {"Bangalore", "Hyderabad", "pune"}
a.remove("Hyderabad")
print(a)
