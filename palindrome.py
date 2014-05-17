def isPalindrome(s):
	#Check for end of recursion
	if(len(s) < 2):
		return True
	#Check first and last char for equality
	if(s[0] != s[len(s) - 1]):
		return False
	#Recursion call
	return isPalindrome(s[1:len(s) - 1])

str='mom'
print(str)
print(isPalindrome(str))