def sum_values(value1_to_sum: float, value2_to_sum: float = 10) -> float:
    '''
    A simple function that sums float values and return a float value
    '''
    sum_result = value1_to_sum + value2_to_sum
    return sum_result

value1 = 2
value2 = 4

value3 = sum_values(value1_to_sum=value1, value2_to_sum=value2)
print(value3)

value4 = 50
value5 = 30
value6 = sum_values(value4, value5)
print(value6)

value7 = 0
value8 = sum_values(value7)
print(value8)