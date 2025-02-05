def multiply_matrices(A, B):
    """
    Умножава две двумерни матрици A и B и връща резултантната матрица C - трети двумерен масив.
    Var A - Първата матрица (списък от списъци), с размер MxN
    Var B - Втората матрица (списък от списъци), с размер NxP
    Var C - Резултантната матрица C (списък от списъци), с размер MxP
    """

    # Проверка за съвместимост на матриците
    # За да могат да се умножават, броят на колоните на матрицата A (len(A[0])) 
    # трябва да бъде равен на броя редове на матрицата B (len(B)).
    if len(A[0]) != len(B):
        raise ValueError("Матриците не могат да се умножават: несъвместими размери.")

    # Инициализиране на резултантната матрица C
    # Резултантната матрица C ще има размер MxP, където:
    # M = брой редове в матрицата A
    # P = брой колони в матрицата B
    C = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Основен алгоритъм за умножение на матрици
    # Обхождаме редовете на матрицата A
    for i in range(len(A)):
        # Обхождаме колоните на матрицата B
        for j in range(len(B[0])):
            # Пресмятаме стойността на C[i][j]
            # Това става чрез умножение на съответните елементи от реда на A и колоната на B,
            # след което сумираме резултатите.
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C


# Демонстрация на функцията с дадените примерни матрици
if __name__ == "__main__":
    # Примерни матрици от задачата
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    """
    Решение:
    * 1x7 + 2x9 + 3x11 = 7 + 18 + 33 = 58
    * 1x8 + 2x10 + 3x12 = 8 + 20 + 36 = 64
    * 4x7 + 5x9 + 6x11 = 28 + 45 + 66 = 139
    * 4x8 + 5x10 + 6x12 = 32 + 50 + 72 = 154

    Матрица C, отпечатана от кода с дадения пример трябва да е:
    [58, 64]
    [139, 154]
    """

    # Извикване на функцията и съхранение на резултата
    C = multiply_matrices(A, B)

    # Отпечатване на резултата
    print("Резултантната матрица C:")
    for row in C:
        print(row)