import random
item_list = ["Rock" , "Paper" , "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
computer_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice ={computer_choice}")

if user_choice == computer_choice:
    print("tie")

elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("computer wins")
    else:
        print("You Win")

elif user_choice == "Paper":
    if computer_choice == "Scissor" :
        print("computer wins")
    else:
        print("You Win")

elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("computer wins")
    else:
        print("You Win")
print("nice play!")