def sq(x):
    return x * x


def add(a, b):
    return a + b


def my_map(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result


def my_reduce(func, data):
    result = data[0]
    for idx in range(1, len(data)):
        result = func(result, data[idx])
    return result


my_data = [1, 2, 3, 4, 5]
str_data = ["1", "2", "3", "4", "5"]
# my_list = my_map(sq, my_data)
my_list = my_map(lambda x: x * x, my_data)
# print(my_list)
# print(my_reduce(lambda a, b: a + b, my_data))
print(my_reduce(lambda a, b: a + b, str_data))
