def profit(array):
    ind = 0
    delta = 0
    min = {0: 0}
    max = {0: 0}
    for price in array:
        if ind == 0:
            min = {0: price}
        if list(min.values())[0] > price:
            min = {ind: price}
        if list(max.values())[0] < price:
            max = {ind: price}

        ind += 1
    if list(max.keys())[0] > list(min.keys())[0]:
        delta = list(max.values())[0] - list(min.values())[0]
    return delta

#solution

def get_max_profit(prices):
    if len(prices) < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        profit_at_current_day = price - min_price
        max_profit = max(max_profit, profit_at_current_day)
        min_price = min(price, min_price)

    return max_profit
