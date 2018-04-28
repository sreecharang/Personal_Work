class Solution(object):
	def minDistance(self, word1, word2):
		m = len(word1)
		n = len(word2)

		dp = [[0 for __ in range(m + 1)] for __ in range( n + 1)]
		for j in range(m + 1):
			dp[0][j] = j
		for i in range(n + 1):
			dp[i][0] = i
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				onemore = 1 if word1[j - 1] != word2[i - 1] else 0
				dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, do[i - 1][j - 1] + onemore)
		return dp[n][m]
		
