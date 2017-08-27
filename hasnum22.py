def has22(nums):
    if len(nums) <=1 :
        return False
    if nums[0] != nums[1]:
        return has22(nums[1:])
    return nums[0] == nums[1]
print(has22([1,2,1,2,3,3]))
