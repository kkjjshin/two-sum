def twoSum(nums: list[int], target: int) -> list[int]:
    ans = []
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                ans.append(i)
                ans.append(j)
    return ans

