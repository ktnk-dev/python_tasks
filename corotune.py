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






class l2023_12_13:
    def _5062(): # 5279, 5651, 5144
        
        import re
        def find_mul(n, include = True):
            for num in range(1 if include else 2, int(n**.5)+1):
                if n%num == 0:
                    yield n//num
                    yield num
                    
        def is_simple(n):
            for _ in find_mul(n, False): return False
            return True
        
        c = 0
        n = 3850000+1
        while c != 5:
            mul_list = [mul for mul in find_mul(n, False) if is_simple(mul)]
            mul_str = ''.join(map(str, mul_list))
            if re.match(r'27.*?1.1$', mul_str):
                print(n, max(mul_list))
                c += 1              
            n += 1
            
    def _5279():
        import re
        def find_mul(n, include = True):
            for num in range(1 if include else 2, int(n**.5)+1):
                if n%num == 0:
                    yield n//num
                    yield num
                    
        def is_simple(n):
            for _ in find_mul(n, False): return False
            return True
        
        c = 0
        n = 65000
        while c != 7:
            n += 1
            if not re.match(r'6.*?97.*?5.', str(n)): continue

            mul_list = [mul for mul in find_mul(n, True) if mul%2 == 0]
            if len(mul_list) < 4: continue

            print(n, sum(mul_list))
            c += 1           

    def _5651():
        import re
        def find_mul(n, include = True):
            for num in range(1 if include else 2, int(n**.5)+1):
                if n%num == 0:
                    yield n//num
                    yield num
                    
        def is_simple(n):
            for _ in find_mul(n, False): return False
            return True       

        # 3****52?
        # 9999999
        for n in range(1000000, 9999999+1):
            s = str(n)
            if not re.match(r'3.*?52.$', s): continue
            if n**.5 != int(n**.5): continue
            muls = list(find_mul(n))
            muls.remove(n)
            print(n, max(muls))
            
    def _5144(): 
        import re
        def find_mul(n, include = True):
            for num in range(1 if include else 2, int(n**.5)+1):
                if n%num == 0:
                    yield n//num
                    yield num
                    
        def is_simple(n):
            for _ in find_mul(n, False): return False
            return True

        def N(k): return 750_000 + k
        
        
        c = 0
        r = -1
        while c != 5:
            r += 1
            n = N(r)
            
            mul_list = set([mul for mul in find_mul(n, True) if mul%2 == 0])
            if len(mul_list)%2 == 0: continue
            print(r, len(mul_list))
           
                
            c += 1              
            
            



class ex:
    def _2():
        def f(x, y, z, w):
            #       
            return ((not(x) or y) or (not(z) or w)) and not (not(x) or w)
        s = [0,1]
        print('x w z y >')
        for _ in s:
            for x in s:
                for y in s:
                    for z in s:
                        for w in s:
                            R = int(f(x,y,z,w))
                            print(z,w,x,y, R) if _ == R else ...
            print("z w x y")

    
    def _7():
        res = 1200*640
        colors = 9 # 257 colors => 256 bin 8, 257 bin 9

        pack = 512

        return (res * colors * pack) / (2**23)        
    
    def _5():
        
        def tobase(n, b):
            d = []
            while n:
                d.append(int(n % b))
                n = n//b
            return ''.join(map(str, d[::-1]))

        def alg(n):
            # 1
            v = tobase(n, 3)

            # 2
            if int(v)%4 == 0: v += v[-3:]
            else:
                q = int(v)%3
                q = q*4
                q = tobase(q, 3)
                v += q

            # 3
            return int(v, 3)
        n = 0
        p = True
        m = 0
        while p:
            n += 1
            r = alg(n)
            
            if n > 10000: return f'max {m}'

            if r < 127:
                print(n, r)
                m = max(m, r)
                
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
        f = file('https://kompege.ru/files/bZ78sOnak.txt')
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
        f = file('https://kompege.ru/files/oJLokDg_n.txt')
        f = f.replace('A','(').replace('B',')')
        q = f
        for d in 'QWERTYUIOPSDFGHJKLZXCVNM':
            f = f.replace(d, '.')
    
        m, c = 0, 0
        res = 0

        for q in f:
            if q == '.': continue
            if q == '(': res += 1
            if q == ')': res -= 1

            
        print (res)
        
        return m
                
            
            

        


data = {
    'polakov': {
        'descr': 'Тестовые задачи',
        'baseurl': 'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=%i',
        'index': True
    },
    'l2023_12_13': {
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
