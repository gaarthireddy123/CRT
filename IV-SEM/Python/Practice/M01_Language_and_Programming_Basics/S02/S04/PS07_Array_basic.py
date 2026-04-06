import array
arr = array.array('i',[12,45,78])
print(arr,type(arr))
arr.append(10)
arr.append(20)
print(arr)
arr.append(12)


List:
1.use [] to create a list
2.List is Mutable
3.List allows duplicate values
4.List is heterogeneous
5.List is indexed 

list =[12,25.4,6+5j,"hello"]
print(list,type(list))
print(list[3])
print(list[3:6:1])
print(list[::-1])
list.append(100)
print(list)
list.insert(2,"world")
print(list)

n=int(input())