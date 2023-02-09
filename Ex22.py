def IdentChck (arr, n, m):
    if len(arr) != n+m:
        print('Неверное кол-во элементов.')
        exit()
    else:
        print(arr)
        tempFst = arr[:n]
        tempScnd = arr[n:]
        resultList = []
        for i in range (len(tempFst)):
            if tempFst[i] in tempScnd:
                if tempFst[i] in resultList:
                    continue
                else:
                    resultList.append(tempFst[i])
        return sorted(resultList)

n = int(input("Введите размер первого множества: "))
m = int(input("Введите размер второго множества: "))
arr = input('Введите элементы множеств через пробел: ').split()
result = IdentChck(arr, n, m)
print(result)
