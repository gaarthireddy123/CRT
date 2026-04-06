'''
Find the largest number (using max())
'''
a =[10,20,87,15,98,12,3,2,45]
print(max(a)) 
s=input("Enter a string: ") 
if s == "".join(reversed(s)):
    print("Palindrome")

a=[10,20,87,15,98,12,3,2,45]
res=list(filter(lambda x: x%2==0, a))
print(res)  
print(len(res))

#Remove duplicates (using set())
a=[10,20,87,15,98,12,3,2,45,10,20]
print(set(a)) 

# Sum of Digits (using sum())
n=12345
res=sum(int(digit) for digit in str(n))
print(res)

#Sort Words Alphabetically (using sorted())
a=["banana", "apple", "cherry", "date"]
print(sorted(a))

#Find Common Elements (using set())
a=[10,20,30,40,50]
b=[30,40,50,60,70]
print(set(a) & set(b))
print(res)
print(tuple(res)) 

#Index with value (using enumerate())
a=["banana", "apple", "cherry", "date"]
for i, value in enumerate(a):
    print(f"Index: {i}, Value: {value}")

#Pair Two Lists (using zip())
a=[1,23,45,6,7]
b=[2,8,5,9,10]
print(zip(a,b))
#Find the Second Largest Number (using sorted())
b=[2,8,5,9,4,5]
b.sort()
print(b[-2])
