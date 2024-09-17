def function_decorator(func):
    def wrapper(text, count):
        for i in range(count):
            func(text)

    return wrapper


@function_decorator
def example(text):
    print(text)


example('print me', count=5)
