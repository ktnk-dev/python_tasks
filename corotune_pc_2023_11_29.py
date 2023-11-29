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
    
    def _6782():
        d = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-264.txt')
        from string import ascii_uppercase
        for sym in ascii_uppercase: d = d.replace(sym, '_')
        for num in '1234567890': d = d.replace(num, '*')
        c, m = 0, 0

        for i, v in enumerate(d[:-2]):
            s1 = v
            s2 = d[i+1]
            if s1 == s2: 
                m = max(c, m)
                c = 1
            else: c += 1

        return max(c, m)

    def _6675():
        d = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-263.txt').split('Y')
        m = 0
        for i, _ in enumerate(d):
            m = max(m, sum([len(pl) for pl in d[i:i+151]])+150)

        return m


    def _2841():

        result = {}

        def s(n):
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    

        for i in range(106732567, 152673836+1):
            if (i**0.5)%1 == 0: 
                lst = set()
                for res in s(i):
                    [lst.add(q) for q in res]
                    if len(lst) > 4: break
                if len(lst) ==  3: 
                    result[i] = max(lst)

        return result
    
    def _2858():
        result = []
        def s(n):
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]

        
        for i in range(135790, 163228+1):
            lst = set()
            for res in s(i):
                lst.add(res[0])
                lst.add(res[1])
                
            if sum(list(lst)) > 460000: 
                result.append(f'{len(lst)} {sum(list(lst))}')

        return result

    def _2859():
        result = {}
        def s(n):
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    

        for i in range(81234, 134689+1):
            if (i**0.5)%1 == 0: 
                lst = set()
                for res in s(i):
                    lst.add(res[0])
                    lst.add(res[1])
                    if len(lst) > 4: break

                if len(lst) ==  3: 
                    result[min(lst)] = max(lst)

        return result #2927 2884
    
    def _2927():
        result = {}
        def s(n):
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    
        for i in range(102714, 102725+1):
            lst = set()
            for res in s(i):
                lst.add(res[0])
                lst.add(res[1])
                if len(lst) > 5: break

            if len(lst) == 4: 
                result[sorted(lst)[-2]] = sorted(lst)[-1]

        return result 
    
    def _2884():
        result = []
        def s(n):
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    
        for i in range(78920, 92430+1):
            if (i**0.5)%1 != 0: continue
            lst = set()
            for res in s(i):
                lst.add(res[0])
                lst.add(res[1])
                if len(lst) > 6: break

            if len(lst) == 5: 
                result.append(i)

        return len(result), min(result) 
# 3159 3160

    def _3159():
        result = {}
        def s(n):
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    
        for i in range(500000, 1000000+1):
            lst = set()
            for res in s(i):
                if res[1]-res[0] < 90:
                    lst.add(res[0])
                    lst.add(res[1])

            if len(lst) > 3*2 -1: result[i] = max(lst)

        return result

    def _3160():
        result = {}
        def s(n):
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    
        for i in range(1000000, 1500000+1):
            lst = set()
            for res in s(i):
                if res[1]-res[0] < 110:
                    lst.add(res[0])
                    lst.add(res[1])

            if len(lst) > 3*2 -1: result[i] = max(lst)

        return result
    
    def _3777():
        result = {}
        def s(n):
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    
        for i in range(55_000_000, 60_000_000+1):
            lst = set()
            for res in s(i):
                if res[1]%2 == 1: lst.add(res[1])
                if res[0]%2 == 1: lst.add(res[0])
                if len(lst) > 5: break

            if len(lst) == 5: 
                print(f'{i} {max(lst)} {lst}')
                result[i] = max(lst)

        return result
    
    def _2928():
        result = {}
        def s(n):
            for i in range(1, int(n**0.5)+1):
                if n%i == 0:
                    yield [i, n//i]
                    
        for i in range(126849, 126871+1):
            lst = set()
            for res in s(i):
                lst.add(res[1])
                lst.add(res[0])
                if len(lst) > 4: break

            if len(lst) == 4:
                r = sorted(lst) 
                # print(f'{i}: {lst}')
                result[i] = [r[-2], r[-1]]

        return result



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


class l8:
    def _93():
        from itertools import product, permutations
        c = 0
        for d in permutations("ПАЙЩИК", 6):
            s = ''.join(d)

            if s[0] != 'Й' and 'ИА' not in s: c += 1

        return c
    
    def _108():
        from itertools import product, permutations
        od = 'ОЕА'
        nd = 'KMT'
        al = []
        for o in od:
            for n in od:
                al.append(f'{o}{n}')

        for o in nd:
            for n in nd:
                al.append(f'{o}{n}')

        c = 0
        for d in permutations('КОМЕТА', 6):
            s = ''.join(d).replace('М', 'К').replace('Т', 'К').replace('Е', 'О').replace('А', 'О')
            if 'КК' in s or 'ОО' in s: continue
            
            c += 1

        return c
    
    def _115(): 
        from itertools import product, permutations
        c = 0
        for d in set(permutations('МАРТА')):
            s = ''.join(d)
            if 'АА' not in s: c+= 1
        

    def _118():
        from itertools import product, permutations
        c = 0
        for d in set(permutations('АВРОРА')): 
            s = ''.join(d)
            if 'АА' in s or 'РР' in s: continue
            c += 1
        
        return c
    
    def _125():
        from itertools import product, permutations
        return len(set(permutations('ТРАТАТА')))
    
    def _135():
        from itertools import product, permutations
        c = 0
        for d in set(permutations('АВРОРА')): 
            s = ''.join(d)
            if 'АА' in s: continue
            c += 1      
        return c
    
    def _143():
        c = 0
        from itertools import product, permutations
        for d in product('RUSTAM', repeat=6):
            s = ''.join(d)
            if s.count('R') + s.count('S') + s.count('T') + s.count('M') >= 3: c += 1

        return c

    def _179():
        from itertools import product, permutations
        for i, d in enumerate(product('щогба', repeat=6)): 
            s = ''.join(d)
            if s == 'общага': return i+1

    def _193():
        c = 0
        from itertools import product, permutations
        for i, d in enumerate(product('01234', repeat=6)): 
            d = ''.join(d)
            if d[0] == '3' and int(d, 5)%2 == 0: c+=1

        return c

    def _200():
        c = 0
        from itertools import product, permutations
        for i, d in enumerate(product('0123456789', repeat=3)): 
            d = ''.join(d)
            if d[0] != '0': 
                if int(d[2]) >= int(d[1]) >= int(d[0]):
                    c+=1

        return c
    
    def _205():
        c = 0
        from itertools import product, permutations
        for i, d in enumerate(product('012345', repeat=5)): 
            d = ''.join(d)
            s = d.replace('2','0').replace('4','0').replace('3','1').replace('5','1')
            if d[0] != '0': 
                if '00' in s or '11' in s: continue
                c += 1
        return c
    
    def _207(): 
        c = 0
        from itertools import product, permutations
        w = {
            'р': 'жмдн',
            'е': 'ио'
        }
        for i, d in enumerate(permutations('режимдно', 6)): 
            d = ''.join(d)
            s = d
            for k, v in w.items():
                for let in v: s = s.replace(let, k)
            
            if s[0] == 'р' and s[1] == 'е' and s[5] == 'е': c+= 1
        return c
    
    def _213(): 
        c = 0
        from itertools import product, permutations
        w = { 'ю': 'и' }
        for i, d in enumerate(permutations('тьюринг', 6)): 
            d = ''.join(d)
            s = d
            for k, v in w.items():
                for let in v: s = s.replace(let, k)
            
            if s[0] != 'ь': 
                if 'юь' not in s:
                    c+=1
        return c


    def _214(): 
        c = 0
        from itertools import product, permutations
        for i, d in enumerate(permutations('вайфу', 4)): 
            d = ''.join(d)  
            if d[0] != 'й': 
                if 'вф' not in d and 'фв' not in d:
                    c+=1
        return c
    
# СПБ гос уник (+90); Политех петра великого; 

class l8_hw1: 
    def _224(): 
        """Евгения составляет 4-значные числа в 8-ичной системе счисления. Числа должны начинаться с чётной цифры, и цифры в них располагаются в невозрастающем порядке. Сколько различных чисел может составить Евгения?"""

        c = 0
        from itertools import product, permutations
        for d in product('01234567', repeat=4): 
            d = ''.join(d)
            if d[0] != '0': 
                if int(d[0], 8)%2 == 0: 
                    if d[0] >= d[1] >= d[2] >= d[3]: c += 1
        return c
    
    def _229(): 
        """Определите количество семизначных чисел, записанных в семеричной системе счисления, учитывая, что числа не могут начинаться с цифр 3 и 5 и не должны содержать сочетания цифр 22 и 44 одновременно."""

        c = 0
        from itertools import product, permutations
        for d in product('0123456', repeat=7): 
            d = ''.join(d)
            if d[0] != '0' and d[0] != '3' and d[0] != '5': 
                if ('22' not in d) and ('44' not in d): c += 1
        return c

    def _225(): 
        """Полина составляет 5-значные числа в 5-ичной системе счисления, которые содержат не более 3 чётных цифр. Сколько различных чисел может составить Полина?"""

        c = 0
        odd = '02468'
        from itertools import product, permutations
        for d in product('01234', repeat=5): 
            d = ''.join(d)
            odd_count = 0
            if d[0] != '0': 
                for num in odd: odd_count += str(int(d, 5)).count(num)
                if odd_count < 4: c += 1

        return c

    def _233(): 
        """Определите количество семизначных чисел, записанных в девятеричной системе счисления, учитывая, что числа не могут начинаться с цифр 2, 4 и 6 и не должны заканчиваться на тройку одинаковых цифр (например, на 000)"""
        
        c = 0
        from itertools import product, permutations
        for d in product('012345678', repeat=7): 
            d = ''.join(d)
            if d[0] not in '0246':  
                if d[-1] == d[-2] == d[-3]: continue
                c += 1

        return c 

class hw9:
    def _1():
        def f(x, y, z, w): 
            """     ¬  (    x →  z) ∨  (y ≡  w) ∨  y"""
            return not (not x or z) or (y == w) or y
        
        results = [0, 1]
        result = 'x z w y'

        for x in results:
            for y in results: 
                for z in results:
                    for w in results:
                        r = f(x, y, z, w)
                        r = 1 if r else 0
                        if r == 0: print(x,z,w,y, r)
        
        return result
    
    def _2():
        q = {
            0:{
                0: 'М',
                1: {
                    0: 'Я',
                    1: {
                        0: ...,
                        1: 'Г'
                    }
                }
            },
            1:{
                0: {
                    0: 'P',
                    1: 'Б',
                },
                1: 'A'
            },
        }

        return 4+3+2+2+2
    

    def _3():
        def func(num):
            # 1
            bin_num = bin(num)[2:]
            print(f'{num}: {bin_num}')

            # 2
            for _ in range(3):
                count_0 = bin_num.count('0')
                count_1 = bin_num.count('1')

                if count_0 == count_1: bin_num += bin_num[-1]
                if count_0 >  count_1: bin_num += '1'
                if count_0 <  count_1: bin_num += '0'
            
            # 3
            print(f'{num}: -> {bin_num}')
            return int(bin_num, 2)
        
        for i in list(range(1, 100))[::-1]:
            q = func(i)
            print(f'query: {i} -> {q}')
            if q%2 == 0 and q%4 != 0: return i


    def _4():
        orig = 1 * 1 * 1 * 1
        new = 2 * 1/1.5 * 1 *1

        orig_ch = 30
        new_ch = orig_ch/4

        return new*new_ch

    def _5():
        from itertools import product, permutations
        c = 0
        for d in sorted (product('МАРТ', repeat=4)):
            s = ''.join(d)
            if c: c+=1
            if s == 'МАРТ': c = 1
            if s == 'РАМТ': return c



    def _6():
        ln = 11
        al = len(bin(6)[2:])
        space = al*ln // 8 +1

        return space*20

    def _7():
        def tobase(n, b):
            d = []
            while n:
                d.append(int(n % b))
                n = n//b
            return ''.join(map(str, d[::-1]))
        
        total = [tobase(188, base) for base in list(range(2,11))]
        passes_base = []

        for base, num in enumerate(total):
            base += 2
            last = '0'
            passed = True
            for sym in num:
                if sym >= last: last = sym
                else: passed = False
            
            if passed: passes_base.append(base)

        return sum(passes_base)
        

    def _8():
        f = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-181.txt').split('.')
        x = 0
        for i, v in enumerate(f):
            try:
                q = len(f[i])+len(f[i+1])+len(f[i+2])+len(f[i+3])+len(f[i+4])+4
                x = max(x, q)
                # print(i, q)
            except: pass
            


        return max(x, q)
                
    def _9():
        def tobase(n, b):
            d = []
            while n:
                d.append(int(n % b))
                n = n//b
            return ''.join(map(str, d[::-1]))
        
        from itertools import product, permutations
        c = 0
        v = 0
        for d in product('0123456789', repeat=5):
            s = ''.join(d)
            if s[0] == '0': continue

            v += 1

            psd = True
            for index, num in enumerate(s):
                if index%2 == 0 and int(num)%2 == 0: continue
                if index%2 == 1 and int(num)%3 == 0: continue
                psd = False
            if psd: 
                c+=1
                # print(v, c, s) if c < 666 else ...
                

        return c, v
                


    def _10():
        from itertools import product, permutations
        c = 0
        q = [0, '']
        for d in sorted (product('мангуст', repeat=6)):
            s = ''.join(d)
            c+=1
            if s[0] != 'у':
                if s.count('м') == 2: 
                    if s.count('г') <= 1: 
                        q = [c, s]
        return q
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
        "index": False,
        "baseurl": None
    },
    "hw9": {
        "descr": "Домашнее задание от 29 октября 2023 года",
        "index": True,
        "baseurl": None
    },
    "l8": {
        "descr": "Задания от 30 октября 2023 года | Тема 8",
        "index": False,
        "baseurl": None
    },
    "l8_hw1": {
        "descr": "Повторение | Тема 8",
        "index": False,
        "baseurl": None
    }
}