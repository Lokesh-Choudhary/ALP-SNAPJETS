#FACTORIAL OF A NUMBER
def fact(n):
    f=1
    for i in range (1,n+1):
        f*=i
    return f
n=int(input("Enter The Number For Finding Factorial  "))   
result=fact(n)
print("The Factorial Of ",n,"is ",result)
