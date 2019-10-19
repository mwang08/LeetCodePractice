# 26. Remove Duplicates from Sorted Array

def removeDuplicates(nums):

    new_len = 1
    if len(nums) == 0:
        return 0
    else:
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[new_len] = nums[i]
                new_len += 1
    return new_len


removeDuplicates([1,2,3,3,3,4,5,6,6])