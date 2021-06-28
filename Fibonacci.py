def Fibonacci(n):
   if n==1:
    return 1
   elif n==2:
    return 1,2
   else:
    a=1
    b=1
    flist=[1,1]
    print(n)
    while n>0:
        c=a+b
        flist.append(c)
        a=b
        b=c
        n-=1
        print(a,b,c,n)
    return flist
