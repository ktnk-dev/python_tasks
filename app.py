import corotune
import importlib
class Color: 
    def __init__(self) -> None:
        try: 
            import colorama
            colorama.init()
            from colorama import Fore as C
            self.support = True
            self.color = C

        except ImportError: 
            print('ERROR > библиотека Colorama не установлена!')
            self.support = False

    def red(self, light = True): 
        if not light: return self.color.RED if self.support else ''
        else: return self.color.LIGHTRED_EX if self.support else ''

    def yellow(self, light = True):
        if not light: return self.color.YELLOW if self.support else ''
        else: return self.color.LIGHTYELLOW_EX if self.support else ''

    def green(self, light = True):
        if not light: return self.color.GREEN if self.support else ''
        else: return self.color.LIGHTGREEN_EX if self.support else ''

    def cyan(self, light = True):
        if not light: return self.color.CYAN if self.support else ''
        else: return self.color.LIGHTCYAN_EX if self.support else ''

    def blue(self, light = True):
        if not light: return self.color.BLUE if self.support else ''
        else: return self.color.LIGHTBLUE_EX if self.support else ''

    def magenta(self, light = True):
        if not light: return self.color.MAGENTA if self.support else ''
        else: return self.color.LIGHTMAGENTA_EX if self.support else ''

    def gray(self):
        return self.color.LIGHTBLACK_EX if self.support else ''
    
    def reset(self):
        return self.color.RESET if self.support else ''
        
color = Color()         
        


def load_db():
    db = {}
    with open('corotune.py', 'r', encoding='utf-8') as file:
        core = file.read().split(f'def func_')
        for func in core:
            try:
                num = int(func.split('(')[0])
                db[num] = f'corotune.func_{num}'
            except ValueError: continue
    return db


db = load_db()
args = ['-loop', '-code']


def get_hash():
    with open('corotune.py', 'r', encoding='utf-8') as file:
        result = hash(file.read())
    return str(hex(result))[3:10]

def run(num):
    try:
        data = input(f"{color.yellow()}{get_hash()}{color.gray()} > {color.cyan()}{num}{color.gray()} > {color.magenta()}")
        global corotune
        corotune = importlib.reload(corotune)
        if data == '': return True
        try:
            result = eval(f'{db[num]}(data)')
            print(f'{color.green()}{result}\n{color.reset()}')
            return True
        except Exception as e:
            print(f'{color.red()}{e}{color.reset()}')
            return True
    except KeyboardInterrupt: return False


def show_code(num):
    with open('corotune.py', 'r', encoding='utf-8') as file:
        core = file.read().split(f'def func_')
        for func in core:
            try:
                if int(func.split('(')[0]) == num: 
                    print(f'{color.green()}def func_{func}print(func_{num}(input())){color.reset()}\n')
            except ValueError: continue


print(f'\n\n{color.gray()}--- {color.reset()}Задания {color.gray()}---')
print(f'{color.yellow()}Доступные задачи: {color.green()}{f"{color.gray()}, {color.green()}".join(map(str, db.keys()))}')
print(f'{color.yellow()}Доступные аргументы: {color.green()}{f"{color.gray()}, {color.green()}".join(args)}')
print(f'{color.gray()}Укажите номер задачи, при необходимости можно использовать аргумент. Например:{color.magenta(False)} 123 {color.yellow(False)}-loop{color.reset()}\n')
while True:
    db = load_db()
    try: 
        u = input(f'{color.yellow()}{get_hash()}{color.gray()} > {color.cyan()}mainloop {color.gray()}> {color.magenta()}').split(' ')
        num = int(u[0])
        try: arg = u[1]
        except: arg = '-loop'
    except ValueError: 
        print(f'{color.red()}Это не номер')
        continue
    except KeyboardInterrupt:
        exit()


    if num not in db.keys():
        print(f'{color.red()}Неправильный номер задания!')
        continue

    if arg == '-loop': 
        while run(num): pass
    elif arg == '-code': show_code(num)
    else: run(num)
