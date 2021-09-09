---
Title: LintCode Problems Notes 
Author: Xiaotie Ding  
---

# Coding Problem Notes

{{TOC}}


## 1781 · Reverse ASCll Encoded String
<span style="color:green">Easy</span>\
[Problem address](https://github.com/xiaotied/learn-coding/blob/master/problems/1781%20%C2%B7%20Reverse%20ASCII%20Encoded%20Strings.py)
#### Notes
1. (Inclusive, exclusive)
2. Slice
3. **It is important to identify the res outside the loop**
4. **The input is string; it should be convert to int to use `chr()`**

```python
# method 1
# 从前往后遍历string，每隔2位提取下标(index)
for i in range(0, len(encodeString),2):
    # slice the str into 2 chrs string 
    # (very important: slice(inclusive, exclusive))
    # That why i+2 instead of i+1
    number = int(encodeString[i:(i+2)])
    # accumulate add char together by using +=
    # It is important to identify the res outside the loop
    res += chr(number)
# reverse the string outside the for loop
res = res[::-1]
print(res)
```

```python
# method 2
ans = ""

# Traverse the string from end to start
# Get index every two chars
# Why it is start from len(String)-1 instead of len(String)????
# It starts from end so consider the index start from 0; it should start from len()-1
# In the method 1, it traverse from start to end and due to the (inclusive, exclusive)
# It should be len(String) in order to end at len(String)-1
for i in range(len(encodeString)-1,0,-2):
    # why i-1 : i+1 because (inclusive, exclusive)
    asciiNumber = int(encodeString[(i-1):(i+1)])
    ans += chr(asciiNumber)
print(ans)
```
## 146 · Lowercase to Uppercase II
<span style="color: rgb(50, 197, 255)">Naive</span>\
[Link](https://www.lintcode.com/problem/146)
#### Notes
1. ~~`upper(var)`~~ use `var.upper()`

```python
def lowercaseToUppercase2(self, str):
    # write your code here
    return str.upper()
```

## 1784 · Decrease To Be Palindrome
<span style="color:green">Easy</span> \
[LintCode Address](https://www.lintcode.com/problem/1784)
#### Notes
1. `ord()` function transfer str to ASCII
2. Two pointer
    1. Start from beginning and end
    2. For loop length should be half of the input string
    3. Use `//` to do a floor value 
4. Use index to get particular str in python

```python
def numberOfOperations(self, s):
    # Write your code here
    cnt = 0
    
    for i in range(len(s)//2):
        cnt += abs(ord(s[i]) - ord(s[len(s)-1-i]))
        return cnt

```

## 958 · Palindrome Data Stream
<span style="color:green">Easy</span> \
[Link](https://www.lintcode.com/problem/958)
#### Notes
1. Brute force
2. Palindrome 的奇偶性\
3. 计数器
4. **如果只有 0 or 1 个字母出现奇数次 就可以组成palindrome**

|   | number of a | number of b | 几个字母出现了奇数次 | Palindrome |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| a | 1 | 0 | 1 | 1 |
| ab | 1 | 1 | 2 | 0 |
| aba | 2 | 1 | 1 | 1 |
| abab | 2 | 2 | 0 | 1 |
| ababa | 3 | 2 | 1 | 1 |

- When the odd appear **\>1** then not palindrome\


```python
def getStream(self, s):
    # check whether the string is None
    if s is None or len(s) == 0:
        return None
    # count the number of letter that appeared odd times
    odd_letter_cnt = 0
    # create a list contain the same length as input string
    result = [0 for _ in range(len(s))]
    # count the number of letters appeared
    letters = [0 for _ in range(26)]
    
    for i in range(len(s)):
        letters[ord(s[i]) - ord("a")] += 1
        if letters[ord(s[i]) - ord("a")] % 2 == 1:
            odd_letter_cnt += 1
        else:
            odd_letter_cnt -= 1
        result[i] = 0 if odd_letter_cnt > 1 else 1
    return result

```

## 1819 · Longest Semi Alternating Substring
<span style="color:green">Easy</span> \
[Link](https://www.lintcode.com/problem/1819)
#### Notes
1. Two pointers
2. `prev` and `cure` are string variables not the index
3. `for end in range()` end is index of end point.
4. `start` is the index not string.
5. `dup_cnt` is 1 because the pointer at least points to one node. 
6. `if dup_cnt == 3:`  move start pointer to one node ahead the end pointer. So the `dup_cnt = 2`
7. Don't forget to check `None` string.

![](/images/1819.png)

```python
def longestSemiAlternatingSubstring(self, s):
    # write your code here
    if s is None or len(s) == 0:
        return None
    
    start = 0
    dup_cnt = 1
    max_len = 0

    for end in range(1, len(s)):
        prev = s[end - 1]
        curr = s[end]

        if prev == curr:
            dup_cnt += 1
            if dup_cnt == 3:
                start = end - 1
                dup_cnt = 2
        else:
            dup_cnt = 1
        
        max_len = max(max_len, end - start + 1)
    return max_len

```

## 1540 · Can Convert
<span style="color:green">Easy</span> \
[LintCode Address](https://www.lintcode.com/problem/1540)

#### Notes
1. Two pointers
2. 
