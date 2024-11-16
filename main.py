import numpy as np
import copy

# Вихідні вектори
vectors = np.array([
    [0, 1, 0, 1, 0, 0, 1, 0, 0],  # v1: Олександр (основний)
    [0, 0, 0, 1, 0, 0, 1, 0, 0],  # v2: Інверсія позицій [1, 2]
    [0, 1, 1, 1, 0, 0, 1, 0, 0],  # v3: Інверсія позицій [3, 4]
    [0, 1, 0, 0, 1, 0, 1, 0, 0],  # v4: Інверсія позицій [5, 6]
    [0, 1, 1, 0, 1, 0, 1, 0, 0],  # v5: Інверсія позицій [7, 8]
    [1, 1, 0, 1, 0, 0, 1, 0, 0],  # v6: Інверсія позицій [0, 1]
    [0, 1, 0, 1, 1, 0, 1, 0, 0],  # v7: Інверсія позицій [2, 3]
    [0, 1, 0, 1, 0, 1, 1, 0, 0],  # v8: Інверсія позицій [4, 5]
    [0, 1, 0, 1, 0, 0, 1, 1, 0]   # v9: Інверсія позицій [6, 7]
])

# Генеруємо початкову матрицю
def generate_matrix(rows, cols):
    numbers = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    matrix = np.random.choice(numbers, size=(rows, cols))
    return matrix

# Оновлюємо матрицю в залежності від наданого значення a
def func_iteration(a, random_matrix):
    new_matrix = copy.deepcopy(random_matrix)
    k = 0
    while k < 9:
        DA = [0, 0, 0]  

        # Обчислюємо DA для кожного стовпця
        for j in range(9):
            DA[0] += (new_matrix[j][0] - vectors[k][j]) ** 2
            DA[1] += (new_matrix[j][1] - vectors[k][j]) ** 2
            DA[2] += (new_matrix[j][2] - vectors[k][j]) ** 2

        # Знаходимо мінімальний DA і його індекс
        minDA = min(DA)
        minIndex = DA.index(minDA)

        # Оновлюємо new_matrix на основі мінімального DA
        for j in range(9):
            new_matrix[j][minIndex] = 0.4 * new_matrix[j][minIndex] + a * vectors[k][j]

        k += 1
    return new_matrix

# Ініціалізація
a = 0.6
iteration_index = 1
matrices = {}

# Початкова матриця
random_matrix = generate_matrix(9, 3)
print("Початкова матриця:")
print(np.array2string(random_matrix, formatter={'float_kind': lambda x: f"{x:.4f}"}))

# Основний цикл ітерацій
current_matrix = func_iteration(a, random_matrix)
matrices[iteration_index] = current_matrix

# Основний цикл ітерацій
while True:
    a *= 0.5
    new_matrix = func_iteration(a, current_matrix)
    iteration_index += 1
    matrices[iteration_index] = new_matrix

    # Перевірка умови зупинки
    stop_condition_met = False
    for j in range(len(new_matrix)):
        for k in range(len(new_matrix[j])):
            if 0 < abs(new_matrix[j][k] - current_matrix[j][k]) <= 0.0005:
                stop_condition_met = True
                break
        if stop_condition_met:
            break

    if stop_condition_met:
        break

    # Оновлюємо поточну матрицю для наступної ітерації
    current_matrix = new_matrix

# Вивід кінцевої матриці
print(f"\nМатриця на ітерації {iteration_index}:")
print(np.array2string(current_matrix, formatter={'float_kind': lambda x: f"{x:.4f}"}))