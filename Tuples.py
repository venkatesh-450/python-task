#Tuples activity



#1) Write a program to swap the values of given tuples.
#t1 = ("A","B")
#t2 = (34,65)
t1=("A","B")
t2=(34,65)
print("Before Swap t1 :",t1)
print("Before Swap t2:",t2)
temp = t1
t1 = t2
t2 = temp
print("After Swap t1 :",t1)
print("After Swap t2 :",t2)


#2)wap to print the frequency of number accepted from the user in given tuple:
#T1 = (12,17,18,25,19,12,18,5)
#Enter any number : 12
T1 = (12,17,18,25,19,12,18,5)
num=int(input("enter any number:"))
print("frequency of number in tuple:",T1.count(num))

#3) wap to find maximum and minimum numbers in tuple


T = (12,17,18,25,19,85,18,5)
print("maximum number of T:",max(T))
print("minimum number of T:",min(T))


#4) wap to find second largest number in given tuple:
#T1 = (23,45,87,45,67,43,23,12)

#method 1:
T1 = (23,45,87,45,67,43,23,12)
T1= sorted(T1)
print(T1)
print("second largest is :" ,T1[-2])

#method 2:
T1 = (23,45,87,45,67,43,23,12)
print("Second largest element is:", sorted(T1)[-2])

#5) wap to find len of given tuple:
#T1 = (23,45,87,45,67,43,23,12)
T1 = (23,45,87,45,67,43,23,12)
print("length of T1:", len(T1))