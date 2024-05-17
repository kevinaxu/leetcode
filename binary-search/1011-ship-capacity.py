class Solution:
    def shipWithinDays(self, weights, days):
        def feasible(capacity):
            shippingDays = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight 
                    shippingDays += 1
            return shippingDays <= days

        # # CONDITION
        # def feasible(capacity):
        #     shippingDays = 0
        #     total = 0

        #     for weight in weights:
        #         total += weight

        #         if total == capacity:
        #             shippingDays += 1
        #             total = 0
        #             continue

        #         if total > capacity:        # over capacity, 
        #             shippingDays += 1
        #             total = weight

        #     if total > 0:
        #         shippingDays += 1

        #     # print(f"shipping days: {shippingDays}")
        #     return shippingDays <= days

        # BOUNDS
        left = max(weights)
        right = sum(weights)

        # BINARY SEARCH TEMPLATE
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else: 
                left = mid + 1
        return left


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

def feasible(capacity):
    shippingDays = 1            # STARTS AT 1! 
    total = 0
    for weight in weights:
        total += weight
        if total > capacity:
            total = weight 
            shippingDays += 1
    print(f"total: {total}")
    return shippingDays
print(feasible(15))



# print(Solution().shipWithinDays(weights, days))



# capacity = 10     shippingDays = 7        > 5 so False 
# (1, 2, 3, 4)
# (5)
# (6)
# (7)
# (8)
# (9)
# (10)

# feasible(2) won't work - you cannot ship weight that's greater than capacity!
# therefore, capacity will need to start at max(weights)



