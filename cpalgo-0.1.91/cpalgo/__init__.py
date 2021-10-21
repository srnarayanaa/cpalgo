import bisect
import heapq
import operator as op
from functools import reduce


def word_break(s, words):
    ok = [True]
    max_len = max(map(len,words+['']))
    words = set(words)
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(max(0, i-max_len),i)),
    return ok[-1]


def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1

    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]
    return dp[n-1]


def two_sum (nums, target):
    complement ={}
    for i,v in enumerate(nums):
        if v in complement:
            return complement[v],i
        else:
            complement[target - v] = i
    return -1


def three_sum(nums, target):
    nums.sort()
    length = len(nums)
    result = set()
    for i in range(length-2):
        left = i+1
        right = length-1
        while left < right:
            sum_value = nums[i]+nums[left]+nums[right]
            if sum_value == 0:
                result.add((nums[i],nums[left],nums[right]))
                left += 1
                right -= 1
            elif sum_value < 0:
                left +=1
            else:
                right -= 1
    return result

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

def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
    max_n = min(max_n, mod - 1)

    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod

def maximum_subarray(nums):   
	newNum = maxTotal = nums[0]        
	
	for i in range(1, len(nums)):
		newNum = max(nums[i], nums[i] + newNum)
		maxTotal = max(newNum, maxTotal)

	return maxTotal	


def maximum_product_subarray(self, nums):
    i = 0
    currentMax, currentMin, ans = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        tmp = currentMax
        currentMax = max(n, n*currentMax, n*currentMin)
        currentMin = min(n, n*tmp, n*currentMin)
        ans = max(ans, currentMax)
    return ans


def longest_substring_without_repetition(self, s):
    start = maxLength = 0
    usedChar = {}
    
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[s[i]] = i

    return maxLength



def longest_increasing_subsequence(nums):
    dp = []
    for num in nums:
        i = bisect.bisect_left(dp, num)
        if i == len(dp):
            dp.append(num)
        else:
            dp[i] = num
    return len(dp) 

def longest_common_palindrome(s):               
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


def longest_common_subsequence(a, b):
    lengths = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i + 1][j + 1] = lengths[i][j] + 1
            else:
                lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])

    result = []
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[ x][y] == lengths[x - 1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y - 1]:
            y -= 1
        else:
            result.append(a[x - 1])
            x -= 1
            y -= 1

    return result[::-1]


def longest_palindromic_subsequence(s):
    return longest_common_subsequence(s, s[::-1])


def longest_common_prefix(S):
    if not S: return ''
    m, M, i = min(S), max(S), 0
    for i in range(min(len(m),len(M))):
        if m[i] != M[i]: break
    else: i += 1
    return m[:i]


def kth_largest_element(nums, k):
    heap=[]
    for i in nums:
        heapq.heappush(heap,-i)
    for i in range(k):
        res=-heapq.heappop(heap)
    return res

def is_valid_parantheses(s):
    dic = {'(':1 , ')':2 , '[':3 , ']':6 , '{':5 , '}':10}
    res = []
    for one in s:
        temp = dic[one]
        if(temp %2 ):
            res.append(temp)
        else:
            if(len(res) and res[-1]==temp//2):
                del res[-1]
            else:
                return False
    return res==[]


def is_palindrome(string):
    N=len(string)
    ans=True
    for i in range(0,N//2):
    	if string[i]!=string[N-i-1]:
    		ans=False
    		break
    return ans


def first_missing_positive(nums):
    index = 0
    while index < len(nums):
        if index + 1 == nums[index]:    
            index += 1
        elif nums[index] <= 0:       
              index += 1
        elif nums[index] > len(nums):  
               index += 1
        elif nums[index] == nums[nums[index]-1]:
            index += 1
        else:
            A,B = index,nums[index]-1
            nums[A], nums[B] = nums[B], nums[A]
            

    for index in range(len(nums)):
        if index + 1 != nums[index]:   
            return index + 1

    return len(nums) + 1


def edit_distance(str1, str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
    	for j in range(n+1):
    		if i==0 and j==0:
    			continue
    		elif i==0:
    			dp[i][j]=dp[i][j-1]+1
    		elif j==0:
    			dp[i][j]=dp[i-1][j]+1
    		elif str1[i-1]==str2[j-1]:
    			dp[i][j]=dp[i-1][j-1]
    		else:
    			dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
    return dp[m][n]


def euler_phi(n):
    sieve = [i if i & 1 else i // 2 for i in range(n + 1)]
    for i in range(3, n + 1, 2):
        if sieve[i] == i:
            for j in range(i, n + 1, i):
                sieve[j] = (sieve[j] // i) * (i - 1)

    return sieve


def count_primes(n):
    if n < 2:
        return 0
    strikes = [1] * n
    strikes[0] = 0
    strikes[1] = 0
    
    for i in range(2, int(n**0.5)+1):
        if  strikes[i] != 0:
            strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
    return sum(strikes)


def remove_middle(a, b, c):
    cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
    return cross < 0 or cross == 0 and dot <= 0


def convex_hull(points):
    spoints = sorted(points)
    hull = []
    for p in spoints + spoints[::-1]:
        while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def chinese_remainder(a, p):
    prod = reduce(op.mul, p, 1)
    x = [prod // pi for pi in p]
    return sum(a[i] * pow(x[i], p[i] - 2, p[i]) * x[i] for i in range(len(a))) % prod


def extended_gcd(a, b):
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def composite_crt(b, m):
    x, m_prod = 0, 1
    for bi, mi in zip(b, m):
        g, s, _ = extended_gcd(m_prod, mi)
        if ((bi - x) % mi) % g:
            return None
        x += m_prod * (s * ((bi - x) % mi) // g)
        m_prod = (m_prod * mi) // gcd(m_prod, mi)
    return x % m_prod


def caesar_cipher(string, key):
    ans=[]
    for i in string:
    	ans.append(chr(97+(ord(i)+key-97)%26))
    return ''.join(ans)