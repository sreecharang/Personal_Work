class Solution(object):
	def lengthofLastWord(self, s):
		length  = len(s)
		index = length - 1
		while index >= 0 and s[index] == " ":
			index -= 1
		temp = index
		while index >= 0 and s[index] != " ":
			index -= 1
		return temp - index
		