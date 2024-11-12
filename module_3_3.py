def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)
values_list = ['Орёл', 23, 4.6]
values_dict = {'a': 9, 'b': 'Решка', 'c': False}
values_list_2 = ['Орешка', 2.4]
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)