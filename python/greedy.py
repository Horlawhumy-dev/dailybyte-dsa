def optimal_small_change(denom, total_amount):

    sorted_denominations = sorted(denom, reverse=True)
    series = []

    for j in range(len(sorted_denominations)):

        term = sorted_denominations[j:]

        number_of_denoms = []
        local_total = total_amount
        
        for i in term:

            div = int(local_total / i)
            local_total = local_total % i

            if div > 0:
                number_of_denoms.append((i, div))

        series.append(number_of_denoms)

    return series

# def basic_small_change(denom, total_amount):
#     sorted_denominations = sorted(denom, reverse=True)
#     number_of_denoms = []
#     for i in sorted_denominations:
#         div = int(total_amount / i)
#         total_amount = total_amount % i
#         if div > 0:
#             number_of_denoms.append((i, div))
#     return number_of_denoms

print(optimal_small_change([4, 5, 1], 14))