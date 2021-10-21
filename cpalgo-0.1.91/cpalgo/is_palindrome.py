def is_palindrome(string):
    # Write your code here.
    N=len(string)
    ans=True
    for i in range(0,N//2):
    	if string[i]!=string[N-i-1]:
    		ans=False
    		break
    return ans