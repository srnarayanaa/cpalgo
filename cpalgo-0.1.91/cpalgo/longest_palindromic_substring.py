def longest_palindromic_substring(s):               
    t = '^#'+'#'.join(s)+'#$'
    n = len(t)
    p = [0]*n
    c = r = cm = rm = 0
    for i in range (1, n-1):
        p[i] = min(r-i, p[2*c-i]) if r > i else 0
        while t[i-p[i]-1] == t[i+p[i]+1]: p[i] += 1
        if p[i]+i > r: c, r = i, p[i]+i
        if p[i] > rm: cm, rm = i, p[i]
    return s[(cm-rm)//2:(cm+rm)//2]