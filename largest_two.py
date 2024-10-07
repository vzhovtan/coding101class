def two_largest(arr):
    if len(arr) <= 1:
        return False
            
    largest, second = arr[:2]
    if largest < second:
        largest, second = second, largest

    for idx in range(2, len(arr)):
        if largest < arr[idx]:
            largest, second = arr[idx], largest
        elif second < arr[idx]:
            second = arr[idx]

    return (largest, second)