# Leetode buy and sell stock

# universal algorithm does worl but tle
# similar to knapsack algo

solve(1,0) # 1- next day 0 bought handle len 1and 0 before calling

def solve(day,buy):

	if(day==len(prices)-1):

		return max(0,prices[day]-prices[buy]) # return +ve or 0

	elif(prices[day]<prices[buy]): # A dip buy!!

		return solve(day+1,day)

	else:

		sellandbuy = prices[day]-prices[buy]+solve(day+1,day) # try buying

		notbuy = solve(day+1,buy) 

		return max(sellandbuy,notbuy)