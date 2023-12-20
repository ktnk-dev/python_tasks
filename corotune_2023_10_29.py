from functions import file

class hw:
    def _1() -> dict: 
        """Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Например, маске 123*4?5 соответствуют числа 123405 и 12300425. 
Найдите все числа, меньшие 1012, соответствующие маске 123?4*5679 и делящиеся без остатка на 4013. В качестве ответа приведите все найденные числа в порядке возрастания, справа от каждого числа выведите результат его деления на 401"""
        
        import re
        query = r'123.4.*?5679'
        result = {}

        for number in range(10**9, 10**12):
            if re.match(query, str(number)):
                if number%4013 == 0: result[number] = number//4013

        return result
    
    def _1_alt() -> dict:
        query = '123-4_5679'
        #        123-4___5679
        result = {}

        def add_result(number): 
            result[number] = number//4013

        for first_query in range(10):
            current = query.replace('-', str(first_query))
            number = int(current.replace('_', ''))
            
            if number%4013 == 0: add_result(number)
            
            for limit_second_query in range(1, 4):
                for second_query in range(10**limit_second_query):
                    number = int(current.replace('_', str(second_query).rjust(limit_second_query, '0')))
                    if number%4013 == 0: add_result(number)

        return result

    def _2() -> int: ...
    
class lesson:
    def _5035() -> dict:

        nums = '012'
        result = {}

        for z in nums:
            for x in nums:
                for c in nums:
                    for v in nums: 
                        for b in nums:
                            cur = f'2{z}1{x}2{c}1{v}2{b}1'
                            num = int(cur, 3)
                            if num%148 == 0: print(num, num//148)
                            

        return result
    
    def _4988() -> dict:
        allowed = [i for i in '1234567890'] 
        allowed.append('')
        print(allowed)

        nums = [i for i in '1234567890']
        result = {}

        for x in nums:
            for y in allowed:
                for z in allowed:
                    match = int(f'123{y}{z}567{x}')
                    if match%169 == 0: result[match] = match//169

        return result

    # 5062, 5144, 5272(9?), 5651

    def _5062() -> dict:
        import re

        def s(n, include = True):
            for num in range(1 if include else 2, int(n**.5)+1):
                if n%num == 0:
                    yield [n//num, num]

        def is_simple(num):
            for _ in s(num, False): return False
            return True

        result = {}

        num = 3850000-1
        while len(result.keys()) < 10:
            num += 1
            num_mul = set()
            for mul in s(num, False):
                num_mul.add(mul[1])   
                num_mul.add(mul[0])   

            true_mul = [num for num in num_mul if is_simple(num)]

            true_mul_str = ''.join(map(str, true_mul))

            if re.match(r'27.*1.1$', true_mul_str): 
                result[num] = max(true_mul)
                print(num, max(true_mul), true_mul_str, true_mul)

        
        return result



        


data = {
    "hw": {
        "descr": "Домашнее задание от 2023.11.29",
        "index": True,
        "baseurl": None # в строку можно добавить %i, оно будет заменено на название функции
    },
    "lesson": {
        "descr": "Урок от 2023.11.29",
        "index": True,
        "baseurl": None # в строку можно добавить %i, оно будет заменено на название функции
    }, 
}