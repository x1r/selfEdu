def mergesort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    left_array = mergesort(left_array)
    right_array = mergesort(right_array)

    merged_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            merged_array.append(left_array[left_index])
            left_index += 1
        else:
            merged_array.append(right_array[right_index])
            right_index += 1

    merged_array += left_array[left_index:]
    merged_array += right_array[right_index:]
    return merged_array


arr = [531810, 929685, 50630, 829174, 942680, 223343, 885978, 138210, 783445, 653458]
sorted_arr = mergesort(arr)
print(sorted_arr)
