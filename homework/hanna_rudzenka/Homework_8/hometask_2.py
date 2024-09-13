import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def return_fibonachi(numb):
    fib_gen = fibonacci_generator()
    index = 0
    for num in fib_gen:
        if index == numb - 1:
            print(num)
            break
        index += 1


return_fibonachi(5)
return_fibonachi(200)
return_fibonachi(1000)
return_fibonachi(100000)
