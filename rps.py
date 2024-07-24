import random
rock=''
paper=''
scissor=''
ch=int(input("to start the game press 1\n"))
while(ch==1):
    m=[rock,paper,scissor]
    user_choice=int(input("enter your choice "))
    print(m[user_choice])
    computer_choice=random.randint(0,2)
    print(f"computer selection {computer_choice}")
    print(m[computer_choice])
    if user_choice==0 and computer_choice==2 :

        print("user win")
    elif user_choice==2 and computer_choice==0:
        print("computer won")
    elif user_choice>computer_choice:
        print("user won")
    elif user_choice==computer_choice:
        print("tie")
    elif user_choice <computer_choice:
        print("computer won!")
    else:
        print("out of bound")
        
    break
