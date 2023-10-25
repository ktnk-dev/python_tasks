from functions import file

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
            

        


data = {
    'polakov': {
        'descr': 'Тестовые задачи',
        'baseurl': 'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=%i',
        'index': True
    },
    'hw1': {
        'descr': 'Домашнее задание от 18 октября 2023 года',
        'index': False,
        'baseurl': None,

    },
    'ex': {
        'descr': 'Экзамен',
        'index': True,
        'baseurl': None,
    }
}
