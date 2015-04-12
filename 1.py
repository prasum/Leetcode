import itertools

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        new = sorted(list(set(A)))
        for i in xrange(len(new)):
            A[i] = new[i]
        length = len(new)
        return length