"""
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

In Unix-style file system:

A period '.' refers to the current directory.
A double period '..' refers to the directory up a level.
Any multiple consecutive slashes '//' are treated as a single slash '/'.
In Simplified Absolute path:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path doesn't end with trailing slashes '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Path will not have whitespace characters.



Input Format

The only argument given is string A.
Output Format

Return a string denoting the simplified absolue path for a file (Unix-style).
"""

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        s = A.split("/")

        stk = []
        for i in range(len(s)):
            if s[i].isalpha():
                stk.append(s[i])
            elif len(stk) != 0 and s[i] == "..":
                stk.pop()

        return '/' + '/'.join(stk)
