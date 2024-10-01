def narcissistic(value):
    length = len(str(value))
    count = 0
    divide = 1
    total = 0

    while count < length:
        total += (value//divide%10)**length
        divide *= 10
        count += 1
    if total == value:
        return True
    else:
        return False