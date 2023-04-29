def radixsort(array):
    max_value = max(array)
    num_digits = len(str(max_value))

    for i in range(num_digits):
        count = [0] * 10

        for j in range(len(array)):
            digit = (array[j] // 10 ** i) % 10
            count[digit] += 1

        for j in range(1, 10):
            count[j] += count[j - 1]

        sorted_array = [0] * len(array)

        for j in range(len(array) - 1, -1, -1):
            digit = (array[j] // 10 ** i) % 10
            index = count[digit] - 1
            sorted_array[index] = array[j]
            count[digit] -= 1

        array = sorted_array

    return array
