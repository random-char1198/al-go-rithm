def max_profit(prices):
    if len(prices) <= 1:
        return 0
    max_prof = 0  # Lowest value of max profit
    min_prof = prices[0]  # make the first index of the list

    for i in range(1, len(prices)):
        min_prof = min(min_prof, prices[i])
        max_prof = max(max_prof, prices[i] - min_prof)
    return max_prof


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6,5,4,3,2,1]))
