nums = [9,1,4,7,3,-1,0,5,8,-1,6]
curr = 1
longest = 1
nums.sort()
for i in range(len(nums) - 1):
    if (nums[i+1] - nums[i]) == 1:
        curr += 1
    else:
        longest = max(curr, longest)
        curr = 1
longest = max(curr, longest)
print(longest)        

