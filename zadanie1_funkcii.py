def squares(length, width, count=0):
    if length < width:
        length, width = width, length
    length -= width
    if length == 0:
        print('квадрат номер: ', count + 1, ' с ребром ', width)
        return 1
    count += 1
    print('квадрат номер: ', count, ' с ребром ', width)
    return squares(length, width, count)
