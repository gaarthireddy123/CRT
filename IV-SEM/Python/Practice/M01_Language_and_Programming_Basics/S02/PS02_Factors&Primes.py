'''Read a number from user and print all the factors of that number
input: 12
output: 1 2 3 4 6 12 


n=int(input("Enter a number: "))
for i in range(1,n//2+1):
    if n%i==0:
        print(i,end=" ")
print(n)

 Read a number from user count the number of factors and display the count

n=int(input())
counter = 0
for i in range(1,n//2+1):
    if n%i==0:
        counter+=1
print(counter+1)


Read a number from the user check whether the number is prime or not


n=int(input())
counter = 0
for i in range(1,n//2+1):
    if n%i==0:
        counter+=1 
if counter==1:
    print("Prime" if counter == 0 else "Not Prime")

'''
#Display all the prime numbers in the given range 

start = int(input())
end = int(input())
for num in range(start, end + 1):
    counter = 0
    for i in range(1, n// 2 + 1):
        if num % i == 0:
            counter += 1
    if counter == 0:
        print(n,end=" ")

#Factorial of a number

n=int(input())
if n < 0:
    print("no factorial for -ve")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    print(fact) 

#GCD of two numbers

a=int(input())
b=int(input())
while b:
    a, b = b, a % b
print(a)

import math
print(math.gcd(a,b))


