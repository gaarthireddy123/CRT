d = {1:'a', 2:'b', 3:'c'} 
 
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(twosum([3,2,4], 6)) 
