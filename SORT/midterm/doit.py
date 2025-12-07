def do_it(arr):
    if len(arr) <=1:
        return arr
    x = len(arr) // 2
    y1 = do_it(arr[:x])
    y2 = do_it(arr[x:])

    result = []
    while y1 and y2:
        result.append(y1.pop(0) if y1[0] < y2[0] else y2.pop(0))

    return result + y1 + y2

word = list('algorithm')
result = do_it(word)
print((result))