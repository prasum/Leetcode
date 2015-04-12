class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        self.s=x;
        count=0;
        self.p=[];
        k=0;
        f=0;
        if(self.s<0):
                self.s=0-self.s;
                f=1;
           
        while((self.s)>0):
                self.p.append((self.s)%10);
                self.s=self.s/10;
                count=count+1;
        c=count-1;
            
        for i in xrange(len(self.p)):
                k=k+(self.p[i])*(10**(c));
                c=c-1;
        if(k==x):
            return True
        else:
            return False
       