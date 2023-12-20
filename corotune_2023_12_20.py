from functions import file

class hw_2023_12_20: # 6782, 6789
    baseurl = 'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=%i'

    def _6782():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-264.txt').lower()
        for q in 'qwertyuiopasdfghjklzxcvbnm': data = data.replace(q, '<')
        for q in '1234567890': data = data.replace(q, '>')

        while '>>' in data and '<<' in data:
            data = data.replace('>>', '> >')
            data = data.replace('<<', '< <')
        
        values = [len(substr) for substr in data.split()]

        return max(values)


    def _6789():
        import re

        mask = r'12.*?34.5$'
        #    min 12_  0000
        #    max 10**8

        result = {}

        for num in range(2025, 10**8, 2025):
            if re.match(mask, str(num)):
                if num%2025 == 0:
                    result[num] = num//2025
                    print(num, num//2025)

        return result


class l_2023_12_20: # 6184, 6168, 6606, 6759, 6757, 6758б 6785
    baseurl = 'https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=%i'
    
    def _6184():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-seq/17-363.txt').split()
        
        new_list = []


        for index in range(len(data)):
            number = data[index]
            for q in '02468': number = number.replace(q, '+')
            for q in '13579': number = number.replace(q, '-')
            if number.count('+') == number.count('-'): new_list.append(int(data[index]))
        
        result = []
        for index in range(len(data)-1):
            first = data[index]
            second = data[index+1]

            if min(first) > max(second) and int(first)+int(second) <= max(new_list):
                result.append(int(first)+int(second))

        return len(result), max(result)


    def _6168():
        import re

        mask = r'9.979.*?8$'

        for num in range(50068, 10**10, 50068):
            if re.match(mask, str(num)):
                if str(num).count('0'):
                    print(num, num//2025)


    def _6606():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-sym/24-261.txt').lower()
        data = data.replace('ea', '__')
        data = data.replace('npc', '___')
        for q in 'qwertyuiopasdfghjklzxcvbnm': data = data.replace(q, ' ')

        return max([len(sub) for sub in data.split()])
    
    def _6759():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-seq/17-381.txt').split()
        
        result = []
        new_result = []

        for num in data:
            if len(str(abs(int(num)))) != 4: continue
            if num[-2:] != '39': continue
            new_result.append(int(num))


        for index in range(len(data)-1):
            first = int(data[index])
            second = int(data[index+1])
            
            lens = [len(str(abs(first))), len(str(abs(second)))]
            if lens.count(4) != 1: continue
            
            summ = (first+second)**2
            if summ > max(new_result)**2 : continue

            result.append(first+second)


        return len(result), max(result)


    def _6757():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-seq/17-379.txt').split()
        
        new_list = []
        for index in range(len(data)):
            number = data[index]
            if number[-2:] == '15': new_list.append(int(number))
        
        result = []
        for index in range(len(data)-2):
            first = data[index]
            second = data[index+1]
            third = data[index+2]

            lens = [len(str(abs(int(first)))), len(str(abs(int(second)))), len(str(abs(int(third))))]
            if lens.count(4) != 1: continue

            if sum(map(int, [first, second, third])) < max(new_list): continue

            result.append(sum(map(int, [first, second, third])))


        return len(result), max(result)
    


    def _6758():
        data = file('https://kpolyakov.spb.ru/cms/files/ege-seq/17-380.txt').split()
        
        new_list = []
        for index in range(len(data)):
            number = data[index]
            if number[-2:] == '25': new_list.append(int(number))
        
        result = []
        for index in range(len(data)-2):
            first = data[index]
            second = data[index+1]
            third = data[index+2]

            lens = [len(str(abs(int(first)))), len(str(abs(int(second)))), len(str(abs(int(third))))]
            if lens.count(4) > 2: continue

            if sum(map(int, [first, second, third])) > max(new_list): continue

            result.append(sum(map(int, [first, second, third])))


        return len(result), max(result)
    
    def _6785():


        result = {}
        def check(number):
            num = int(number)
            if num%13 == 0: 
                # print(num, num//13)
                result[num] = num//13

        mask = '24_68?35'
         # max  24__68?35
         # max  100000000
        
        
        odd_nums = '02468'
        allowed = []

        for n1 in odd_nums: 
            allowed.append(f'{n1}')
            for n2 in odd_nums: 
                allowed.append(f'{n1}{n2}')


        print(allowed)

        for question in '39':
            current_mask = mask.replace('?', question)

            check(current_mask.replace('_', ''))

            for point in allowed: check(current_mask.replace('_', point))


        for num in sorted(result.keys(), key = lambda x: int(x)):
            print(num, result[num])