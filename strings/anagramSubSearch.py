'''
	Make two arrays of size 256, one of the original string and one of substring. As alphabet size is fixed
	this solution has O(n) complexity. Increase the count of the respective substring letters in the temp array.
	Do the same for the first m characters of the main text (where m is the number of letters in substring).
	Now traverse the main array and check if the frequency in the temp arrays are equal. If they are then print 
	the index where we got the anagram. Remove the first letter of the temp array (count_text) and add the latest 
	letter. Now keep comparing till we get to the end of the loop. At the end compare one last time. 
'''

MAX = 256

def isMatch(a,b):			# function to check if they are anagrams
	for i in range(MAX):
		if a[i] != b[i]:
			return False
	return True

def anagramSearch(text,s):
	n = len(s)				# length of substring
	m = len(text)			# length of main string
	count_s = [0]*MAX		# a temp array to keep count of substring elements
	count_text = [0]*MAX	# temp array to keep count of main text elements
	found = False				

	for i in range(n):					# storing first n elements in the main and substring in the temp strings
		count_s[ord(s[i])] +=  1
		count_text[ord(text[i])] += 1

	for i in range(n, m):					
		if isMatch(count_s, count_text):		
			print('Anagram found at index',i-n)
			found  = True	

		count_text[ord(text[i])] += 1			# adding new element and removing the first from the main string temp array
		count_text[ord(text[i-n])] -= 1

	if isMatch(count_s, count_text):			# checking if the last n elements are anagram
		print('Anagram found at index', m-n)
		found = True

	if found == False:
		print('No anagrams exists')
	return 


txt = "BACDGABCDA"
pat = "ABCD"

anagramSearch(txt, pat)
