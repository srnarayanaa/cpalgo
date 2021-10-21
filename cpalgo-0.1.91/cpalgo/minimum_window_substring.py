def minimum_window_substring(s, t):
    ln_s = len(s)
    ln_t = len(t)
    if ln_s == 0 or ln_t == 0 or ln_t > ln_s:
        return ""
    dct = {}
    for ch in t:
        dct[ch] = dct.get(ch, 0) + 1
    
    i = j = 0
    minWindow = ln_s + 1
    output = ""

    while i < ln_s:
        if s[i] in dct:

            if dct[s[i]] > 0:
                ln_t -= 1

            dct[s[i]] -= 1
        

        while ln_t == 0:
            if i - j + 1 < minWindow:
                minWindow = i - j + 1
                output = s[j: i+1]
            
            if s[j] in dct:
                dct[s[j]] += 1

                if dct[s[j]] > 0:
                    ln_t += 1
                
            j += 1
                
        i += 1
    
    return "" if minWindow == ln_s + 1 else output