def palindrom(s):
    s=''.join(c for c in s if c.isalpha())
    s=s.lower()
    if s==s[::-1]:
        return 'Palindrome'
    else:
        return 'Not palindrome'

print(palindrom(input('Enter the string: ')))