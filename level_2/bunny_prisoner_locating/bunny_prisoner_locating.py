import sys


def generate_cells(x_coord, y_coord):
    cells = []
    x_coord = (x_coord * 2) + 2
    y_coord = (y_coord * 2) + 2

    x_cell_number = 1
    x_delta = 2
    starting_x_delta = 2
    sxd_delta = 1

    y_cell_number = 1
    y_delta = 1

    for row in range(y_coord):
        # print('row {}'.format(row))
        cells.append([y_cell_number])
        x_cell_number = y_cell_number
        starting_x_delta = row + 2
        x_delta = starting_x_delta

        for col in range(x_coord + 1):
            x_cell_number += x_delta
            cells[row].append(x_cell_number)
            x_delta += 1

        y_cell_number += y_delta
        y_delta += 1
        x_coord -= 1

    return cells


def solution(x, y):
    x_coord = x
    y_coord = y

    x_cell_number = 1
    x_delta = 2

    for col in range(x_coord):
        x_cell_number += x_delta
        x_delta += 1
    y_cell_number = x_cell_number - 1
    y_delta = x_delta - 1

    for row in range(y_coord - 2):
        y_cell_number += y_delta
        y_delta += 1

    output = y_cell_number

    return str(output)


print(solution(1, 1))
print(solution(2, 3))
print(solution(3, 2))
print(solution(5, 10))
'''print(solution(100, 100))
print(solution(200, 200))'''
print(solution(10, 10))
print(solution(100, 100))
print(solution(1000, 1000))
print(solution(10000, 10000))
print(solution(100000, 100000))

'''generated_cell_list = generate_cells(8, 8)
for y in range(len(generated_cell_list)):
    print(generated_cell_list[y])'''
