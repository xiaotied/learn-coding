# 1781 · Reverse ASCII Encoded Strings

# Description
# Given a string which encode by ascii 
# (For example, "ABC" can encode to "656667")
# You need to write a function that take an encoded string as input and returns reversed decoded string.



# Write your code here

encodeString = "7976766972"

# imnporant here: establish the None string here otherwise no res identified and will casue the error in for loop
res = ""


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
