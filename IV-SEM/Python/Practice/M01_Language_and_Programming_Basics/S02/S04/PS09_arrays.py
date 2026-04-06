import numpy as np 
a=np.array([ 1,2,3,4,5])
print("Array elements are:",a)

print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.sum(a))
print(np.zeros(5))
print(np.ones(5))
print("Even numbers are:",np.arange(2,10,2))
print("Odd numbers are:",np.arange(1,3,7))

n=int(input("Enter size of array:"))
ele=list(map(int,input("Enter elements:").split()))
print("Array elements are:",np.array(ele))