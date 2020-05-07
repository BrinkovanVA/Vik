def stupid_decorator(func):
    def wrapper(l):
        res = func(l)
        if res == 0:
            print("Нет")
        elif res > 10:
            print("Очень много")
    return wrapper


@stupid_decorator
def numbers(l):
    count = 0
    for i in l:
        if i % 2 == 0:
           count += 1
    print(count)
    return count


numbers([1, 1, 1, 1])