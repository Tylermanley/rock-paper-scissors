import numpy as np


while True:

    player_choice =input('select 1 for rock select 2 for paper select 3 for scissors ')

    player_choice = int(player_choice)

    computer_choice = np.random.randint(low=1,high=3,size=1)

    if player_choice == computer_choice[0]:
        print('tie')
    elif player_choice==1 and computer_choice[0]==3:
        print('congrats rock beat scissors')
    elif player_choice==2 and computer_choice[0]==1:
        print('congrats paper beats rock')
    elif player_choice==3 and computer_choice[0]==2:
        print('congrats scissors beats paper')
    elif computer_choice[0]==1 and player_choice==3:
        print('you lose rock beats scissors')
    elif computer_choice[0]==2 and player_choice==1:
        print('you lose paper beats rock')
    elif computer_choice[0]==3 and player_choice==2:
        print('you lose scissors beats paper')

