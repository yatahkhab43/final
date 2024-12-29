from binsearch import binary_search


def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    return binary_search(arr[:min(i, len(arr))], target)

arr = [2, 3, 4, 10, 40]
target = 10
print(f"Element found at index: {exponential_search(arr, target)}")
