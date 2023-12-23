class MatrixHelper:
    def __init__(self):
        pass

    def print_2d_matrix(matrix):
        for row in matrix:
            for i, elem in enumerate(row):
                if i == len(row)-1:
                    print(f'| {elem:.2f}')
                else:
                    print(f'{elem:.2f}', end=' ')

    def save_matrix(matrix, file_name):
        with open(file_name, 'w') as f:
            f.write(f'{len(matrix)}\n')
            for row in matrix:
                for i, elem in enumerate(row):
                    if i == len(row)-1:
                        f.write(f'{elem:.2f}\n')
                    else:
                        f.write(f'{elem:.2f} ')