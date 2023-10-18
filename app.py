import functions, corotune, importlib
color = functions.Color()
include = ''

while True:
    try: task_id = input(f'\n{color.yellow()}main {functions.lim(color.magenta())} ')
    except KeyboardInterrupt: exit()
    search_results = []
    if task_id.startswith('/'):
        command = task_id.split(' ')[0]
        query = task_id.split(' ')[1]

        if command == '/only':
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


    
    else:    
        
        for runtime in corotune.data:
            if not runtime['index']: continue 
            if task_id.lower() in functions.info(runtime): 
                search_results.append(runtime)
            
        if search_results == []:
            print(f'{color.red()}Not found\n')
            continue
        elif include == '':
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
        else: class_name = include

        print(f'{color.blue()}{functions.code(class_name, task_id)}\n')
        
        while True:
            try: 
                functions = importlib.reload(functions)
                result = functions.run(class_name, task_id)
                if result.passed: print(f'{color.green()}{result.result}\n')
                else: print(f'{color.red()}{result.error}\n')
                if include != '': break
                if len(functions.info(class_name, task_id)['args']) == 0: break

            except KeyboardInterrupt: break