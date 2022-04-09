print("Select An Operation To Perform ")
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
opr=input()
if opr=='1':
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    print("The sum is ",str(int(n1)+int(n2)))
elif opr=='2':
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    print("The sub is ",str(int(n1)-int(n2)))
elif opr=='3':
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    print("The mul is ",str(int(n1)*int(n2)))
elif opr=='4':  
    n1=int(input("Enter first number "))
    n2=int(input("Enter second number "))
    print("The div is ",str(int(n1)/int(n2)))
else :
     print("INVALID OPERATOR")
