class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Find the maximum cost
        max_cost = max(costs)

        # Count frequency of each cost
        count = [0] * (max_cost + 1)
        for cost in costs:
            count[cost] += 1

        bars = 0

        # Buy from cheapest to most expensive
        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue

            # Maximum bars we can buy at this cost
            can_buy = min(count[cost], coins // cost)

            bars += can_buy
            coins -= can_buy * cost

            # No need to continue if we cannot afford this cost anymore
            if coins < cost:
                break

        return bars