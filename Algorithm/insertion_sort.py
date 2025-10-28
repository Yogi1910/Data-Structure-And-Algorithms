def insertion_sort(input):
    n = len(input)
    for i in range(1, n):             # start from 1, since first element is sorted
        for j in range(i - 1, -1, -1):
            print(j+1,j)
            if input[j + 1] < input[j]:
                input[j], input[j + 1] = input[j + 1], input[j]   # swap adjacent
            else:
                break    # stop early if correct position reached

            
            print(input)

    return input


my_array = [7, 12, 9, 11, 3]
print(insertion_sort(my_array))







