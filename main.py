import datetime


def logs_path(path):
    def logger_(old_func):
        def new_func(*args, **kwargs):
            result = old_func(*args, **kwargs)
            data = f'Datetime - {datetime.datetime.now()}, name - {old_func.__name__}, arguments - {args}, {kwargs}, result - {result}\n'
            with open(path, 'a', encoding='utf-8') as file_result:
                file_result.write(data)
            print(data)
            return result

        return new_func
    return logger_


@logs_path("data.txt")
def flat_generator(ex_list):
    cursor = 0
    pointer = 0
    while cursor <= len(ex_list):
        if pointer == len(ex_list[cursor]):
            pointer = 0
            cursor += 1
            if cursor == len(ex_list):
                break
        result = ex_list[cursor][pointer]
        pointer += 1
        yield result


@logs_path("data.txt")
def sum(a, b):
    return a + b


my_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]
if __name__ == '__main__':
    for item in flat_generator(my_list):
        print(item)
    print(sum(25, 26))

