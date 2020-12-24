class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        n = len(A)
        self.move(n,A,B,C)
    def move(self,n,A,B,C):  
        if n == 1:                 # if n=1, move A to C
            C.append(A[-1])
            A.pop()
            return
        else:
            self.move(n-1,A,C,B)   # move n-1 from A to B
            C.append(A[-1])        # move 1 from A to C
            A.pop()
            self.move(n-1,B,A,C)   # move n-1 from B to C
