'''
Peusdo code
1. Create a dictionary to map Roman values to integer values 
2. Iterate over length of string 
3. If we have "IV" this is 4, whereas "VI" is 5. The order of the Roman numeral character matters.
4. We therefore need to compare the value each character of the strings represents.
5. This determins what operation we use to find the total value of the Roman numeral.
6. If there is a smaller value before a bigger one we subtract the small from the big,
   e.g ,IV, we have 1 and 5 -> 5-1 = 4. 
7. And vice versa if we have a bigger value before a small or equal we add. 

'''

#Dictionary of mapped values

roman_Num = {
    "I": 1,
    "V": 5,
    "X": 10, 
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


# Code Roman neumeral rules
def romantoInt(string):
    number = 0 #Current value = 0
    for i in range(len(string)): #Iterate over length of string
        if i < len(string) - 1: #Check if there is a next character in string
            if roman_Num[string[i]] < roman_Num[string[i + 1]]: #Comapare value of current character against the next in the string
                number -= roman_Num[string[i]]
            else:
                number += roman_Num[string[i]]
        else:
            number += roman_Num[string[i]]  # Add last character
    return number

             

print(romantoInt(string = 'MC'))
        