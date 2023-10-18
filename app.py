import functions, corotune, importlib
color = functions.Color()
include = ''
command_prefix = '#'
code_show = False
url_show = True
infinity = False


while True:
    try: task_id = input(f'\n{color.yellow()}main {functions.lim(color.magenta())} ')
    except KeyboardInterrupt: exit()
    search_results = []
    if task_id.startswith(command_prefix):
        command = task_id.split(' ')[0][1:]
        query = task_id.split(' ')[1] if len(task_id.split(' ')) > 1 else ''

        if command == 'only':
            for runtime in corotune.data:
                if query.lower() in runtime: 
                    search_results.append(runtime)
                    
            
            if search_results == []:
                print(f'{color.red()}Not found\n')
                continue
            elif len(search_results) != 1:
                search_query = input(f'''{color.yellow()}{f"{functions.lim(color.yellow(),', ')}".join(search_results)} {functions.lim(color.magenta())} ''').lower()
                for runtime in corotune.data:
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

                

    
    else:    
        if include == '':
            for runtime in corotune.data:
                if not corotune.data[runtime]['index']: continue 
                if task_id.lower() in functions.info(runtime): 
                    search_results.append(runtime)
            
            if search_results == []:
                print(f'{color.red()}Not found\n')
                continue
            if len(search_results) != 1:
                class_name = ''
                search_query = input(f'''{color.yellow()}{f"{functions.lim(color.yellow(),', ')}".join(search_results)} {functions.lim(color.magenta())} ''').lower()
                for runtime in corotune.data:
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
                   

        print(f'{color.blue()}{functions.code(class_name, task_id)}\n') if code_show else ...
        if corotune.data[class_name]["baseurl"] and url_show: print(f'{color.blue()}URL: {color.cyan()}{corotune.data[class_name]["baseurl"].replace("%i", str(task_id))}')
        
        while True:
            try: 
                functions = importlib.reload(functions)
                result = functions.run(class_name, task_id)
                if result.passed: print(f'{color.green()}{result.result}\n')
                else: print(f'{color.red()}{result.error}\n')
                if not infinity: break
                if len(functions.info(class_name, task_id)['args']) == 0: break

            except KeyboardInterrupt: break