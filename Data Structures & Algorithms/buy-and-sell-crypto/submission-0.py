class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #l=buy and r=sell
        Pmax=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                Pmax=max(profit,Pmax)
            else:
                l=r
            r+=1
        return Pmax