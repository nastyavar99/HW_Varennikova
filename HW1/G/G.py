def solution(a, b):
    b = [i for i in b if i not in a]
    a.extend(b)
    return sorted(a)


