def solution(x):
    result = []
    first_h_idx = x.find('h')
    last_h_idx = x.rfind('h')

    for i in range(len(x)):
        if i > 0 and i % 3 == 0:
            result.append('')
        elif x[i] == 'h':
            if i != first_h_idx and i != last_h_idx:
                result.append('H')
            else:
                result.append('h')
        elif x[i] == '1':
            result.append('one')
        else:
            result.append(x[i])

    return ''.join(result)
