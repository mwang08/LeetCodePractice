# 27. Remove Element

def removeElement(nums, val):

    new_len = 0

    for i in range(len(nums)):

        if nums[i] != val:
            nums[new_len] = nums[i]
            new_len += 1

    return new_len
