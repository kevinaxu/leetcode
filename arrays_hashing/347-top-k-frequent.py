from collections import defaultdict
from collections import Counter
import heapq

class Solution:

    def topKFrequent(self, nums, k):
        # Count the frequency of each element
        counts = defaultdict(int)
        for n in nums: counts[n] += 1
        
        # Create a min-heap to store the top k elements
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract the top k frequent elements from the heap
        top_k = [elem for count, elem in heap]
        return top_k


    '''
    # Do this with Heap 
    def topKFrequent(self, nums, k):
        dd = defaultdict(int)
        bucket = [[] for i in range(len(nums)+1)]

        for n in nums:
            dd[n] += 1
        for key, count in dd.items():
            bucket[count].append(key)

        print(bucket)
        
        return []
    '''


    '''
    # neetcode implementation - similar except for building the results 
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums+1))]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):     # REVERSE RANGE LOOP SYNTAX
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
    '''



    '''
    def topKFrequent(self, nums, k):

        # create dict that maps {n: #occurences}
        dd = defaultdict(int)
        for n in nums: dd[n] += 1

        # build an array for bin sort
        # initialize values as empty list  
        # bucket = [[]] * (len(nums)+1)               # WRONG WAY OF INITIALIZING LISTS
        bucket = [[] for i in range(len(nums)+1)]

        # fill: bucket[count] = [3, 2, 1]
        for key, count in dd.items():
            bucket[count].append(key)

        # get the top k counts
        result = []
        for ls in reversed(bucket):
            if k == 0: break
            if ls:
                result = result + ls                  # THIS IS BUGGY - what if elements all have the same count? 
                k -= len(ls)
        return result
    '''


nums = [7,7,7,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))
