from functions import file

class polakov:
    def _2(string: str) -> int:
        return f'123: {string}'
    
    def _file(filename: str) -> int:
        return file(filename)[:50]+'...'
    
    def _add(a, b) -> int:
        return int(a)+int(b)


    
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




data = {
    'polakov': {
        'descr': 'Задачи с сайта полякова',
        'baseurl': None,
        'index': True
    },

    'hw1': {
        'descr': 'Домашнее задание от 18 октября 2023 года',
        'index': False
    }
}