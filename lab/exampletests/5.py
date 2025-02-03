# 5. Да се състави програма за обработка на двумерния масив A[N,N], където данните са
# цели числа в интервала [-500;1000]. Програмата да извърши следните действия:
# ● отпечатване на условието на задачата;
# ● отпечатване на имената на автора на програмата;
# ● въвеждане на входните данни;
# ● отпечатване на входните данни;
# ● а) да се образува едномерен масив C[N], елементите на който са максималните
# елементи от всеки ред на масива А;
# ● б) полученият масив да се сортира по големина;
# ● отпечатване на получените резултати след обработка а) и след обработка б)

def print_condition():
    print("\nЗадача: Обработка на двумерен масив A[N,N] с цели числа в интервала [-500;1000].\n"
          "1. Да се образува едномерен масив C с максималните елементи от всеки ред на масива A.\n"
          "2. Да се сортира масивът C по големина.\n")

def print_author():
    print("\nАвтор: Вашето име\n")

def input_matrix(n):
    print(f"\nВъведете елементите на матрицата A ({n}x{n}):")
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            while True:
                try:
                    element = int(input(f"A[{i}][{j}]: "))
                    if -500 <= element <= 1000:
                        row.append(element)
                        break
                    else:
                        print("Моля, въведете число в интервала [-500, 1000].")
                except ValueError:
                    print("Моля, въведете валидно цяло число.")
        matrix.append(row)
    return matrix

def print_matrix(matrix, name):
    print(f"\nМатрица {name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

def find_row_max_elements(matrix):
    c = [max(row) for row in matrix]
    return c

def main():
    print_condition()
    print_author()

    while True:
        try:
            n = int(input("\nВъведете размер на матрицата N (цяло число > 0): "))
            if n > 0:
                break
            else:
                print("Моля, въведете цяло число по-голямо от 0.")
        except ValueError:
            print("Моля, въведете валидно цяло число.")

    a = input_matrix(n)
    print_matrix(a, "A")

    c = find_row_max_elements(a)
    print(f"\nМасив C с максималните елементи от всеки ред: {c}")

    c_sorted = sorted(c)
    print(f"\nМасив C след сортиране: {c_sorted}")

if __name__ == "__main__":
    main()