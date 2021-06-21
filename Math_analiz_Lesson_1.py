'''
Даны три множества a,b и с. Необходимо выполнить все изученные виды бинарных операций над всеми комбинациями множеств.
*Выполнить задание 1 на языке Python

'''

set_a = {1, 2, 3, 4, 5, 6, 16, 17}
set_b = {1, 3, 5, 16}
set_c = {2, 4, 6, 16}

set_d = set_a & set_b & set_c
set_e = set_a & (set_b | set_c)
set_f = (set_a | set_b) & set_c
set_g = set_a | set_b | set_c
set_h = set_a - (set_b | set_c)
set_i = set_a - (set_b & set_c)
set_j = set_a ^ set_b
set_k = set_a ^ set_c
set_l = set_b ^ set_c


print(set_d)
print(set_e)
print(set_f)
print(set_g)
print(set_h)
print(set_i)
print(set_j)
print(set_k)
print(set_l)