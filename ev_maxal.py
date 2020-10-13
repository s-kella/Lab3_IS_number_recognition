import numpy as np
from numpy import linalg
from glob_and_reading import *


def evmaxal(obj, care_name, i_care):
    care = globals()[care_name]
    care = np.array(care)  # превращение в массив
    trans = care - obj
    trans = trans.transpose()  # транспонирование
    covar = globals()[covars_names[i_care]]
    E = np.eye(len(covar))  # единичная матрица
    reverse = covar + E
    reverse = linalg.inv(reverse)  # обратная матрица
    globals()['D' + care_name[4]] = np.dot(trans, reverse)  # перемножение
    globals()['D' + care_name[4]] = np.dot(globals()['D' + care_name[4]], care - obj)  # перемножение
    return globals()['D' + care_name[4]]

