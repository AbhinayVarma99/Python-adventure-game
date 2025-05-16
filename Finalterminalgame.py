import random

name = str(input('enter your name : '))
print(name + ' welcome to Terminal adventure')
HP = 100
NPC_HP = 100
is_defending = False  

while HP > 0 and NPC_HP > 0:
    print(f'\nYour HP: {HP}')
    print(f'NPC HP: {NPC_HP}')

    option = int(input('Choose your action: 1.Attack 2.Defense 3.Heal '))
    is_defending = False

    MC = random.randint(1, 10)
    NPC = random.randint(1, 10)
    print(f'\n{name}\'s roll: {MC}')
    print(f'NPC\'s roll: {NPC}')

    if MC > NPC:
        if option == 1:
            damage = 20
            NPC_HP -= damage
            print(f'You attacked and dealt {damage} damage!')
        elif option == 2:
            print('You are defending!')
            is_defending = True 
        elif option == 3:
            heal = 15
            HP += heal
            print(f'You healed for {heal} HP!')
        else:
            print('Invalid option.')
    elif MC < NPC:
        if option == 1:
            print('Your attack missed!')
        elif option == 2:
            print('You tried to defend but the NPC\'s roll was higher!')
            is_defending = True 
        elif option == 3:
            print('Your heal was not effective enough!')
        else:
            print('Invalid option.')
    else:  
        print('It\'s a draw! No action this turn.')

    # NPC's turn
    if NPC_HP > 0:
        npc_action = random.randint(1, 3)
        print('\nNPC\'s turn...')
        if npc_action == 1:
            npc_damage = 15
            if NPC > MC and not is_defending:
                if is_defending:
                    damage_taken = npc_damage // 2 
                    HP -= damage_taken
                    print(f'NPC attacked, but you defended and only took {damage_taken} damage!')
                else:
                    HP -= npc_damage
                    print(f'NPC attacked and dealt {npc_damage} damage!')
            else:
                print('NPC\'s attack missed!')
        elif npc_action == 2:
            print('NPC defended!')
        elif npc_action == 3:
            npc_heal = 10
            if NPC > MC:
                NPC_HP += npc_heal
                print(f'NPC healed for {npc_heal} HP!')
            else:
                print('NPC\'s heal was not effective enough!')

    if HP <= 0:
        print('\nYou have been defeated!')
    elif NPC_HP <= 0:
        print(f'\nCongratulations! You defeated the NPC!')

print('\nGame Over!')