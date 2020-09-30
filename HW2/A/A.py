def solution(arr):
    if len(arr) == 0:
        return 0

    current_max = 0
    current = 1

    element = arr[0]
    for i in arr[1:]:
        if element == i:
            current += 1
        else:
            if current > current_max:
                current_max = current
            current = 1
        element = i

    return max(current_max, current)
