def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement  = target - num 
        if complement in seen:
                return [seen[complement], i]
        seen[num] = i
    return []
            
print(twoSum([1, 2, 3, 4, 5, 6], 9))