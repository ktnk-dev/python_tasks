class Result:
    def __init__(self, passed, value) -> None:
        self.passed = passed
        if passed: self.result = value
        else: self.error = value

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
    
color = Color()

def lim(c: str = '', d: str = '>') -> str: return f'{color.gray()}{d}{c}'

def file(file_string: str) -> str:
    if 'http://' in file_string or 'https://' in file_string:
        import requests
        print(f'{color.blue()}Downloading file:{color.cyan()} {file_string.split("/")[-1]}{color.magenta()}')
        data = requests.get(file_string).text

    else: 
        with open(file_string, 'r', encoding='utf-8') as local_file: data = local_file.read()
        print(f'{color.cyan()}Loaded local file:{color.cyan()} {file_string}{color.magenta()}')

    return data

def check(result, answer):
    print(f'\n{color.gray()}*{color.cyan()} Your answer:{color.magenta()} {result}')
    print(f'{color.gray()}*{color.blue()} True answer:{color.magenta()} {answer}')
    if result == answer: print(f'{color.gray()}*{color.blue()} {color.green()}100% {color.gray()}|{color.green()} Pass')
    elif str(result) == str(answer): print(f'{color.gray()}*{color.blue()} {color.green()}100% {color.gray()}|{color.yellow()} Types are not same')
    else:
        from difflib import SequenceMatcher
        compare_ratio = round(SequenceMatcher(None, str(result), str(answer)).ratio()*100)
        if compare_ratio > 80: print(f'{color.gray()}*{color.blue()} {color.yellow()}{compare_ratio}% {color.gray()}|{color.red()} Failed')
        else: print(f'{color.gray()}*{color.blue()} {color.red()}{compare_ratio}% {color.gray()}|{color.red()} Failed')
    print(color.magenta())

def iterator(data, lenght):
    from itertools import product
    for result in product(data, repeat = lenght):
        yield result

try: import corotune
except ImportError: 
    print(f'\n{color.red()}Corotune does not exist! Creating...\n')
    with open('./corotune.py', 'w', encoding='utf-8') as corotune_file: corotune_file.write(file('https://raw.githubusercontent.com/ktnk-dev/python_tasks/main/corotune.py'))
    import corotune
    print(f'{color.green()}Example corotune created')

import inspect
import importlib

def get_corotune_data() -> dict:
    classes = inspect.getmembers(corotune, inspect.isclass)
    result = {}
    for (class_name, data) in classes:
        try: descr = data.descr
        except: descr = 'No description'

        try: baseurl = data.baseurl
        except: baseurl = None

        try: index = data.index
        except: index = True

        result[class_name] = {
            'descr': descr,
            'baseurl': baseurl,
            'index': index
        }
    return result



def info(class_name: str, task_id = False) -> list:
        global corotune 
        corotune = importlib.reload(corotune)
        data = eval(f'corotune.{class_name}.__dict__')
        if not task_id: return [name[1:] for name in data if name[0] == '_' and name[1] != '_'] 
        else: 
            try:
                return {
                    'args': inspect.getfullargspec(data[f'_{task_id}']).args,
                    'code': inspect.getsource(data[f'_{task_id}']),
                    'doc': eval(f'corotune.{class_name}._{task_id}.__doc__')
                }
            except: return False

def run(class_name: str, task_id, args: list = []) -> Result:
    target = info(class_name, task_id)
    if not target: return Result(False, 'Unknown "task_id" or "class_name"')
    if args == []:
        for arg in target['args']: args.append(str(input(f'{color.yellow()}{class_name} {lim(color.cyan())} {task_id} {lim(color.green())} {arg} {lim(color.magenta())} ')))
    elif len(args) != len(target['args']): return Result(False, 'Arguments count error')
    
    global corotune 
    corotune = importlib.reload(corotune)

    try: return Result(True, eval(f'corotune.{class_name}._{task_id}({", ".join([f"args[{i}]" for i, v in enumerate(args) ])})'))
    except Exception as e: return Result(False, e)


def code(class_name: str, task_id) -> str:
    func = info(class_name, task_id)
    base = f'class Solution:\n{func["code"].replace(f"def _{task_id}", "def run")}\n'
    if 'file(' in func['code'] or 'file (' in func['code']: base = f'{inspect.getsource(file).replace("print", "# print")}\n{base}'
    if 'check(' in func['code'] or 'check (' in func['code']: base = f'def check(a, b): return a\n{base}'
    
    base += f'result = Solution.run({",".join(["input()" for _ in func["args"]])})\nprint(result)'
    return base

def share_class(class_name):
    source_code = inspect.getsource(eval(f'corotune.{class_name}'))
    merge_info = {
        'name': class_name,
    }

    with open('merge.py', 'w', encoding='utf-8') as file: file.write(f'{source_code}\n\n'+f'info = {merge_info}')
    return Result(True, f'"merge.py" created')



def merge_class():
    global corotune 
    corotune = importlib.reload(corotune)
    import json, os
    try: import merge
    except ImportError: return Result(False, '"merge.py" was not found')
    info = merge.info
    source_code = inspect.getsource(eval(f'merge.{info["name"]}'))
    
    new_corotune = 'from functions import file, check\n\n'
    
    for class_name in get_corotune_data().keys():
        new_corotune += inspect.getsource(eval(f'corotune.{class_name}')) + '\n\n'

    new_corotune += source_code + '\n\n'


    with open('corotune.py', 'w', encoding='utf-8') as file: file.write(new_corotune)

    os.remove('merge.py')
    return Result(True, f'"{info["name"]}" was merged!')


