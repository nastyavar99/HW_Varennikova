def solution(total):
    time = total % 1440  # минут в сутка
    hours = time // 60
    minutes = time % 60
    return f'{hours} {minutes}'




