numbers = [1 , 4 , 6]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        # even_numbers += [number]
print(f"Even numbers: {even_numbers}")

numbers = [1 ,3, 4, 6 , 7 ,8]
doubles = [num * 2 for num in numbers]
print(doubles)
