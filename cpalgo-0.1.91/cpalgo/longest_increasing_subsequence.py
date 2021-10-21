import bisect
def longest_increasing_subsequence(nums):
    dp = []
    for num in nums:
        i = bisect.bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp) 