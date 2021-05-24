a = [20, 7, 8, 2, 5]
def minimumLoss(price):
    prices_dict = {pr: idx for (pr, idx) in zip(price, range(len(price)))}
    price.sort()
    return min([price[i + 1] - price[i]
    for i in range(len(price) - 1)
        if prices_dict[price[i + 1]] < prices_dict[price[i]]]) #index of price[i] RP should be greater than index of price[i+1] PR


x=minimumLoss(a)
print(x)
