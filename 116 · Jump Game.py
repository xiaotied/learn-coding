# Description
# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# The array A contains 𝑛 integers 𝑎1, 𝑎2, …, 𝑎𝑛 (1≤𝑎𝑖≤5000) (1≤n≤5000 )

# Example
# Example 1:

# Input:

# A = [2,3,1,1,4]
# Output:

# true
# Explanation:

# 0 -> 1 -> 4 (the number here is subscript) is a reasonable scheme.

# Example 2:

# Input:

# A = [3,2,1,0,4]
# Output:

# false
# Explanation:

# There is no solution that can reach the end.

# method1 dfs

def canJump(self, A):
	if A is None or len(A) == 0:
		return False

	return self.dfs(A, 0)

def dfs(self, A, curr_index):
	if curr_index == len(A) - 1:
		return True

	for i in range(curr_index + 1, curr_index + A[curr_index] + 1):
		if self.dfs(A,i):
			return True
	return Flase
	