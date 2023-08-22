
def find_max_value(weights: list, values: list, max_pound: int) -> int:
    """"T(C) => O(n) S(C) => O(1)"""
    max_value_of_gallery = 0
    i = 0

    if weights[1] > weights[0]:
        i = 1
        
    while i < len(weights) and max_pound >= weights[i]:
        max_value_of_gallery += values[i]
        max_pound -=  weights[i]
        i += 1
    return max_value_of_gallery

weights = [6, 1, 10]
values = [60, 5, 110]
max_pound = 38
print(find_max_value(weights, values, max_pound))