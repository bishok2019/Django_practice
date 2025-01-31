# Greedy Method
# nums = [2,7,11,15]
# target = 9

# class Solution(object):
#     def twoSum(self, nums, target):

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)

## 2 Pointer method
# nums.sort()
# print(nums)
# left = 0
# right = len(nums)-1
# while left < right:
#     current_sum = nums[left] + nums[right]
#     if current_sum == target:
#         print('Pair found at:',[left], [right])
#         break
#     elif current_sum<target:
#         left+=1
#     else:
#         right-=1

# # Dict Method:
# def find_pair(nums, target):
#     num_and_index = {}
#     for i , num in enumerate(nums):
#         complement = target - num
#         if complement in num_and_index:
#             return[num_and_index[complement], i]
#         num_and_index[num] = i
#     return "no pair found"

# print(find_pair(nums, target))

# nums.sort()
# print(nums)
# left = 0
# right = len(nums) - 1
# pair_found = False

# while left < right:
#     current_sum = nums[left] + nums[right]
#     if current_sum == target:
#         print('Pair found at:', [left, right])
#         pair_found = True
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1

# if not pair_found:
#     print('No pair found')

# nums = [2,7,11,15]
# target = 18

# class Solution:
#     def twoSum(self, nums, target):
#         numAndIndex = {}
#         for i in range(len(nums)):
#             if target - nums[i] in numAndIndex:

#                 # print([numAndIndex[target - nums[i]], i])
#                 return [numAndIndex[target - nums[i]], i]
#             numAndIndex[nums[i]] = i
#         return []
    

# solution = Solution()
# result = solution.twoSum(nums, target)
# print(result)


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         compliment = target - nums[i]
#         if compliment in nums and nums.index(compliment)!=i:
#             print(f"Indices:{i}, {nums.index(compliment)}")
#             return [i, nums.index(compliment)]
#     else:
#         print("Not found")
    
# twoSum(nums, target)

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         compliment = target - nums[i]
#         if compliment in nums:
#             print(f"Indices:{i}, {nums.index(compliment)}")
#             return [i, nums.index(compliment)]
#     else:
#         print("Not found")
    
# twoSum(nums, target)

