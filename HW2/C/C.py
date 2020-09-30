def solution(arr):
    if not arr:  # для четного квадрата
        return []

    result = arr.pop(0)
    if not arr:  # для нечетного квадрата
        return result

    for i in arr[: -1]:
        result.append(i.pop(-1))

    result.extend(reversed(arr.pop(-1)))
    for i in reversed(arr):
        result.append(i.pop(0))

    result.extend(solution(arr))
    return result


