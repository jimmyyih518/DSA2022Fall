def maxProfit(prices):
	l = 0
	res = 0
	for r in range(1, len(prices)):
		if prices[r] < prices[l]:
			l = r
			
		curr = prices[r] - prices[l]
		res = max(curr,res)
		
	return res
	
prices = [7,1,5,3,6,4]
maxProfit(prices)