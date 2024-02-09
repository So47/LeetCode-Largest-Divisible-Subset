class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)

        maxIndex = 0  # To find the largest subset
        prevIndex = [-1] * n  # To track the previous index

        # sort nums to find divisible pairs to make sure a comes before b so it divides it
        nums.sort()

        # Initialize DP array
        dp = [1] * n

        # Build the DP array
        for i in range(1, n):
            # ensures that each element nums[i] is only compared with its predecessors 
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]: # to ensure that we only update the length of the largest divisible subset ending 
                    dp[i] = dp[j] + 1
                    prevIndex[i] = j

                    if dp[i] > dp[maxIndex]:
                        maxIndex = i

        # Reconstruct the subset
        while maxIndex >=0:
            answer.append(nums[maxIndex])
            maxIndex = prevIndex[maxIndex]


        return answer
