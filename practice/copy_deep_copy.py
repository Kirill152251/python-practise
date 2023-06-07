import copy

some_list = [[2], 4, 1, 4, 5]
# some_copy = some_list.copy()
simple_copy = some_list.copy()
deep_copy = copy.deepcopy(some_list)

print('сравнение по содержанию:')
print(f'simple copy: {some_list[0] == simple_copy[0]}')
print(f'deep copy: {some_list[0] == deep_copy[0]}')
print()
print('сравнение по ссылке:')
print(f'simple copy: {some_list[0] is simple_copy[0]}')
print(f'deep copy: {some_list[0] is deep_copy[0]}')