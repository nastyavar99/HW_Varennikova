def solution(n):
    if n == 0:
        return ''
    penguin = [
        '   _~_   ' * n,
        '  (o o)  ' * n,
        ' /  V  \ ' * n,
        '/(  _  )\\' * n,
        '  ^^ ^^  ' * n
    ]

    return '\n'.join(penguin)



