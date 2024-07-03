nums = [0,3,7,2,5,8,4,6,0,1]
curr = 1
longest = 1
nums.sort()
for i in range(len(nums) - 1):
    if (nums[i+1] - nums[i]) == 1:
        curr += 1
    else:
        longest = max(curr, longest)
longest = max(curr, longest)
print(longest)        

