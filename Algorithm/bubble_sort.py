def bubble_sort(input):
    n = len(input)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if input[i] > input[i + 1]:
                input[i], input[i + 1] = input[i + 1], input[i]


    return input



def bubble_sort_optimised(input):
    n = len(input)
    for j in range(n - 1):
        swapped = False
        for i in range(n - j - 1):
            if input[i] > input[i + 1]:
                input[i], input[i + 1] = input[i + 1], input[i]
                swapped = True
                print("To track progress:       ", input)
        if not swapped:
            break
    return input


my_array = [7, 12, 9, 11, 3]

print("Answer:    ",bubble_sort(my_array))
print("Answer:    ",bubble_sort_optimised(my_array))