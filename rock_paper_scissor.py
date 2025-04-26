import random
rock='''   
                                       /\| | | |
                                      / /|_|_|_|
                                      \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
          / ---._.---._.---\        /       /
          \||    '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
'''
paper=''' 
          __________
         |DAILY NEWS|
         |&&& ======|
         |=== ======|
         |=== == %%$|
         |[_] ======|
         |=== ===!##|
         |__________|
'''

scissor=''' ____
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/'''


image = [rock,paper,scissor]

user_choice= int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissor:\n "))

if user_choice==0 or user_choice==1 or user_choice==2:
    print(image[user_choice])
    pc_choice= random.randint(0,2)
    print(f"Computer chose {pc_choice}")
    print(image[pc_choice])

# Rock (0), Paper (1), Scissors (2)

    if user_choice== pc_choice:
     print("Draw")

    elif user_choice ==0 and pc_choice==1:
     print("Computer Won!!!!!!")

    elif user_choice==0 and pc_choice==2:
     print("You win!!!!")

    elif user_choice ==1 and pc_choice==0:
     print("You win!!!!!!")

    elif user_choice ==1 and pc_choice==2:
     print("Computer won!!!!!")

    elif user_choice ==2 and pc_choice==1:
     print("You won!!!!!")
    elif user_choice ==2 and pc_choice==0:
     print("Computer won!!!!!")

 
else:
    print("Wrong input.Try again...")
