def function_decorator(func):
    def wrapper(text):
        func(text)
        print('finished')

    return wrapper


@function_decorator
def start_func(text):
    print(text)


start_func('the function started')
