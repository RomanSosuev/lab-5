"""
11.	Формируется матрица F следующим образом: скопировать в нее А и если в С сумма чисел  в нечетных столбцах больше,
чем произведение чисел в четных строках, то поменять местами В и С симметрично, иначе Е и В поменять местами
несимметрично.При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов
матрицы F,то вычисляется выражение:A-1*AT – K * F-1, иначе вычисляется выражение (AТ +G-1-F-1)*K, где G-нижняя
треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
import numpy as np
try:
    row_q = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 4 до 100:"))
    while row_q < 4 or row_q > 100:
        row_q = int(input("Вы ввели неверное число\nВведите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100:"))
    K = int(input("Введите число К="))

    A = np.random.randint(-10, 10, (row_q, row_q)) # заполняем матрицу А случайными числами
    print("Матрица А\n", A)

    F = A.copy() #копируем элементы матрицы А в матрицу F
    print("Матрица F\n", F, "\n")
    summ = 0
    proizv = 1
    # сумма и произведение в C
    for i in range(row_q // 2 + row_q % 2, row_q):
        for j in range(row_q // 2 + row_q % 2, row_q):
            if j % 2 == 0:
                summ += F[i][j]
            if i % 2 == 1:
                proizv *= F[i][j]
    print ('Сумма в нечетных слобцах: ', summ, "\nПроизведение в четных строка: ", proizv, "\n")
    if summ > proizv:
        for i in range(row_q // 2):
            for j in range(row_q // 2 + row_q %2, row_q):
                F[i][j], F[i + row_q//2 + row_q % 2][j] = F[i + row_q//2 + row_q % 2][j], F[i][j]
    else:
        for i in range(row_q // 2):
            for j in range(row_q // 2):
                F[i][j], F[i][j + row_q // 2 + row_q % 2] = F[i][j + row_q // 2 + row_q % 2], F[i][j]
    print("Матрица F после изменений\n", F)
    print("\n Определитель A = ", np.linalg.det(A),"\n Сумма диагоналей F = ", np.trace(F),"\n")
    G = np.tril(A, k=0)
    print("Нижняя трeугольная матрица G\n", G,"\n")
    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
    print("Нельзя вычислить")
    elif np.linalg.det(A) > np.trace(F):
        print("A^-1*AT – K * F^-1\n")
        print(np.linalg.inv(A)*np.transpose(A)-K*np.linalg.inv(F))
    else:
        print("(AТ +G^-1-F^-1)*K\n")
        print((np.linalg.inv(A) + np.linalg.inv(G) - np.linalg.inv(F)) * K)

except ValueError:
        print("\nэто не число, перезапустите программу и повторите попытку")
