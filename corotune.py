from functions import file

class polakov: 
    def _2523():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-1.txt')
        symbols = 'qwertyuiopasdfghjklzxcvbnm'.upper()
        for i in symbols:
            data = data.replace(i, ' ')
        
        m = 0
        for i in data.split():
            if int(i)%2: m = max(m, int(i))

        return m

    def _4923(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-196.txt')
        data = data.replace('ZX', '_').replace('ZY', '_')
        data = data.replace('Z', ' ').replace('X', ' ').replace('Y', ' ')

        return len(max(data.split(), key=lambda x: len(x)))
    

    def _4924(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-197.txt')
        data = data.replace('ZXY', '_').replace('ZYX', '_')
        data = data.replace('Z', ' ').replace('X', ' ').replace('Y', ' ')

        return len(max(data.split(), key=lambda x: len(x)))
    

    def _5389(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt')
        data = data.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
        data = data.replace('A11', '_')
        data = data.replace('A', ' ').replace('1', ' ')
        return len(max(data.split(), key=lambda x: len(x)))
    
    # 5392, 5391, 5387

    def _5392(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt')
        data = data.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
        data = data.replace('A1A1A', 'A1A A1A')
        data = data.replace('A1A', '_')
        data = data.replace('A', ' ').replace('1', ' ')
        return len(max(data.split(), key=lambda x: len(x)))
    
    def _5391(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt')
        data = data.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
        data = data.replace('1A1', '_')
        data = data.replace('A', ' ').replace('1', ' ')
        return len(max(data.split(), key=lambda x: len(x)))
    
    def _5387(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt')
        data = data.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
        data = data.replace('A1', '_')
        data = data.replace('A', ' ').replace('1', ' ')
        return len(max(data.split(), key=lambda x: len(x)))

    def _2527():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-1.txt')
        for i in 'QWERTYUIOPASDFGHJKLZXCVBNM02468': data = data.replace(i, ' ')
        return max([int(num) for num in data.split()])
    

    def _5390(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt')
        data = data.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
        data = data.replace('11A', '_')
        data = data.replace('A', ' ').replace('1', ' ')
        return len(max(data.split(), key=lambda x: len(x)))
    
    def _5388(): 
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-215.txt')
        data = data.replace('B', 'A').replace('C', 'A').replace('2', '1').replace('3', '1')
        data = data.replace('1A', '_')
        data = data.replace('A', ' ').replace('1', ' ')
        return len(max(data.split(), key=lambda x: len(x)))


class hw1:
    def _2() -> str:
        def f(x, y, z): 
            """(¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z)"""
            return (not x and y and z) or (not x and not y and z) or (not z and not y and not z)
        
        results = [0, 1]
        result = 'x y z F\n'
        for x in results:
            for y in results: 
                for z in results:
                    r = f(x, y, z)
                    r = 1 if r else 0
                    if r: result += f'{x} {y} {z} {r}\n'
        return result

    def _5(num: int) -> int:
        num = int(num)
        return int(bin(num)[2:][::-1], base=2)
    
    def _14() -> int:
        for base in range(2, 37):
            try: 
                if int('12', base) * int('33', base) == int('406', base): return base
            except ValueError: continue

    def _24():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-230.txt')
        query = '8???54???22'
        found = []
        
        for substr in data.split('ZZ'):
            is_equal = True
            try: int(substr)
            except: continue
            if len(substr) != len(query): continue
            for i, num in enumerate(substr):
                if query[i] == '?': continue
                if query[i] != num: is_equal = False

            found.append(substr) if is_equal else ...

        print(f'Совпадения с {query}: '+', '.join(map(str, found)))
        if len(found) > 1: print(f'\nНайдено {len(found)} совпадений! Выбрано {found[1]}')
        res = []
        ret = 1
        for num in found[1]:
            if int(num) in [1,3,5,7,9]: res.append(int(num))
        for num in res: ret *= num
        return ret


class ex:
    def _5(n: int):
        n = int(n)
        def tobase(n, b):
            d = []
            while n:
                d.append(int(n % b))
                n = n//b
            return ''.join(map(str, d[::-1]))


        # 1
        v = tobase(n, 3)

        # 2
        if int(n)%3 == 0: v = f'1{v}02'
        else:
            q = int(n)%3
            q = q*4
            q = tobase(q, 3)
            v += q

        # 3
        return int(v, 3)

    def _14(n: int):
        s = '7*x*939717 + 27*x*75 + 139*x*7'
        #n = int(n)
        def tobase(n, b):
            d = []
            while n:
                d.append(int(n % b))
                n = n//b
            return ''.join(map(str, d[::-1]))

        res = eval(s.replace('x',n))
        return res, not res%22, tobase(int(n), 23)

    def _17():
        f = file('https://kompege.ru/files/gHQ7ncvzh.txt')
        f = f.split()
        m = []
        for i, v in enumerate(f):
            if not i: continue
            v2 = int(v)
            v1 = int(f[i-1])

            if str(max(v1,v2))[-2:] != '39': continue
            if 4 not in [len(str(abs(v1))), len(str(abs(v2)))] and len(str(abs(v1))) != len(str(abs(v2))):continue
            if (v1+v2)**2 > max(v1,v2)**2: continue
            if len(str(max(v1,v2)).replace('-', '')) != 4: continue
            
            print(v1, v2)
            m.append(v1+v2)
        

        return len(m), max(m)


    def _24():
        f = file('https://kompege.ru/files/HIJpUMRws.txt')
        m, c = 0, 0
        f = f.replace('9', '8').replace('C','A').replace('B', 'A')
        for i, v in enumerate(f):
            v1 = f[i-1]
            v2 = v
            
            if not i: continue

            if v2 == v1:
                m = max(m, c)
                c = 1
            else: 
                c += 1

        return m, c , max(m, c)


class hw2: 
    def _1() -> str:
        def f(x, y, z, w): 
            """    x  ∧  (y  ∧  z ∨  z  ∧  w ∨  y  ∧    ¬ w)."""
            return x and (y and z or z and w or y and not w)
        
        results = [0, 1]
        result = 'x z y w'

        for x in results:
            for y in results: 
                for z in results:
                    for w in results:
                        r = f(x, y, z, w)
                        r = 1 if r else 0
                        if r: print(x,z,y,w, r)
        
        return result
    
    def _2() -> str: 
        d = {
            0: {
                0: ...,
                1: {
                    0: ...,
                    1: 'Б'
                }
            },

            1: 'A'
        }
        return '00: В, 010: Г ---> 2+3 = 5'
    
    
    
    def _3() -> int: 
        r = 400
        avgI = 2 * 1024 * 1024 *8
        # I = doc * r * r * c = doc * 400*400 * c


        new_r = 100
        new_c = 6
        new_avgI = 96 * 1024 *8
        # I = doc * new_r * new_r * new_c = doc * 100 * 100 * 6
        # 96~ = doc * 100 * 100 * 6
        doc = 13.1072 # => подставим
        c = int(avgI / (doc* (400**2)))
        
        return 2**c
    
    def _4() -> int:
        """При регистрации в компьютерной системе каждому пользователю выдаётся
идентификатор, состоящий из 10 символов, первый и последний из которых –
одна из 18 букв, а остальные – цифры (допускается использование 10
десятичных цифр). Каждый такой идентификатор в компьютерной программе
записывается минимально возможным и одинаковым целым количеством байт
(при этом используют посимвольное кодирование; все цифры кодируются
одинаковым и минимально возможным количеством бит, все буквы также
кодируются одинаковым и минимально возможным количеством бит).
Определите объём памяти в байтах, отводимый этой программой для записи 25
идентификаторов."""
        # id_len = 10
        special = 18
        nums = 10

        special_bits = len(bin(special)[2:])
        nums_bits = len(bin(nums)[2:])

        total_id_space = special_bits*2 + nums_bits*8
        total_byte = total_id_space//8 + 1

        return total_byte * 25
    
    
    def _5() -> str:
        def f(x, y, z, w): 
            """    (    x →  y)  ∧  (    y →  z)  ∧  (    z  → w)"""
            return (not x or y) and (not y or z) and (not z or w)
        
        results = [0, 1]
        result = 'z y w x'

        for x in results:
            for y in results: 
                for z in results:
                    for w in results:
                        if not w or x: continue
                        r = f(x, y, z, w)
                        r = 1 if r else 0
                        if r: print(z,y,w,x, r)
        
        return result
    

    def _6(): return hw2._2()

    def _7(): 
        """Для хранения в информационной системе документы сканируются с
разрешением 600 ppi и цветовой системой, содержащей 224 = 16 777 216 цветов.
Методы сжатия изображений не используются. Средний размер
отсканированного документа составляет 16 Мбайт. В целях экономии было
решено перейти на разрешение 300 ppi и цветовую систему, содержащую 64
цвета. Сколько Мбайт будет составлять средний размер документа,
отсканированного с изменёнными параметрами?"""
        
        from math import log2
        o_avg_space = 16 * 1024**2 *8
        o_ppi = 600
        o_color = log2(16_777_216)
        avg_doc = o_avg_space / ((o_ppi**2) * o_color)


        n_ppi = 300
        n_color = log2(64)
        n_avg_space = avg_doc * (n_ppi**2) * n_color
        n_avg_space_mb = n_avg_space / 8 / (1024**2) 

        return n_avg_space_mb
        # return 


    def _8() -> str:
        """При регистрации в компьютерной системе каждому пользователю выдаётся
пароль, состоящий из 6 символов и содержащий только символы из 7-буквенного
набора Н, О, Р, С, Т, У, Х. В базе данных для хранения сведений о каждом
пользователе отведено одинаковое целое число байт, при этом для хранения
сведений о 100 пользователях используется 1400 байт. Для каждого пользователя
хранятся пароль и дополнительные сведения. Для хранения паролей используют
посимвольное кодирование, все символы кодируются одинаковым и минимально
возможным количеством бит. Сколько бит отведено для хранения
дополнительных сведений о каждом пользователе?"""

        l = 6
        q = 7
        q_bit = len(bin(q)[2:])
        token = q_bit*l 
        per_user = 14 * 8

        return per_user - token

    
    def _9() -> str:
        def f(x, y, z, w): 
            """    ((    x →  w) ∨  y  ∧    ¬ z)  ∧  ((    y →    ¬ z) ∨  x  ∧    ¬ w)"""
            return ((not x or w) or y and not z) and ((not y or not z) or x and not w)
        
        results = [0, 1]
        result = 'z w y x -> 0'

        for x in results:
            for y in results: 
                for z in results:
                    for w in results:
                        if [x, y, z, w].count(0) < 2: continue
                        r = f(x, y, z, w)
                        r = 1 if r else 0
                        if r == 0: print(z,w,y,x)
        return result       

    def _10() -> int: 
        """По каналу связи передаются сообщения, содержащие только шесть букв: Т, Е, Н, С, И, В. Для передачи используется двоичный
код, допускающий однозначное декодирование. Кодовые слова для букв известны: Т – 010, Е – 0100, Н – 1100, С – 01000, И – 0110, 
В – 1110. Как можно сократить код для буквы Н, чтобы сохранялось свойство однозначности декодирования? Если таких кодов 
несколько, в качестве ответа указать код наименьшей длины."""
        
        s = 'ТЕНСИВ'
        d = {
            0: {
                0: {
                    0: {
                        0: ...,
                        1: {
                            0: 'С',
                            1: ...
                        }
                    },
                    1: {
                        0: 'Е',
                        1: 'Н'
                    }
                },
                1: {
                    0: 'Т',
                    1: {
                        0: 'И',
                        1: 'В'
                    }
                }
            },
            1: ... # Н
        }

        return 1
    
    def _11() -> int: 
        '''Камера делает фотоснимки 1024×768 пикселей. При этом объём файла с
изображением не может превышать 600 Кбайт, упаковка данных не
производится. Какое максимальное количество цветов можно использовать в
палитре изображения?'''
        
        res = 1024*768
        max_I = 600 * 1024 * 8
        col = max_I/res //1
        return 2**col
    
    def _12() -> int:
        """При регистрации в компьютерной системе каждому пользователю выдаётся
пароль, состоящий из 10 символов, содержащий только символы из набора Н, Е,
П, Р, И, Д, У, М, А, Л, десятичные цифры и специальные символы #, $, @, _, %.
В базе данных для хранения сведений о каждом пользователе отведено
одинаковое и минимально возможное целое число байт. При этом используют 
посимвольное кодирование паролей, все символы кодируют одинаковым и
минимально возможным количеством бит. Кроме собственно пароля, для
каждого пользователя в системе хранятся дополнительные сведения. На
хранение как пароля, так и дополнительных сведений отведено одинаковое для
каждого пользователя целое количество байт. Известно, что для хранения пароля
выделено в байтах РОВНО в 1,5 раза меньше памяти, чем для хранения
дополнительных сведений. Какое минимальное количество байт необходимо
выделить, чтобы сохранить информацию о 22 пользователях? В ответе запишите
только целое число – количество байт."""
        
        l = 10
        alph = 10 + 10 + 5
        alph_bit = len(bin(alph)[2:])
        pwd = (alph_bit * l) // 8 +1 +1 # последний +1 из-за условия, что РОВНО 1.5 раза. а если не добавить +1, то там выйдет дробное число, что НЕДОПУСТИМО в байтах. -1 сделать нельзя иначе не уместимся, так как требуется 6.25 байта
        usd = pwd*1.5

        user = pwd+usd

        return int(user*22) 



data = {
    "polakov": {
        "descr": "Задачи со сборника Полякова",
        "index": True,
        "baseurl": "https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=%i"
    },
    "hw1": {
        "descr": "Домашнее задание от 18 октября 2023 года",
        "index": False,
        "baseurl": None
    },
    "ex": {
        "descr": "Экзамен",
        "index": False,
        "baseurl": None
    },
    "hw2": {
        "descr": "Домашнее задание от 29 октября 2023 года",
        "index": True,
        "baseurl": None
    }
}