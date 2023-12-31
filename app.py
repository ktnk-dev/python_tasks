import functions, importlib, os
try: 
    from pprint import pprint 
    pprint_runtime = True 

except ImportError: 
    pprint_runtime = False


color = functions.Color()
include = ''
command_prefix = '#'
code_show = False
url_show = True
infinity = False
doc_show = True

if 'merge.py' in os.listdir('./'):
    try: i = input(f'{color.green()}Merge file found!\n{color.cyan()}Do you want merge? (y/n) {functions.lim(color.magenta())} ')
    except KeyboardInterrupt: i = 'n'
    if i.lower() == 'y': 
        result = functions.merge_class()
        if result.passed: print(f'\n{color.green()}{result.result}\n')
        else: print(f'\n{color.red()}{result.error}\n')
    else: print(f'\n{color.red()}Merge ignored\n')

import corotune

while True:
    try: task_id = input(f'\n{color.yellow()}main {functions.lim(color.magenta())} ')
    except KeyboardInterrupt: exit()
    corotune = importlib.reload(corotune)
    search_results = []
    if task_id.startswith(command_prefix):
        command = task_id.split(' ')[0][1:]
        query = task_id.split(' ')[1] if len(task_id.split(' ')) > 1 else ''

        if command == 'only':
            for runtime in functions.get_corotune_data():
                if query.lower() in runtime: 
                    search_results.append(runtime)
                    
            
            if search_results == []:
                print(f'{color.red()}Not found\n')
                continue
            elif len(search_results) != 1:
                search_query = input(f'''{color.yellow()}{f"{functions.lim(color.yellow(),', ')}".join(search_results)} {functions.lim(color.magenta())} ''').lower()
                for runtime in functions.get_corotune_data():
                    if runtime.lower().startswith(search_query):
                        include = runtime
                        break
                
                if not include: 
                    print(f'{color.red()}Not found\n')
                    continue  

            else: include = search_results[0]
            print(f'{color.green()}Current runtime: {include}\n')

        if command == 'loop':
            if infinity:
                infinity = False
                print(f'{color.red()}Task loop disabled\n')
            else: 
                infinity = True
                print(f'{color.green()}Task loop enabled\n')
        

        if command == 'code':
            if code_show:
                code_show = False
                print(f'{color.red()}Code showing disabled\n')
            else: 
                code_show = True
                print(f'{color.green()}Code showing enabled\n')

        if command == 'url':
            if url_show:
                url_show = False
                print(f'{color.red()}URL showing disabled\n')
            else: 
                url_show = True
                print(f'{color.green()}URL showing enabled\n')
        
        if command == 'doc':
            if doc_show:
                doc_show = False
                print(f'{color.red()}Docs showing disabled\n')
            else: 
                doc_show = True
                print(f'{color.green()}Docs showing enabled\n')

        if command == 'share':
            if query not in functions.get_corotune_data():
                print(f'{color.red()}Not found\n')
                continue
            else: 
                result = functions.share_class(query)
                if result.passed: print(f'{color.green()}{result.result}\n')
                else: print(f'{color.red()}{result.error}\n')
            

                

    
    else:    
        if include == '':
            for runtime in functions.get_corotune_data():
                if not functions.get_corotune_data()[runtime]['index']: continue 
                if task_id.lower() in functions.info(runtime): 
                    search_results.append(runtime)
            
            if search_results == []:
                print(f'{color.red()}Not found\n')
                continue
            if len(search_results) != 1:
                class_name = ''
                search_query = input(f'''{color.yellow()}{f"{functions.lim(color.yellow(),', ')}".join(search_results)} {functions.lim(color.magenta())} ''').lower()
                for runtime in functions.get_corotune_data():
                    if runtime.lower().startswith(search_query):
                        class_name = runtime
                        break
                
                if not class_name: 
                    print(f'{color.red()}Not found\n')
                    continue  

            else: class_name = search_results[0]
        else: 
            class_name = include
            if task_id.lower() not in functions.info(runtime): 
                print(f'{color.red()}Not found\n')
                continue
                   

        print(f'{color.blue()}{functions.code(class_name, task_id)}{color.magenta()}\n') if code_show else ...

        if doc_show: 
            docstr = functions.info(class_name, task_id)["doc"]
            docstr = docstr.replace("\n", " ") if docstr != None else None
            print(f'{color.gray()}{docstr}{color.magenta()}\n') if docstr != None else ...
        if functions.get_corotune_data()[class_name]["baseurl"] and url_show: print(f'{color.blue()}URL: {color.cyan()}{functions.get_corotune_data()[class_name]["baseurl"].replace("%i", str(task_id))}{color.magenta()}')

        while True:
            try: 
                functions = importlib.reload(functions)
                result = functions.run(class_name, task_id)
                if result.passed: 
                    print(f'{color.green()}', end='')
                    if pprint_runtime: pprint(result.result, width=25, sort_dicts=False)
                    else: print(f'{result.result}\n')
                else: print(f'{color.red()}{result.error}\n')
                if not infinity: break
                if len(functions.info(class_name, task_id)['args']) == 0: break

            except KeyboardInterrupt: break