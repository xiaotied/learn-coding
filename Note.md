# Coding Notes

## 1781 · Reverse ASCll Encoded String
[Problem address](https://github.com/xiaotied/learn-coding/blob/master/1781%20%C2%B7%20Reverse%20ASCII%20Encoded%20Strings.py)
#### Notes
1. (Inclusive, exclusive)
2. Slice
3. **It is important to identify the res outside the loop**
4. **The input is string; it should be convert to int to use chr()**

```python
    def reverseAsciiEncodedString(self, encodeString):
        # Write your code here
        ans = ""
        for i in range(0, len(encodeString),2):
            number = encodeString[i:i+2]
            ans += chr(int(number))
        return ans[::-1]
```


## 146 · Lowercase to Uppercase II
[LintCode Address](https://www.lintcode.com/problem/146)
#### Notes
1. ~~upper(var)~~ use var.upper()

```python
    def lowercaseToUppercase2(self, str):
        # write your code here
        return str.upper()
```