import xml.etree.ElementTree as ET

names_files_s = ['samples0.xml', 'samples1.xml', 'samples3.xml', 'samples4.xml']
names_matrix_s = []  # имена переменных с матрицами образцов
cares_names = []  # имена переменных с ядрами
covars_names = []  # имена переменных с матрицами ковариации
types_of_samples = []  # типы классов
# считываем образцы
for name_s in names_files_s:
    tree_s = ET.parse(name_s)
    root_s = tree_s.getroot()
    globals()['len'+root_s[0].attrib['type']] = len(root_s) - 1  # количество образцов
    types_of_samples.append(int(root_s[0].attrib['type']))
    width = int(root_s[0].attrib['width'])
    height = int(root_s[0].attrib['height'])
    for i in range(1, len(root_s)):
        globals()['m_s_' + name_s[7] + str(i)] = []  # матрица образца
        globals()['l_s_' + name_s[7] + str(i)] = []  # list образца
        names_matrix_s.append('m_s_' + name_s[7] + str(i))
        if 'care'+name_s[7] not in cares_names:
            cares_names.append('care' + name_s[7])
            covars_names.append('covar' + name_s[7])
        for row in range(height):  # считывание образца
            globals()['m_s_' + name_s[7] + str(i)].append([])
            for column in range(width):
                globals()['m_s_' + name_s[7] + str(i)][row].append(int(root_s[i][row].text[column]))
                globals()['l_s_' + name_s[7] + str(i)].append(int(root_s[i][row].text[column]))


# считываем объекты, которые нужно классифицировать
name_o = 'objects.xml'
tree_o = ET.parse(name_o)
root_o = tree_o.getroot()


# функция для считывания объекта
def read_obj(i):
    lis = []
    matrix = []
    for row in range(height):
        matrix.append([])
        for column in range(width):
            lis.append(int(root_o[i][row].text[column]))
            matrix[row].append(int(root_o[i][row].text[column]))
            type_of_obj = root_o[i].attrib['type']
    return matrix, lis, type_of_obj


# ядра
for care in cares_names:
    globals()[care] = [0 for i in range(height*width)]
# матрици ковариации
for covar in covars_names:
    globals()[covar] = [[0 for i in range(height*width)] for j in range(height*width)]




