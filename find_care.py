# поиск ядра
def find(count_of_samples, matrix_s, care):
    number_of_element = 0
    for i in range(count_of_samples):
        for row in matrix_s:
            for elem in row:
                care[number_of_element] += int(elem)
                number_of_element += 1
        number_of_element = 0
    for i in range(len(care)):
        care[i] /= count_of_samples
    return care