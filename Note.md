# Coding Notes

## 1781-Reverse ASCll Encoded String
[Problem address](https://github.com/xiaotied/learn-coding/blob/master/1781%20%C2%B7%20Reverse%20ASCII%20Encoded%20Strings.py)
#### Notes
1. (Inclusive, exclusive)
2. Slice
3. **It is important to identify the res outside the loop**
4. **The input is string; it should be converted to int to use chr()**

''' Python

    def reverseAsciiEncodedString(self, encodeString):
        # Write your code here
        ans = ""
        for i in range(0, len(encodeString),2):
            number = encodeString[i:i+2]
            ans += chr(int(number))
        return ans[::-1]
'''