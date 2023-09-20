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

    
