def heapsort(array):
    build_max_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)

    return array


def build_max_heap(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        heapify(array, i, len(array))


def heapify(array, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest, n)
