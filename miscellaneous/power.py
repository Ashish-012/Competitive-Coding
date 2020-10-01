

MOD = 1000000007
t  = int(input())
for i in range(t):
    a,b = map(int,input().split())
    result = 1
    while b>0:
        if b%2 == 1:
            result = (result*a) % MOD
        
        b = b//2
        a = (a*a)%MOD
    print(result)