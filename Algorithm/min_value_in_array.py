my_array = [7, 12, 9, 4, 11]

def find_lowest(arr):
    lowest = arr[0]
    for i in arr[1:]:
        if i < lowest:
            lowest = i

    return lowest


print(find_lowest(my_array))