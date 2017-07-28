__matrix_dict = {

    '0': [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    '1': [[0, -1, 0], [-1, 5, -1], [0, -1, 0]],
    '2': [[0, -1, 0], [-1, 4, -1], [0, -1, 0]],
    '3': [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]],
    '4': [[1, 1, 1], [1, -2, 1], [-1, -1, -1]]

}


def get_matrix_dict():
    return __matrix_dict


def change_color_effects(mode, array, matrix_type_dict):
    res = 0

    matrix = matrix_type_dict.get(mode)

    for i in range(3):
        for j in range(3):
            res += array[i][j] * matrix[i][j]

    res /= 9

    return int(res)
