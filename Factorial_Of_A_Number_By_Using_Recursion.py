def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
n=int(input("Enter The Number For Finding The Factorial :-"))
result=fact(n)
print("The Factorial Of The Number ",n," is ",result)
