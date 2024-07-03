nums = [1,2,0,1]
curr = 1
longest = 1
nums = set(nums)
nums.sort()
for i in range(len(nums) - 1):
    if (nums[i+1] - nums[i]) == 1:
        curr += 1
    else:
        longest = max(curr, longest)
        curr = 1
longest = max(curr, longest)
print(longest)        

