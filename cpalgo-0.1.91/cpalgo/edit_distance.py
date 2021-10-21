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