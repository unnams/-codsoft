def cal(a,b):
    while True:
       
       
        ch=input("select the operator ")
        if ch=='+':
            print("addition",a+b)
        elif ch=='-':
            print("subtraction",a-b)
        elif ch=='*':
            print("multiplication",a*b)
        elif ch=='/':
            print("divison ",a/b)
        elif ch=='%':
            print("remainder ",a%b)
        else:
            print("sorry the operator is not specified")

        c=input("if you want to play again yes/no")
        if c.lower()!='yes':
           print("thank you")
           break
a=int(input("enter the a value   "))
b=int(input("enter the b value  "))

cal(a,b)

