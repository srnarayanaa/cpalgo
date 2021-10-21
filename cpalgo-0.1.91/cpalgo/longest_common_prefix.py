def longest_common_prefix(S):
    if not S: return ''
    m, M, i = min(S), max(S), 0
    for i in range(min(len(m),len(M))):
        if m[i] != M[i]: break
    else: i += 1
    return m[:i]