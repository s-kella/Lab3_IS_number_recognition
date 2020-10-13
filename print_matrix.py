# вывод матрицы
def pr(matrix, lenght):
    for i in range(len(matrix)):
        print(round(matrix[i], 2), '\t', end='')
        if (i+1) % lenght == 0:
            print()
    print()