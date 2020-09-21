def solution(n):
    lst = []
    start = 1
    while start <= n:
        lst.append(start)
        start = start * 2
    return lst


