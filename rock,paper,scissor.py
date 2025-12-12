import random
while True:
    ch=["rock","paper","scissor"]
    user_action=input("Enter a choice(rock,paper,scissor):")
    computer_choice=random.choice(ch)
    print("You chose",user_action)
    print("Computer chose",computer_choice)
    if  user_action==computer_choice:
        print("It's a tie.")
    elif user_action=="rock"and computer_choice=="scissor":
        print("Rock smashes scissors.You win.")
    elif user_action=="scissor"and computer_choice=="paper":
        print("Scissor cuts paper.You win.")
    elif user_action=="paper"and computer_choice=="rock":
        print("Paper covers rock.You win.")
    else:
        print("You lose.")
