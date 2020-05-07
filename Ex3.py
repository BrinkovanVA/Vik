from datetime import datetime

def logger(path):
    def my_decorator(func):
        def wrapper(arg1, arg2):
            start = datetime.now()
            res = func(arg1, arg2)
            with open(path, "a") as file:
                file.write(f"Started {start}\n")
                file.write(f"Args {arg1}, {arg2}\n")
                file.write(f"Result {res}\n")
                file.write(f"Stopped {datetime.now()}\n")
                file.write(f"Work time {datetime.now() - start}\n\n")
            return res
        return wrapper
    return my_decorator

@logger("out.txt")
def summ(arg1, arg2):
    o = 2
    for i in range(100000000):
        o += 1
    print(arg1 + arg2)
    return arg1 + arg2

summ(1, 2)