class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        print(costs)
        s = 0
        for i in range(len(costs)):
            if costs[i]<=coins: 
                s += 1
                coins -= costs[i]
            else:
                break
        return(s)
