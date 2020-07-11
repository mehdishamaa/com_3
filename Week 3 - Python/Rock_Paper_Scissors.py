import random



def rock_paper_scissors():

    print("Press 1 for Rock")
    print("Press 2 for Scissors")
    print("Press 3 for Paper")
    user_selection = (input("Please select your choice!:"))
    comp_choices = ["Rock", "Paper", "Scissors"]
    comp_choice = comp_choices[random.randint(0, 2)]
    if user_selection == 1 and comp_choice == 0:
        print("Computer has chosen rock! DRAW!")










