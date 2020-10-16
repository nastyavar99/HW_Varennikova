def integers():
    i = 0
    while True:
        yield i
        i += 1


def squares():
    for i in integers():
        yield i * i


def take1(n, generator):
    result = []
    for i in range(n):
        try:
            result.append(next(generator))
        except StopIteration:
            break

    return result


def take2(n, generator):
    result = []
    for index, elem in enumerate(generator, start=1):
        print(index, elem)
        if index > n:
            break
        result.append(elem)

    return result
