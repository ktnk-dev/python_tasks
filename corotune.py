def func_3121(s: str) -> int:
    found = False
    for i, v in enumerate(s):
        if v == 'f':
            if found: return i
            else: found = True
    
    if not found: return -2
    else: return -1 

def func_3122(s: str) -> str:
    q = s.split('h')
    return f'{q[0]}{q[-1]}'

def func_3123(s: str) -> str: 
    q = s.split('h')
    iq = 'h'.join(q[1:-1])[::-1]
    return f'{q[0]}h{iq}h{q[-1]}'

def func_3124(s: str) -> str:
    q = s.split('h')
    iq = 'h'.join(q[1:-1])
    return f'{q[0]}h{iq*2}h{q[-1]}'

def func_3125(s: str) -> str:
    return s.replace('1', 'one')

def func_3126(s: str) -> str:
    return s.replace('@', '') 

def func_112339(s: str) -> str:
    return s.split()[0]

def func_112340(s: str) -> str:
    return s.split()[-1]

def func_112341(s: str) -> str:
    max = [0, '']
    for word in s.split(' '):
        if len(word) > max[0]: max[0], max[1] = len(word), word
    return '\n'.join(map(str, max[::-1]))

def func_112342(s: str) -> int:
    return len(s.split())

def func_112343(s: str) -> str:
    return 'YES' if s == s[::-1] else 'NO'

def func_112344(s: str) -> str:
    s = s.replace(' ', '')
    return 'YES' if s == s[::-1] else 'NO'

def func_112345(s: str) -> str:
    return '\n'.join(s.split('\\'))

def func_112346(s: str) -> str:
    s = s.split(' ')
    return f'{s[2]} {s[0][0]}.{s[1][0]}.'

def func_112347(s: str) -> str:
    s = s.split(' ')
    return f'{s[1][0]}.{s[2][0]}. {s[0]}'

def func_112348(s: str, repl_from: str, repl_to: str) -> str:
    return s.replace(repl_from, repl_to) 

def func_112349(s: str, splitter: str) -> int:
    return len(s.split(splitter))-1

def func_112350(s: str, ft: str) -> str:
    q = s.split('.')
    if len(q) == 1: return f'{s}.{ft}'
    else: return ".".join(q[:-1])+f'.{ft}'

def func_112351(s: str) -> int:
    return int(s, base=16)

def func_112352(s: str) -> int:
    res = bin(int(s, base=16))
    return res.replace('0b','')

def func_112353(s: str) -> int:
    return oct(int(s, base=16)).replace('0o', '')

def func_112354(s: str, ui: str) -> str:
    if s[0] == '-': minus = True
    else: minus = False
    s = s.replace('-','')
    ui = ui.split()
    from_base, to_base = ui[0], ui[1]

    dec_num = int(s, base=int(from_base))
    dgts = []
    while dec_num:
        dgts.append(int(dec_num % int(to_base)))
        dec_num //= int(to_base)

    dgts.reverse()
    import string
    if minus: res = '-'
    else: res = ''
    for n in dgts:
        if n > 9: res += string.ascii_uppercase[n-10]
        else: res += str(n)

    return res

def func_112355(s: str) -> int:
    num = 0
    rim = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
        }
    for k in s:
        num += rim[k.lower()]
    return num

def func_2506(s: str) -> int:
    cur = 0
    max = 0
    for i in s:
        if i == 'C': cur += 1
        else:
            if cur > max: max = cur
            cur = 0
    return max

def func_2510(s: str) -> int:
    cur = 0
    max = 0
    for i in s:
        if i in 'ABC': cur += 1
        else:
            if cur > max: max = cur
            cur = 0
    return max

def func_2520(s: str) -> int:
    cur = 0
    max = 0
    for i in s:
        if i not in 'AE': cur += 1
        else:
            if cur > max: max = cur
            cur = 0
    return max

def func_2521(s: str) -> str:
    cur = ['', 1]
    max = ['', 1]
    for i in s:
        if i == cur[0]: cur[1] += 1
        else:
            if cur[1] > max[1]: max = cur
            cur = [i, 1]
        
    if cur[1] > max[1]: max = cur
    return f'{max[0]} {max[1]}'

def func_2529(s: str) -> str:
    s = open(f'./files/{s}', 'r').read()
    import string
    string.ascii_uppercase
    max_list = [[],0]
    cur = ['',0]
    for j, i in enumerate(s):
        #print(j/len(s), i, cur, max_list) if j%10000 == 0 else ...
        cm = string.ascii_uppercase.find(i)
        if cm > cur[1]:
            cur[0], cur[1] = cur[0]+i, cm
        else:
            if len(cur[0]) > max_list[1]: max_list = [[cur[0]], len(cur[0])]
            elif cur[0] not in max_list[0] and len(cur[0]) > max_list[1]: max_list[0].append(cur[0])
            cur = [i, cm]
    return f'{max_list[0][0]} {max_list[1]}'

def func_2531(s: str) -> str:
    s = open(f'./files/{s}', 'r').read()
    import string
    string.ascii_uppercase
    max_list = [[],0]
    cur = ['',99999999, 0]
    for j, i in enumerate(s):
        #print(j/len(s), i, cur, max_list) if j%100000 == 0 else ...
        cm = string.ascii_uppercase.find(i)
        if cm > cur[1]:
            cur[0], cur[1] = cur[0]+i, cm
        else:
            if len(cur[0]) > max_list[1]: max_list = [[cur[2]], len(cur[0])]
            elif cur[0] not in max_list[0] and len(cur[0]) > max_list[1]: max_list[0].append(cur[2])
            cur = [i, cm, j+1]
    return f'{max_list[0][0]}'

def func_2533(s: str) -> str:
    s = open(f'./files/{s}', 'r').read()
    import string
    string.ascii_uppercase
    max_list = [[],0]
    cur = ['',0, 0]
    for j, i in enumerate(s):
        print(j/len(s), i, cur, max_list) if j%10000 == 0 else ...
        cm = string.ascii_uppercase.find(i)
        if cm < cur[1]:
            cur[0], cur[1] = cur[0]+i, cm
        else:
            if len(cur[0]) > max_list[1]:
                max_list = [[cur[0]], len(cur[0])]
            elif cur[0] not in max_list[0] and len(cur[0]) > max_list[1]:
                max_list[0].append(cur[0])
            cur = [i, cm, j+1]
    return f'{max_list[0][0]}'

def func_2518(s: str) -> int:
    cur = 0
    max_num = 0
    for i in s:
        if i != 'D': cur += 1
        else:
            if cur > max_num: max_num = cur
            cur = 0
    return max_num



def func_2538(file_name: str) -> int:
    data = ''
    with open(f'./files/{file_name}', 'r', encoding='utf-8') as file: data = file.read()
    max_len = 0
    cur_len = 0
    state = False
    for v in data:
        if v == '(': # match -> case проще
            if state: 
                state = False
                if cur_len > max_len: max_len = cur_len
                cur_len = 0
            else: state = True
        elif v == ')':
            if state: 
                cur_len += 1
                state = False
            else: 
                state = False
                if cur_len > max_len: max_len = cur_len
                cur_len = 0
    if cur_len > max_len: max_len = cur_len
    return max_len
    
def func_2548(file_name: str) -> int:
    data = ''
    with open(f'./files/{file_name}', 'r', encoding='utf-8') as file: data = file.read()
    return len(data.split('KTOS'))-1


def func_2715(file_name: str) -> int:
    data = ''
    with open(f'./files/{file_name}', 'r', encoding='utf-8') as file: data = file.read()
    max_len = 0
    cur_len = 0
    is_odd_cur = False
    for v in data:
        if int(v)%2:
            if not is_odd_cur:
                if cur_len > max_len: max_len = cur_len
                cur_len = 1
                is_odd_cur = True
            else: cur_len += 1
        else: 
            if is_odd_cur:
                if cur_len > max_len: max_len = cur_len
                cur_len = 1
                is_odd_cur = False
            else: cur_len += 1
    if cur_len > max_len: max_len = cur_len
    return max_len

