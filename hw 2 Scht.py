while True:
    try:
        def nod(a, b):
            while b != 0:
                a, b = b, a % b
            return a


        chislo1 = int(input("введите целое число первое"))
        chislo2 = int(input("введите целое число второе"))
        if chislo1 > chislo2:
            itog = nod(chislo1, chislo2)
            print(itog, "наибольший делитель этих чисел")
            break
        elif chislo1 < chislo2:
            itog = nod(chislo2, chislo1)
            print(itog, "наибольший делитель этих чисел")
            break
    except:
        print("вы сделали что-то не так,введите целые числа")
