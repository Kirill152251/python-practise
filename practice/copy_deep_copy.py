import copy

# Поверхностная копия (copy) создает новый составной объект, и затем
# (по мере возможности) вставляет в него ссылки на объекты, находящиеся в оригинале.

# Глубокая копия (deepcopy) создает новый составной объект, и затем рекурсивно
# вставляет в него копии объектов, находящихся в оригинале.

some_list = [[2], 4, 1, 4, 5]
# some_copy = some_list.copy()
simple_copy = some_list.copy()
deep_copy = copy.deepcopy(some_list)

print('сравнение по содержанию:')
print(f'simple copy: {some_list[0] == simple_copy[0]}')
print(f'deep copy: {some_list[0] == deep_copy[0]}')
print()
print('сравнение по ссылке:')
print(f'simple copy: {some_list[2] is simple_copy[2]}')
print(f'deep copy: {some_list[0][0] is deep_copy[0][0]}')
