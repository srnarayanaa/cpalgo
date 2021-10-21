def maximum_product_subarray(nums):
    i = 0
    currentMax, currentMin, ans = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        tmp = currentMax
        currentMax = max(n, n*currentMax, n*currentMin)
        currentMin = min(n, n*tmp, n*currentMin)
        ans = max(ans, currentMax)
    return ans