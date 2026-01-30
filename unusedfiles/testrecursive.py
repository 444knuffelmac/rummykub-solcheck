def function(n):
    if n>0:
        print(n)
        n=function(n-1)
        print(n)
    elif n<0:
        n=function(-n)
    return n
print(function(9))