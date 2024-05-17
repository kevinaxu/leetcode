class Solution:
    def searchMatrix(self, matrix, target):
        firstCol = [row[0] for row in matrix]
        rowIdx = self.binarySearch(firstCol, target)
        colIdx = self.binarySearch(matrix[rowIdx], target)        
        return matrix[rowIdx][colIdx] == target

    def binarySearch(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > target:
                right = mid
            else: 
                left = mid + 1
        return left - 1



# arr = [1, 3, 5, 10]
# target = 10
# print(Solution().binarySearch(arr, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 12
print(Solution().searchMatrix(matrix, target))