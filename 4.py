class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        self.s=n;
        self.p=[];
        self.q=[];
        
        count=0;
        while(self.s>0):
            if((self.s)%2==1):
                count=count+1;
            self.s=self.s/2;
        
        return count;