import random
def comp_chc():
    n=random.randint(1, 3)
    if n==1:
        return "rock"
    elif n==2:
        return "paper"
    else:
        return "scissors"   
    
user_chc=input("Enter your choice (rock, paper, scissors): ").lower()
if user_chc not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please choose rock, paper, or scissors.")

if user_chc in ["rock", "paper", "scissors"]:
   
   comp_choice = comp_chc()
   print(f"Computer chose: {comp_choice}")
   print(f"You chose: {user_chc}")
if user_chc == comp_choice:
       print("It's a tie!")
elif (user_chc == "rock" and comp_choice == "scissors") or (user_chc == "paper" and comp_choice == "rock") or (user_chc == "scissors" and comp_choice == "paper"):   
       print("You win!")
    
else:
        print("Computer wins!")
    
    