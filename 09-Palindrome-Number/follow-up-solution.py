
# Without converting the interger into a string

  
def palindrome_Checker(n):
    if n < 0:
        print(n, 'is not a palindrome')
        return False  

    number = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    if reverse == number:
        print(number, 'is a Palindrome')
        return True
    else:
        print(number, 'is not a Palindrome')
        return False



palindrome_Checker(1002348)
