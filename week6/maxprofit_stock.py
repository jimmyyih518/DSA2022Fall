'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


'''

def maxProfit(prices):
	l = 0
	res = 0
	for r in range(1, len(prices)):
		if prices[r] < prices[l]:
			l = r
			
		curr = prices[r] - prices[l]
		res = max(curr,res)
		
	return res

#Testing Code	
prices = [7,1,5,3,6,4]
print(maxProfit(prices))