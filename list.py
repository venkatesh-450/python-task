#Create a List:
a = ["apple", "banana", "cherry"]
print(a)
#Lists allow duplicate values
a = ["apple","apple", "banana", "cherry","cherry"]
print(a)
#Print the number of items in the list:
a = ["apple", "banana", "cherry"]
print(len(a))
#String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
#What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))





thislist = ["apple", "banana", "cherry","venky"]
thislist[1:3] = ["watermelon","sai"]
print(thislist)

#1. Create a empty list & add elements into the list.
#-----usingfor loop - -----
  #  solution:
a = []
for i in range(10):
    a.append(i)
print("list:")
#a)----without using loop - ---
#solution:
a1 = []
a1.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("list:", a1)

#2.Program to Create two lists with EVEN numbers and ODD numbers from a list(in this program i want to see append method will used)
#Input: List1 = [11, 22, 33, 44, 55]
# Output:
   # List with EVEN numbers: [22, 44]
   #List with ODD NUMBERS: [11, 33, 55]
list1 = [11, 22, 33, 44, 55]
listOdd = []
listEven = []
for num in list1:
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)
print("list1:    ", list1)
print("List with EVEN numbers: ", listEven)
print("List with ODD numbers:  ", listOdd)


#3.Program to sort the elements of given list in Ascending and Descending Order(separately)

'''input:
a= [10, 30, 40, 20, 50]
b= [10.23, 10.12, 20.45, 11.00, 0.1]
str = ["Banana", "Cat", "Apple", "Dog", "Fish"]'''

#-------ascending order:

a= [10, 30, 40, 20, 50]
a.sort()
print(a)
b= [10.23, 10.12, 20.45, 11.00, 0.1]
b.sort()
print(b)
str = ["Banana", "Cat", "Apple", "Dog", "Fish"]
str.sort()
print(str)
#------descending order:
a= [10, 30, 40, 20, 50]
a.sort(reverse=True)
print(a)
b= [10.23, 10.12, 20.45, 11.00, 0.1]
b.sort(reverse=True)
print(b)
str = ["Banana", "Cat", "Apple", "Dog", "Fish"]
str.sort(reverse=True)
print(str)


'''List1 = [äpples ,"bananas", ""pineapples""]
Shopping list = [ apples, apples, bananas, apples, pear, pineapples, pear, apples,banana]
count the no.of times list1 elements are present in ShoppingList
ex: apples ==> 4 times in ShoppingList'''

list1 = ["apples" ,"bananas", "pineapples"]
shoppinglist = [" apples"," apples", "bananas", "apples", "pear", "pineapples","pear", "apples","banana"]

for i in list1:
    count=0
    for j in shoppinglist:
        if i==j:
            count=count+1
           # print(i)
    print(i,":",count)

animals=["dog","cat","elephant"]
animals.append("peacock")
print(animals)





a='hello world'[::-1]
print(a)
