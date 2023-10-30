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

import corotune
import inspect
import importlib

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
    base += f'result = Solution.run({",".join(["input()" for _ in func["args"]])})\nprint(result)'
    return base

def share_class(class_name):
    source_code = inspect.getsource(eval(f'corotune.{class_name}'))
    class_data = corotune.data[class_name]
    merge_info = {
        'name': class_name,
        'data': class_data
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
    
    new_corotune = 'from functions import file\n\n'
    
    for class_name in corotune.data.keys():
        new_corotune += inspect.getsource(eval(f'corotune.{class_name}')) + '\n\n'

    new_corotune += source_code + '\n\n'

    new_data = corotune.data
    new_data[info["name"]] = info["data"]
    new_data_str = json.dumps(new_data, ensure_ascii=False, indent=4).replace(' true', ' True').replace(' false', ' False').replace(' null', ' None')

    new_corotune += f'data = {new_data_str}'

    with open('corotune.py', 'w', encoding='utf-8') as file: file.write(new_corotune)

    os.remove('merge.py')
    return Result(True, f'"{info["name"]}" was merged!')


