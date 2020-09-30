def solution(a, b):
    if b == 0:
        return a
    return solution(a + 1, b - 1)


