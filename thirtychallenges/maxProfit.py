def printResult(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))
    return wrapper

class Solution:
    @printResult
    def maxProfit(self, prices: list) -> int:
        if prices is None:
            return 0

        maxProfit = 0
        tmpProfit = 0
        lastPrice = -1

        for price in prices:
            if lastPrice == -1:
                lastPrice = price
            
            if price >= lastPrice:
                tmpProfit += price - lastPrice
            else:
                maxProfit += tmpProfit
                tmpProfit = 0
            
            lastPrice = price

        return maxProfit + tmpProfit

if __name__ == '__main__':
    scanner = Solution()
    scanner.maxProfit(None)
    scanner.maxProfit([])
    scanner.maxProfit([1,2,3,4,5])
    scanner.maxProfit([1,5,2,4,1])
    scanner.maxProfit([5,7,3,9,4])