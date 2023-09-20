
class Color: 
    def __init__(self, force_unsupport = False) -> None:
        try: 
            import colorama
            colorama.init()
            from colorama import Fore as C
            self.support = True
            self.color = C

        except ImportError: 
            print('ERROR > библиотека Colorama не установлена!')
            self.support = False

        if force_unsupport: self.support = False

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
        
color = Color(True)         
        
def get_hash():
    with open('corotune.py', 'r', encoding='utf-8') as file:
        result = hash(file.read())
    return str(hex(result))[3:10]


def get_inputs(num): 
    with open('corotune.py', 'r', encoding='utf-8') as file:
        core = file.read().split(f'def func_')
        for func in core:
            try:
                if int(func.split('(')[0]) == num: 
                    return len(func.split('(')[1].split(')')[0].split(','))
            except ValueError: continue


def show_code(num, var = False):
    with open('corotune.py', 'r', encoding='utf-8') as file:
        core = file.read().split(f'def func_')
        for func in core:
            try:
                if int(func.split('(')[0]) == num: 
                    response = f'{color.green()}def func_{func}print(func_{num}({", ".join(["input()"]*get_inputs(num))})){color.reset()}'
                    if not var: print(f'{response}\n')
                    else: return response
            except ValueError: continue


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



