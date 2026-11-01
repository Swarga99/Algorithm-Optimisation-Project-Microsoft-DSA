def merge_sort(arr):
    # Base case: an array with 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare elements and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90, 5]

print("Original list:", numbers)

sorted_numbers = merge_sort(numbers)

print("Sorted list:", sorted_numbers)
