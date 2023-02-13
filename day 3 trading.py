#In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete (Buy->sell->Buy->sell). Given stock prices throughout the day, find out the maximum profit that a share trader could have made.
Program:
def maxProfit(price, n):
   # Create profit array and initialize it as 0
    profit = [0]*n
    max_price = price[n-1]
 for i in range(n-2, 0, -1):
 if price[i] > max_price:
            max_price = price[i]
   profit[i] = max(profit[i+1], max_price - price[i])
  min_price = price[0]
 for i in range(1, n):
  if price[i] < min_price:
            min_price = price[i]
   profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))
  result = profit[n-1]
  return result
 # Driver function
price = [7,1,5,3,6,4]
print ("Maximum profit is", maxProfit(price, len(price)))

Output:
Input: prices = [7,1,5,3,6,4] 
Output: 7 
