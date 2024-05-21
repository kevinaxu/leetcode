from typing import List
class Solution:

    # Find the max sum subarray of fixed size k 
    def maxSumSubarray(self, arr: List[int], k: int) -> int:

        max_sum = 0 
        for start in range(len(arr)-k+1):            # len = 10, k = 2, start should terminate at 7-9
            end = start + k
            curr_sum = sum(arr[start:end])
            max_sum = max(max_sum, curr_sum)
            # print(f"start: {start}, subarr: {arr[start:end]}, curr_sum: {curr_sum}")
        return max_sum


arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(Solution().maxSumSubarray(arr, 2))



    