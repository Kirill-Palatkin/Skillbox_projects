import datetime
import functools


def logging(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        with open('function_errors.log', 'a', encoding='utf8') as log_file:
            try:
                func(*args, **kwargs)
                print(f'Название функции: {func.__name__}')
                print(f'Ее документация:{func.__doc__}\n')
            except Exception as error:
                print(f'В функции {func.__name__} ошибка!\n')
                log_file.write(f'Ошибка в функции: {func.__name__}\n')
                log_file.write(f'Ошибка: {str(error)}\n')
                log_file.write(f'Дата и время возникновения ошибки: {datetime.datetime.now()}\n\n')
    return wrapped_func


@logging
def func_1():
    """ <Документация функции 1...>"""
    return None


@logging
def func_2():
    """ <Документация функции 2...>"""
    res = 1/0
    return res


@logging
def func_3():
    """ <Документация функции 3...>"""
    res = 'a' + 5
    return res


@logging
def func_4():
    """ <Документация функции 4...>"""
    return None


func_1()
func_2()
func_3()
func_4()
