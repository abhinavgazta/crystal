def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            # getting the min price while iter
            min_price = price
        else:
            # getting the max diff and with prev max_profit , keep max..
            max_profit = max(max_profit, price - min_price)
    print(max_profit, min_price)


'''
... achieve max profit in a day ...
logic ... find first dec value
......... find till increase and switch to dec...
'''


# def max_profit_day(prices):
#     new_min_price = prices[0]
#     max_profit = 0
#     for idx, curr_price in enumerate(prices):
#         if curr_price < new_min_price:
#             new_min_price = curr_price
#         # find next max price..
#         elif curr_price > new_min_price and prices[idx-1] > prices[idx]:
#             print(curr_price, new_min_price, prices[idx - 1], prices[idx])
#             max_profit += prices[idx-1] - new_min_price
#             new_min_price = curr_price
#             print(max_profit)
#         else:
#             max_profit = max(max_profit, curr_price - new_min_price)
#     print(max_profit)

def maxProfit(prices):
    # find all upward movements.. use a range loop tech..
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    print(max_profit)


def max_profit(prices):
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            maxProfit += prices[i] - prices[i - 1]
    print(maxProfit)


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    prices1 = [7, 2, 5, 3, 6, 4, 9]
    tp = [7, 1, 5, 3, 6, 4]
    # buy 1 sell 6... profit 5.. which is max..
    # max_profit(prices1)
    pot = [1, 2, 3, 4, 5]
    max_profit(pot)
