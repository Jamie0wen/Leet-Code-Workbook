# 13. Roman to Integer
**Difficulty:** Easy  
**Topics:** — Hash Table Math String

**Description**

---

Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|--------|
| I      | 1      |
| V      | 5      |
| X      | 10     |
| L      | 50     |
| C      | 100    |
| D      | 500    |
| M      | 1000   |

For example:
- **2** is written as **II** (1 + 1)  
- **12** is written as **XII** (10 + 2)  
- **27** is written as **XXVII** (20 + 5 + 2)

Roman numerals are usually written from **largest to smallest**, left to right.

However, subtraction is used in these cases:

- **I** can be placed before **V (5)** or **X (10)** → *4 and 9*  
- **X** can be placed before **L (50)** or **C (100)** → *40 and 90*  
- **C** can be placed before **D (500)** or **M (1000)** → *400 and 900*

Given a Roman numeral, convert it to an integer.

---

## Examples

### Example 1
**Input:** `s = "III"`  
**Output:** `3`  
**Explanation:** `III = 3`

### Example 2
**Input:** `s = "LVIII"`  
**Output:** `58`  
**Explanation:** `L = 50`, `V = 5`, `III = 3`

### Example 3
**Input:** `s = "MCMXCIV"`  
**Output:** `1994`  
**Explanation:**  
- `M = 1000`  
- `CM = 900`  
- `XC = 90`  
- `IV = 4`

---

## Constraints
- `1 <= s.length <= 15`
- The string contains only: `I`, `V`, `X`, `L`, `C`, `D`, `M`
- `s` is guaranteed to be a valid Roman numeral in the range **[1, 3999]**
