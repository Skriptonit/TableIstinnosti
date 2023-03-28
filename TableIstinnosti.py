def FTable(rows):
    arr = []
    print("Введите F столбец:")
    for i in range(rows):
        arr.append(int(input("Введите 1 или 0: ")) % 2)
    print("Данные введены!")
    print("Введенные данные: ", arr)
    return arr


def truthTable(rows, columns):
    arr = [[1 for i in range(columns)] for j in range(rows)]
    for i in range(rows):
        count = i
        for j in range(columns):
            arr[i][j] = count % 2
            count //= 2

    for i in range(rows):
        arr[i].reverse()

    for i in range(rows):
        for j in range(columns):
            print(arr[i][j], end=' ')
        print('')
    return arr


def SDNF(truthArr, FArr):
    str = "СДНФ: ";
    for i in range(len(FArr)):
        if FArr[i]:
            str += "("
            for j in range(len(truthArr[i])):
                if truthArr[i][j]:
                    str += f"A{j + 1}"
                else:
                    str += f"¬A{j + 1}"
                str += "&"
            str = str[:-1]
            str += ")"
            str += "|"
    str = str[:-1]
    return str


def SKNF(truthArr, FArr):
    str = "СКНФ: ";
    for i in range(len(FArr)):
        if not FArr[i]:
            str += "("
            for j in range(len(truthArr[i])):
                if not truthArr[i][j]:
                    str += f"A{j + 1}"
                else:
                    str += f"¬A{j + 1}"
                str += "|"
            str = str[:-1]
            str += ")"
            str += "&"
    str = str[:-1]
    return str


columns = 0
columns = int(input("Введите кол-во столбцов: "))
rows = 2 ** columns
FArr = FTable(rows)
truthArr = truthTable(rows, columns)
print(SDNF(truthArr, FArr))
print(SKNF(truthArr, FArr))