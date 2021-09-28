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
5. This is a reverse, return `ans[::-1]`.
6. Please return "" if an check function has been added since sometime the problem require to return "" instead of `None`.


```python
if encodeString is None or len(encodeString) == 0:
    return ""
```


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
1. the number of operations needed to change s to a palindrome at least in this problem basically is asking what is the sum of ASCII distance between the letter in the symmetrical position. 
2. Therefore we only need to find ASCII int for each string and then subtract in a symmetrical way.
2. `ord()` function transfer str to ASCII
3. Two pointer
    1. Start from beginning and end
    2. For loop length should be half of the input string
    3. Use `//` to do a floor value 
4. Remember the floor value is `//` 
5. Use index to get particular str in python

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
2. Greedy method

```python
def canConvert(self, s, t):
    # Write your code here
    if s is None or len(s) == 0:
        return False
    
    index_t = 0
    
    for c in s:
        if c == t[index_t]:
            index_t += 1
            if index_t == len(t):
                return True
    return False
```

## 936 · Capitalizes The First Letter
<span style="color:green">Easy</span> \
[LintCode Address](https://www.lintcode.com/problem/936)

#### Notes
1. 'str' object does not support item assignment, which means you cannot do `s[i] = s[i].upper()`. 
2. Must transfer the str to list and `''.join()` for return.
3. My code, ~~`if s[0] != " ":`~~, doesn't consider not letter situations; so the correct code should be `if s[0] >= 'a' and s[0] <= 'z':`.
4. Highlighted solution uses ASCII but mine use `upper.()`.

#### My code
```python
def capitalizesFirst(self, s):
    # Write your code here
    s = list(s)
    if s[0] != " ":
        s[0] = s[0].upper()
    else: pass
    for i in range(1, len(s)):
        if s[i-1] == " " and s[i] != " ":
            s[i] = s[i].upper()
    return ''.join(s)
```
#### Highlight solution
```python
def capitalizesFirst(self, s):
    # Write your code here
    n = len(s)
    s1 = list(s)
    if s1[0] >= 'a' and s1[0] <= 'z':
        s1[0] = chr(ord(s1[0]) - 32)
    for i in range(1, n):
        if s1[i - 1] == ' ' and s1[i] != ' ':
            s1[i] = chr(ord(s1[i]) - 32)
    return ''.join(s1)
```

## 415 · Valid Palindrome
<span style="color:orange">Medium</span> \
[LintCode Address](https://www.lintcode.com/problem/415)

#### Note
1. `str.isalnum()`
2. `str.[::-1]`
3. `str.isdigit()`
4. `str.isalpha()`
5. `str.lower()`
6. Remove all char expect letters and numbers.
7. Reverse the str and see if it is a palindrome.

#### My code
```python
def isPalindrome(self, s):
    # write your code here
    s1 = "".join(x for x in s if x.isalnum()).lower()
    if s is None or len(s) == 0 or s1 == s1[::-1]:
        return True
    else: 
        return False
```

#### solution 1
```python
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
```

#### Solution 2
```python
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s=[c.lower() for c in s if c.isalnum()]
        
        return s[0:]==s[::-1]
```

## 483 · Convert Linked List to Array List
<span style="color:green">Naive</span> \
[LintCode Address](https://www.lintcode.com/problem/483)

#### Note
1. The basic concept of linked list.
2. `self.val = val`
3. `self.next = next`
4. How to traverse the linked list? Use `while`

```python
def toArrayList(self, head):
    # write your code here
    ans = []
    while head is not None:
        ans.append(head.val)
        head = head.next
    return ans
```


## 225 · Find Node in Linked List
<span style="color:green">Naive</span> \
[LintCode Address](https://www.lintcode.com/problem/225)

#### Note
1. Use `while` to go through the linked list.
2. `else` issue?

#### My solution

```python
def findNode(self, head, val):
    # write your code here
    while head is not None:
        if head.val == val:
            return head 
        else:
            head = head.next
    return None
```
#### Official solution
```python
def findNode(self, head, val):
    # write your code here
    while head is not None:
        if head.val == val:
            return head 
        head = head.next
    return None
```

## 228 · Middle of Linked List
<span style="color:green">Naive</span> \
[LintCode Address](https://www.lintcode.com/problem/228)

#### Note
1. Have to use slow pointer and faster pointer.
2. Using `head.next` and `head.next.next` is not correct since `head.next.next` is only two steps ahead of `head`, which is not twice the `head`.
3. Using `slow = head` `fast = head` `slow = slow.next` `fast = fast.next.next`
4. Using `while fast.next and fast.next.next is not None` instead of only using `fast.next.next` to avoid `fast.next` is `None` and then `fast.next.next` will return error.

#### My WRONG solution
```python
# wrong answer!!!!

def middleNode(self, head):
    # write your code here
    if head is None:
        return None
    else:
        while head.next and head.next.next is not None:
            head = head.next
        return head
```

#### Correct solution
```python
def middleNode(self, head):
    # write your code here
    if head is None:
        return None
    else:
            slow = head
            fast = head
        while fast.next and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
```