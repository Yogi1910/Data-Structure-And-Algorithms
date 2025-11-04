def selection_sort(input):
    n = len(input)
    for i in range(n):
        for j in range(i + 1, n):
            if input[j] < input[i]:
                input[i], input[j] = input[j], input[i]
    return input



def selection_sort_optimised(input):
    n = len(input)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if input[j] < input[min_index]:
                min_index = j
        if min_index != i:  # only swap if needed
            input[i], input[min_index] = input[min_index], input[i]
    return input


my_array = [7, 12, 9, 11, 3]
print(selection_sort(my_array))
print(selection_sort_optimised(my_array))
