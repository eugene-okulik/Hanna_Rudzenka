def func_decorator(func):
    def wrapper(first, second):
        if first > 0 and second > 0:
            if first == second:
                return func(first, second, operation="+")
            elif first > second:
                return func(first, second, operation="-")
            elif second > first:
                return func(first, second, operation="/")
        return func(first, second, operation="*")

    return wrapper


@func_decorator
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return second - first
    elif operation == "/":
        return first / second
    elif operation == "*":
        return first * second


int_1 = int(input('введите первое число'))
int_2 = int(input('введите второе число'))
print(calc(int_1, int_2))
