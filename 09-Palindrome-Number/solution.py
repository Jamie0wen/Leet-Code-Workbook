
# Palindrome - a word, phrase, or sequence that reads the same backwards as forwards


def palindrome_checker(n):
    rev = int(str(n)[::-1]) # reverse the integer using string slicing

    if rev == n:
        print(n, 'is a palidrome')
    else:
        print(n, 'is not a palindrome')

palindrome_checker(123)