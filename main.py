from glob_and_reading import *
import find_covar
import find_care
import ev_maxal
import print_matrix


# ищем ядро
for ind, name in enumerate(names_matrix_s):
    globals()['care' + names_matrix_s[ind][4]] = find_care.find(globals()['len'+name[4]], globals()[name], globals()['care' + names_matrix_s[ind][4]])

# ищем матрицу ковариации
for i_care, care_name in enumerate(cares_names):
    globals()[covars_names[i_care]] = find_covar.find(globals()[covars_names[i_care]], globals()['len' + care_name[4]], globals()[cares_names[i_care]], care_name[4])

print('Ядра всех классов:')
for i_care, care_name in enumerate(cares_names):
    print('Класс',care_name[4])
    print_matrix.pr(globals()[cares_names[i_care]], width)

match = 'Да'
for obj_i in range(1, len(root_o)):
    list_d = []  # лист с расстояниями до классов
    list_classes = []  # лист с порядком классов, с которыми считалось расстояние
    print('Расстояние до всех классов:')
    for i_care, care_name in enumerate(cares_names):
        obj_m, obj_l, type_of_obj = read_obj(obj_i)  # чтение объекта из xml
        d = ev_maxal.evmaxal(obj_l, care_name, i_care)  # нахождение расстояния по метрике Евклида-Махаланобиса
        list_d.append(d)
        list_classes.append(care_name[4])  # care_name - строка с названием переменной с ядром, 4 элемент - класс (care0, care1 ...)
        print(f'Класс {care_name[4]} : {d}')
    m = min(list_d)
    print('Класс объекта:', list_classes[list_d.index(m)])
    if list_classes[list_d.index(m)] == type_of_obj:
        b = 'Да'
    else:
        b = 'Нет'
        match = 'Нет'
    print('Правильно ли определился класс:', b)
    print('Объект:')
    print_matrix.pr(obj_l, width)
    print()

print('Все ли объекты определены правильно:', match)
