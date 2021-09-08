# Coding Notes

## 1781 · Reverse ASCll Encoded String
[Problem address](https://github.com/xiaotied/learn-coding/blob/master/1781%20%C2%B7%20Reverse%20ASCII%20Encoded%20Strings.py)
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
[LintCode Address](https://www.lintcode.com/problem/146)
#### Notes
1. ~~`upper(var)`~~ use `var.upper()`

```python
    def lowercaseToUppercase2(self, str):
        # write your code here
        return str.upper()
```

## 1784 · Decrease To Be Palindrome
Easy \
[LintCode Address](https://www.lintcode.com/problem/1784)
#### Notes
1. `ord()` function transfer str to ASCII
2. Two pointer
    3. Start from beginning and end
    4. For loop length should be half of the input string
    5. Use `//` to do a down divide 
4. Use index to get particular str in python

``` python
def numberOfOperations(self, s):
    # Write your code here
    cnt = 0
    
    for i in range(len(s)//2):
        cnt += abs(ord(s[i]) - ord(s[len(s)-1-i]))
        return cnt

```