import random
def get_choices(): #this is the way to define a user defined function
    player_choice=input("Enter a choice (Rock, Paper, Scissor): ")
    options=["Rock", "Paper", "Scissor"]
    computer_choice=random.choice(options)
    choices={"player": player_choice, "computer":computer_choice}
    return choices



def check_win(player, computer):
    print("Your's Choice: "+player+"\n Computer's Choice: "+computer)
    #print(f"Your's choice: {player} \n Computer's Choice: {computer})
    if player == computer:
        return "Tie"
    elif player=="Rock":
        if computer=="Scissors":
            return "Player Wins"
        else:
            return "Computer Wins"
    elif player=="Paper":
        if computer=="Scissors":
            return "Computer Wins"
        else:
            return "Player Wins"
    elif player=="Scissors":
        if computer=="Rock":
            return "Computer Wins"
        else:
            return "Player Wins"
choices = get_choices()
result=check_win(choices["player"], choices["computer"])
print(result)
    


# def greeting(): ----A basic definition of user defined method----
#     return "Hi"

# response =greeting()
# print(response)



# dictionary
# dict={"name":"Tojo", "Color":choices}

#list

# food=["Pizza", "Carrots", "Eggs"]
# dinner=random.choice(food)
# print(dinner)