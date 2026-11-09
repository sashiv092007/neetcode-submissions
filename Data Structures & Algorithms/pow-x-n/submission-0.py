class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.00000
        elif n > 0:
            return float(x**n)
        else:
            a = -n
            return float((1/x)**a)       
        