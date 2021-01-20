def perm_gen_lex(a):        
    if(len(a)==1): return [a]
    result=[]
    for i,v in enumerate(a):
        result += [v+p for p in perm_gen_lex(a[:i]+a[i+1:])]
    return result

