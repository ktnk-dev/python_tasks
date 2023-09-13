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
