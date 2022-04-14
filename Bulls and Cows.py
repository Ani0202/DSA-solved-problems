'''
Problem Description
 
 

 You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following 
info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls. 
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain 
duplicate digits.



Problem Constraints
1 <= secret.length, guess.length <= 100000
secret.length == guess.length
secret and guess consist of digits only.


Input Format
First argument is string denoting secret string 


Second argument is string denoting guess string 



Output Format
Return the hint for you friend's guess.
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        b = 0
        c = 0
        count = dict()
        for i in range(len(A)):
            if A[i] == B[i]:
                b += 1
                A = A[:i] + 'o' + A[i+1:]
                B = B[:i] + 'o' + B[i+1:]

            else:
                count[A[i]] = count.get(A[i], 0) + 1

        for i in B:
            if i != 'o' and i in count:
                c += 1
                count[i] -= 1
                if count[i] == 0:
                    del count[i]  

        return str(b)+'A'+str(c)+'B'  

        

