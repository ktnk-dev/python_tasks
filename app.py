import corotune
import importlib
import functions
        
color = functions.Color()
db = functions.load_db()
args = ['-code', '-s']



def run(num):
    try:
        inputs = []
        inputs_len = functions.get_inputs(num)
        for input_num in range(inputs_len):
            inputs.append(input(f"{color.yellow()}{functions.get_hash()}{color.gray()} > {color.cyan()}{num}{color.gray()} {color.green()}{input_num+1}/{inputs_len}{color.gray()} > {color.magenta()}"))
        global corotune
        corotune = importlib.reload(corotune)
        if inputs == ['']*len(inputs): return True
        try:
            result = eval(f'{db[num]}({", ".join(["inputs["+str(input_num)+"]" for input_num in range(len(inputs))])})')
            print(f'{color.green()}{result}\n{color.reset()}')
            return True
        except Exception as e:
            print(f'{color.red()}{e}{color.reset()}')
            return True
    except KeyboardInterrupt: return False


print(f'\n\n{color.gray()}--- {color.reset()}Задания {color.gray()}---')
print(f'{color.yellow()}Доступные задачи: {color.green()}{f"{color.gray()}, {color.green()}".join(map(str, db.keys()))}')
print(f'{color.yellow()}Доступные аргументы: {color.green()}{f"{color.gray()}, {color.green()}".join(args)}')
print(f'{color.gray()}Укажите номер задачи, при необходимости можно использовать аргумент. Например:{color.magenta(False)} 123 {color.yellow(False)}-loop{color.reset()}\n')
while True:
    db = functions.load_db()
    try: 
        u = input(f'\n{color.yellow()}{functions.get_hash()}{color.gray()} > {color.cyan()}mainloop {color.gray()}> {color.magenta()}').split(' ')
        num = int(u[0])
        try: arg = u[1]
        except: arg = '-loop'
    except ValueError: 
        print(f'{color.red()}Это не номер')
        continue
    except KeyboardInterrupt:
        exit()

    # print(f'\n{color.cyan()}https://informatics.msk.ru/mod/statements/view.php?chapterid={num}{color.reset()}')

    if arg == '-loop': 
        while run(num): pass
    elif arg == '-code': functions.show_code(num)
    else: run(num)
