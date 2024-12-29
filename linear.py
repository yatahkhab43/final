def linear_search(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count

arr = [2, 3, 5, 3, 7, 3, 8]
target = 3
print(f"Occurrences of {target}:", linear_search(arr, target))
