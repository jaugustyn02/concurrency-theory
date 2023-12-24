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
        nrow = len(matrix)
        ncol = len(matrix[0])
        with open(file_name, 'w') as f:
            f.write(f'{nrow}\n')
            for row in range(nrow):
                for col in range(ncol-1):
                    if col == ncol-2:
                        f.write(f'{matrix[row][col]}\n')
                    else:
                        f.write(f'{matrix[row][col]} ')
            for row in range(nrow):
                f.write(f'{matrix[row][ncol-1]} ')
            f.write('\n')