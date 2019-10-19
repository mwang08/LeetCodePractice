# 53. Maximum Subarray


# 1. Brutal Force
# 2. dynamic programming
# So I change the format of the sub problem into something like:
# maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] which must has A[i] as the end element.

def maxSubArray(nums):

    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], nums[i])
    return max(nums)


maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


