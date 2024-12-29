def insert_element(array, position, element):
    array.insert(position, element)
    return array

def delete_element(array, position):
    if 0 <= position < len(array):
        array.pop(position)
    return array

def search_element(array, target):
    return array.index(target) if target in array else -1

arr = [1, 2, 3, 4, 5]
print("After Insertion:", insert_element(arr, 2, 99))
print("After Deletion:", delete_element(arr, 2))
print("Search Result:", search_element(arr, 4))
