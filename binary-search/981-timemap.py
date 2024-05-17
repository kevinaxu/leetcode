class TimeMap:

    def __init__(self):
        '''
        {
            "foo": {
                1: "bar",
                4: "bar2"
            }
        }
        '''
        self.dict = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = {timestamp: value}
        else:
            self.dict[key][timestamp] = value

    def binarySearch(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left-1

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""

        values = list(self.dict[key].keys())
        idx = self.binarySearch(values, timestamp)
        if idx == -1:
            return ""
        return self.dict[key][values[idx]]



    def print(self) -> None:
        print(self.dict)
        

# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

db = TimeMap()
db.set("love", "high", 10)
db.set("love", "low", 20)
db.print()


print(db.get("love", 5))       # "" 
# print(db.get("love", 10))      # high
# print(db.get("love", 15))      # high 
# print(db.get("love", 20))      # low
# print(db.get("love", 25))      # low


# db.set("foo", "bar3", 7)
# db.print()
# print(db.get("foo", 5))

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

