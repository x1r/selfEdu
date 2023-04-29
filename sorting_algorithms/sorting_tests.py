from copy import deepcopy
import mergesort
import quicksort
import radixsort
import heapsort
import random
import time
import icecream as ic

import pytest


@pytest.fixture
def array_size():
    return 5000000


def test_sorting(array_size):
    array = []
    print()
    for _ in range(array_size):
        array.append(random.randint(0, 10000))
    original_array = deepcopy(array)
    # print("Original array: " + str(array))
    start = time.time()
    array = mergesort.mergesort(array)
    end = time.time()
    print("Mergesort: " + str(end - start))
    assert array == sorted(original_array)
    array = original_array
    start = time.time()
    array = quicksort.quicksort(array)
    end = time.time()
    print("Quicksort: " + str(end - start))
    assert array == sorted(original_array)
    array = original_array
    start = time.time()
    array = radixsort.radixsort(array)
    end = time.time()
    print("Radixsort: " + str(end - start))
    assert array == sorted(original_array)
    array = original_array
    start = time.time()
    array = heapsort.heapsort(array)
    end = time.time()
    print("Heapsort: " + str(end - start))
    assert array == sorted(original_array)


if __name__ == '__main__':
    for i in range(1000, 100000, 1000):
        print(f"Array size: {i}")
        test_sorting(i)
        print()
