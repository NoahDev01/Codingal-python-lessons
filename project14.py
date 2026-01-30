def tuple(t):
    product = 1
    for num in t:
        product *= num
    return product

numbers = (2, 3, 4, 5)

result=tuple(numbers)
print("The product of all numbers in the tuple is:", result)