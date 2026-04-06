'''N=int(input("Enter a number:"))
count=0
while N>0:
    count+=1
    N=N//10
print(count)
print(len(str(N)))

N=int(input())
s=0
while N>0:
    N//=10
print(s)

print(sum(map(int,str(temp))))

N=int(input())
even = odd = 0
while N >0:
    if (N % 2) == 0:
        even += 1
    else:
        odd += 1
    N //= 10
print(even,odd)
'''
n = int(input())
while n > 9:
    n = sum(map(int, str(n)))
print(n)



