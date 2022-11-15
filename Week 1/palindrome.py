string = input('Enter any word: ')

string = string.casefold()
rev_string = reversed(string)
if list(string) == list(rev_string):
    print('palindrome')
else:
    print('Not palindrome')