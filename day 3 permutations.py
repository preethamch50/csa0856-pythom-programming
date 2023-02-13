#Given a collection of numbers, nums, that might contain duplicates,
#return all possible unique permutations in any order. 
Program:

def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [1,1,2]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))

#Output:
Input: nums = [1,1,2] 
Output: 
[[1,1,2], 
[1,2,1], 
[2,1,1]] 
