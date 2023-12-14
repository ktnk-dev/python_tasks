from functions import file

class t:
    def _homework_3():
        """Написать программу, которая по введенному номеру единицы измерения (1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер) и массе М
выдавала бы соответствующее значение массы в килограммах."""
        
        # --------- #
        единица_измерения = int(input("Введите номер единицы измерения: "))
        введенная_масса = int(input("Введите массу: "))

        print("Результат: ")

        if единица_измерения == 1: print(введенная_масса)
        if единица_измерения == 2: print(введенная_масса / 1000000) 
        if единица_измерения == 3: print(введенная_масса / 1000)
        if единица_измерения == 4: print(введенная_масса * 1000)
        if единица_измерения == 5: print(введенная_масса * 100)

        return ''

    def _kr():
        from random import randint

        лимит_массива = 3
        двумерный_массив = [] # это список каких-то любых(!) данных 


        for i in range(лимит_массива): # range() это перебор. например range(4) => 0,1,2,3
            маленький_массив = []
            for j in range(лимит_массива): 
                маленький_массив = маленький_массив + [randint(-100, 100)]

            двумерный_массив = двумерный_массив + [маленький_массив]

        print (двумерный_массив)

        # тут список всех сумм
        все_суммы = []

        for i in range (лимит_массива): # проходим по каждому списку из двучиного массива
            нынешний_массив = двумерный_массив[i]
            сумма_ячеек = sum(нынешний_массив) # считаем сумму
            все_суммы = все_суммы + [сумма_ячеек] # добавляем сумму в переменную все_суммы

        print(все_суммы)

        # обьявляем самый большой и самый маленький массив
        самый_маленький_массив = []
        самый_большой_массив = []

        for i in range (лимит_массива): # проходим по каждому списку из двучиного массива
            нынешний_массив = двумерный_массив[i]
            сумма_ячеек = sum(нынешний_массив) # считаем сумму

            if сумма_ячеек == min(все_суммы): # если сумма совпала с самой маленькой суммой из всех найденных = записываем список в переменную для самого маленького 
                самый_маленький_массив = нынешний_массив 

            if сумма_ячеек == max(все_суммы): # если сумма совпала с самой большой суммой из всех найденных = записываем список в переменную для самого большого 
                самый_большой_массив = нынешний_массив


                
        print("строка с наименьшей суммой элементов", самый_маленький_массив)
        print("строка с наибольшей суммой элементов", самый_большой_массив)

    
    def _7():
        """В строке заменить букву(а) буквой (о). Подсчитать количество замен. Подсчитать, сколько символов в строке."""

        строка = input('Введите строку: ') # сюда вводим строку любую

        букву_которую_надо_заменить = 'а' 
        букву_НА_которую_надо_заменить = 'о'
        # название говорит само за себя


        количество_замен = строка.count(букву_которую_надо_заменить) 
        # функция count в строке считает количество встречающихся букв или фраз
        # например "привет".count("п") => 1

        количество_всех_символов = len(строка) 
        # len(строка) выводит цифру, которая означает длинну строки. так же можно в качестве аргумента указать список (массив)


        print('Количество замен:', количество_замен)
        print('Количество символов в строке:', количество_всех_символов)
        # выводим то что от нас хотят

        новая_строка = строка.replace(букву_которую_надо_заменить, букву_НА_которую_надо_заменить)
        # строка.replace(a, b) заменяет в строке A на B и возвращает новую строку. можно указать количество замен третьим аргументом если это необходимо

        print('Новая строка:', новая_строка)



    def _4():
        """Дана последовательность из n вещественных чисел, начинающаяся с положительного
числа. Определить, какое количество положительных чисел записано в начале
последовательности."""
        количество_чисел = int(input("Количество чисел в последовательности: "))

        количество_положительных_чисел = 0
        считать_числа = True

        for i in range(количество_чисел):
            число = int(input("Введите число: "))
            if число > -1:
                if считать_числа: 
                    количество_положительных_чисел = количество_положительных_чисел + 1
            
            else: считать_числа = False

        print('Количество положительных чисел в начале последовательности:', количество_положительных_чисел)

        return количество_положительных_чисел

    def _6_1():
        
        # 6.1
        import math
        def A(x, y, z): 
            return math.sqrt( abs(x) - math.sqrt(abs(y)) ) / (1 + x * 2 + y * 2)
 
        def B(x, y, z): 
            return y * (math.atan(z) + math.atan(x)) 
        
        def V(a, b): 
            return (a**2) * (b**2)

        x = float(input("Введите x: ")) 
        y = float(input("Введите y: ")) 
        z = float(input("Введите z: ")) 
        
        if A(x, y, z)is None or math.isnan(A(x, y, z)): 
            exit("Не удалось вычислить значение функции A")

        if math.isnan(B(x, y, z)): 
            exit("Не удалось вычислить значение функции B")

        print("Результат:", V(A(x,y,z), B(x,y,z)))

    
    def _6_2():

        # 6.2
        import math
        def A(x, y, z): 
            return math.sqrt( abs(x) - math.sqrt(abs(y)) ) / (1 + x * 2 + y * 2)

        def B(x, y, z): 
            return y * (math.atan(z) + math.atan(x)) 

        def V(a, b): 
            return (a**2) * (b**2)

        def W(a, b): 
            return (a**0.5) - b

        def F(v, w): 
            return 10*v*w - v

        x = float(input("Введите x: ")) 
        y = float(input("Введите y: ")) 
        z = float(input("Введите z: ")) 

        if A(x, y, z)is None or math.isnan(A(x, y, z)): 
            exit("Не удалось вычислить значение функции A")

        if math.isnan(B(x, y, z)): 
            exit("Не удалось вычислить значение функции B")

        a = A(x, y, z)
        b = B(x, y, z)

        print("Результат:", F(V(a, b), W(a, b)))


x = [ # это двумерный массив
    [1,2,3], # это маленький массив внутри массива
    [4,5,6],
    [7,8,9],
] # i = 2; j = 0


        


data = {
    "t": {
        "descr": "Домашнее задание",
        "index": True,
        "baseurl": None # в строку можно добавить %i, оно будет заменено на название функции
    },
}