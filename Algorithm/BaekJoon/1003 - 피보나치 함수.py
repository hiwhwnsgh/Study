import sys
global a,b
dic = {0:0,1:1}
def fibo(n):
    global a,b
    if n == 0:
        a+=1
        return 0
    elif n==1:
        b+=1
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
N = int(sys.stdin.readline())
for i in range(N):
    n = int(sys.stdin.readline())
    a = b = 0
    fibo(n)
    print(str(a)+' '+str(b))
    
