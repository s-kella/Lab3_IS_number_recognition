from glob_and_reading import *

# поиск матрицы ковариации
def find(covar, count_of_samples, care, type):
    for i_row, row in enumerate(covar):  # для каждого ряда матрицы ковариации
        for i_elem in range(len(row)):  # для каждого элемента ряда
            for i_sample in range(1, count_of_samples):  # для каждого образца
                covar[i_row][i_elem] += (globals()['l_s_' + type + str(i_sample)][i_elem] - care[i_elem]) * (
                            globals()['l_s_' + type + str(i_sample)][i_row] - care[i_row])
            covar[i_row][i_elem] *= 1 / (count_of_samples - 1)
    return covar
