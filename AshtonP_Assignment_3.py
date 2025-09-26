# GITHUB LINK: https://github.com/pashton7/comp163-assignment-3
# Initialize our starting variables and ask for user input
ship_name = input("Enter the name of your ship: ") # Has no actual usage except for Stat display
ship_health = 100 # Used to determine if player has died
ship_crew = ["Steve","Roe","E.T"] # List of crewmembers the player can loose 
heavy_weapons = False # Bool option that is toggle to True based on user decisions
has_scanner = False #  Bool option that is toggle to True based on user decisions
money = 0 # The "Score" counter for the game. You want the most amount to "win"

event_choices = [] # A list that is inserted with past even choices for stat display
game_event = ["Salvage","Battle","Rescue"] # A list of valid events that players can choose

# Have users pick a ship focus that will greatly affect the outcome/ending
print("""Now that you've named your ship its time to decide its primary focus.
      A.) Health - You ship invests in outlasting your opponent rather than outfiring them
      B.) Scanner - It helps to know what's ahead so you can prepare for danger. This focus ensures you know what comes next.
      C.) Weapons - Decimate your opponent with heavy weapons
      """)
ship_choice = input("Your choice (A, B, C): ")

if ship_choice == "A":
    ship_health += 50
elif ship_choice == "B":
    has_scanner = True
elif ship_choice == "C":
    heavy_weapons = True
else:
    print(f"{ship_choice} is an invalid option. Please try again.")

print("Now that your ready to venture into space let's decide what you want to do.")
print(f"Choose from the following options on what you want to do {game_event}: ")
event_choice = input(f"Your choice {game_event}: ")
event_choices.append(event_choice)
print()

# Handle the game logic and branching where each player choice effects the ending
if event_choice in game_event: # Check if the option is in the list of valid options
    if event_choice == "Salvage": # Only runs if "Salvage" option was chosen
        game_event.remove(event_choice) # Remove it from the list of valid options in the future so it cant be repeated
        if has_scanner is True: # Branch only runs if user chose ship B
            print("Your scanners picked up no dangerous lifeforms or dangerous ships, leading you to a successful salvage. You gained +25 Money") # Display decision outcome 
            money += 25 # Make variable changes to match outcome
        elif ship_choice == "A": # Branch only runs if user chose ship A
            print("Because you have no scanners you are unaware of any danger. While attempting to salvage a rouge turret fires upon your ship. Ship Health: -10, Money: +15")
            ship_health -= 10
            money += 15
        elif heavy_weapons is True: # Branch only runs if user chose ship C
            print("Being unable to scan for danger has you cautious, you fire your cannons to ensure the wreck is safe to salvage, destroying some of the loot in the process. Money: +6")
            money += 6
    elif event_choice == "Rescue": # Only runs if "Rescue" option was chosen
        game_event.remove(event_choice)
        if has_scanner is True:
            print("After recieving a distress signal you scan the vessel for danger. Your scanners pick up that the distress signal is coming from a crew of dangerous rouge \nandroids you destroy their vessel and salvage the wreck. Money: +10")
            money += 10
        elif ship_choice == "A":
            print("You've just recieved a distress signal, but you are unaware of any danger that might be present.")
            print("You must choose your next decision wisely:\nA.) Take no chances and destroy the ship\nB.) Take the chance of saving lives")
            # Having players put in a nested input to give players more decisions on what to do
            rescue_choice = input("Your choice (A, B): ")
            if rescue_choice == "A":
                print("Unwilling to take any risks you destroy their ship. Unfortunatly those aboard were infact in need of aid. But at least you were able to salvage something. Money: +20")
                money += 20
            elif rescue_choice == "B":
                print("Being the selfless captain you are you take the risk and help those in need. Luckily for you the crew you saved were peaceful. In their gratitude they \noffer you money and one pledges himself to your crew.")
                print(f'Crew member gained: Rogers, Money: +10')
                money += 10
                ship_crew.append("Rogers")
            else:
                print(f"'{rescue_choice}' is not a valid option. Please try again.")
        elif heavy_weapons is True:
            print("After recieving a message requesting aid you jump to the rescue. Encountering a large vessel poised for attack!")
            print("After a lengthy and hard fought battle you save the endangered crew but not without casualties. Luckily the crew you saved is  greatful and compensated you the best they could.")
            print(f"Ship damaged: -30, Crew member lost: {ship_crew[1]}, Money: +25")
            ship_health -= 30
            ship_crew.pop(1)
            money += 25
    elif event_choice == "Battle": # Only runs if "Battle" option was chosen
        game_event.remove(event_choice)
        if has_scanner is True:
            print("While flying across the galaxy you encounter a vessel with a bounty on its head. Unfortunatly they have jammed your scanners leaving you unaware of their power.")
            print("Will you decide to:\nA.) Engage in battle and collect the bounty\nB.) Do not engage the ship and flee")
            battle_choice = input("Your choice (A, B): ")
            if battle_choice == "A":
                print(f"You decided to ingore the risk and attack the vessel. It was a hard fought battle but the firepower of the enemy vessel was too strong and your ship was destroyed in battle. Health: -{ship_health}")
                ship_health -= ship_health
            elif battle_choice == "B":
                print("You decided to flee rather than engage. A bold move as your scanners picked up that the ship was heavy armored and armed.")
            else:
                print(f"{battle_choice} is not a valid option. Please try again.")
        elif ship_choice == "A":
            print("While traveling across the galaxy you are attacked by pirates. They've given you two options,  pay them or die.")
            print("What will you do?: \nA.) Concede, theres no risk getting hurt\nB.) A pirate cannot be trusted, all hands on deck!")
            # Having players put in a nested input to give players more decisions on what to do
            battle_choice2 = input("Your choice (A, B): ")
            if battle_choice2 == "A":
                print(f"You concede and are willing to pay the price they ask, consequently they have taken a large sum of money and one of your crew members\n Crewmember lost: {ship_crew[0]}, Money: -60")
                ship_crew.pop(0)
                money -= 60
            elif battle_choice2 == "B":
                print("Unwilling to negotiate with pirate you attack! Lasers stream across the cold vaccum of space until you emerge the victor. You salvage the remains of their vessel and save a prisoner who joins your crew.")
                print("New Crewmember: Stannis, Money: +15")
                ship_crew.append("Stannis")
                money += 15
            else:
                print(f"{battle_choice2} is not a valid option. Please try again.")
        elif heavy_weapons is True:
            print("You come across a battle between smugglers and a bounty hunter. They both have requested of your help, the smugglers offer you a portion of their goods but the bounty hunter offers you a portion of the bounty reward.")
            print("What will you do?:\nA.) Side with the smugglers they might have valuable goods.\nB.) Side with the bounty hunter, the reward might be greater than the risks.\nC.) My enemies are many, my equals are none. Attack both and claim the rewards for yourself!")
            # Having players put in a nested input to give players more decisions on what to do
            battle_choice3 = input("Your choice (A, B, C): ")
            if battle_choice3 == "A":
                print("You decide to team up with the smugglers and you easily take down the bounty hunter. As thanks the smugglers give you a portion of their loot and you salvage the remains of the bounty hunter's ship.")
                print("Health: -10, Money: +38")
                ship_health -= 10
                money += 38
            elif battle_choice3 == "B":
                print("You decide that its better to take a portion of the bounty than possibly low value goods. You and the bounty hunter easily overwhelm the smugglers and destroy them. The bounty hunter gives you a portion of the bounty and you salvage the remains of the smugglers ship.")
                print("Health: -5, Money: +24")
                ship_health -= 5
                money += 24
            elif battle_choice3 == "C":
                print("You decide its more profitable to take down both ships and claim the rewards for yourself. After engaging in a long gruely battle you come out victorious. Claiming the remains of both ships and collecting the smugglers bounty.")
                print("Health: -48, Money: +80")
                ship_health -= 48
                money += 80
            else:
                print(f"{battle_choice3} is an invalid option. Please try again.")
else:
    print(f"{event_choice} is an invalid option. Please try again.")

# Run game logic again to have end game results differ
print(f"Choose from the following options on what you want to do next {game_event}: ")
event_choice = input(f"Your choice {game_event}: ")
event_choices.append(event_choice)
print()

if event_choice in game_event: # Check if the option is in the list of valid options
    if event_choice == "Salvage": # Only runs if "Salvage" option was chosen
        game_event.remove(event_choice) # Remove it from the list of valid options in the future so it cant be repeated
        if has_scanner is True: # Branch only runs if user chose ship B
            print("Your scanners picked up no dangerous lifeforms or dangerous ships, leading you to a successful salvage. You gained +25 Money") # Display decision outcome 
            money += 25 # Make variable changes to match outcome
        elif ship_choice == "A": # Branch only runs if user chose ship A
            print("Because you have no scanners you are unaware of any danger. While attempting to salvage a rouge turret fires upon your ship. Ship Health: -10, Money: +15")
            ship_health -= 10
            money += 15
        elif heavy_weapons is True: # Branch only runs if user chose ship C
            print("Being unable to scan for danger has you cautious, you fire your cannons to ensure the wreck is safe to salvage, destroying some of the loot in the process. Money: +6")
            money += 6
    elif event_choice == "Rescue": # Only runs if "Rescue" option was chosen
        game_event.remove(event_choice)
        if has_scanner is True:
            print("After recieving a distress signal you scan the vessel for danger. Your scanners pick up that the distress signal is coming from a crew of dangerous rouge \nandroids you destroy their vessel and salvage the wreck. Money: +10")
            money += 10
        elif ship_choice == "A":
            print("You've just recieved a distress signal, but you are unaware of any danger that might be present.")
            print("You must choose your next decision wisely:\nA.) Take no chances and destroy the ship\nB.) Take the chance of saving lives")
            # Having players put in a nested input to give players more decisions on what to do
            rescue_choice = input("Your choice (A, B): ")
            if rescue_choice == "A":
                print("Unwilling to take any risks you destroy their ship. Unfortunatly those aboard were infact in need of aid. But at least you were able to salvage something. Money: +20")
                money += 20
            elif rescue_choice == "B":
                print("Being the selfless captain you are you take the risk and help those in need. Luckily for you the crew you saved were peaceful. In their gratitude they \noffer you money and one pledges himself to your crew.")
                print(f'Crew member gained: Rogers, Money: +10')
                money += 10
                ship_crew.append("Rogers")
            else:
                print(f"'{rescue_choice}' is not a valid option. Please try again.")
        elif heavy_weapons is True:
            print("After recieving a message requesting aid you jump to the rescue. Encountering a large vessel poised for attack!")
            print("After a lengthy and hard fought battle you save the endangered crew but not without casualties. Luckily the crew you saved is  greatful and compensated you the best they could.")
            print(f"Ship damaged: -30, Crew member lost: {ship_crew[1]}, Money: +25")
            ship_health -= 30
            ship_crew.pop(1)
            money += 25
    elif event_choice == "Battle": # Only runs if "Battle" option was chosen
        game_event.remove(event_choice)
        if has_scanner is True:
            print("While flying across the galaxy you encounter a vessel with a bounty on its head. Unfortunatly they have jammed your scanners leaving you unaware of their power.")
            print("Will you decide to:\nA.) Engage in battle and collect the bounty\nB.) Do not engage the ship and flee")
            battle_choice = input("Your choice (A, B): ")
            if battle_choice == "A":
                print(f"You decided to ingore the risk and attack the vessel. It was a hard fought battle but the firepower of the enemy vessel was too strong and your ship was destroyed in battle. Health: -{ship_health}")
                ship_health -= ship_health
            elif battle_choice == "B":
                print("You decided to flee rather than engage. A bold move as your scanners picked up that the ship was heavy armored and armed.")
            else:
                print(f"{battle_choice} is not a valid option. Please try again.")
        elif ship_choice == "A":
            print("While traveling across the galaxy you are attacked by pirates. They've given you two options,  pay them or die.")
            print("What will you do?: \nA.) Concede, theres no risk getting hurt\nB.) A pirate cannot be trusted, all hands on deck!")
            # Having players put in a nested input to give players more decisions on what to do
            battle_choice2 = input("Your choice (A, B): ")
            if battle_choice2 == "A":
                print(f"You concede and are willing to pay the price they ask, consequently they have taken a large sum of money and one of your crew members\n Crewmember lost: {ship_crew[0]}, Money: -60")
                ship_crew.pop(0)
                money -= 60
            elif battle_choice2 == "B":
                print("Unwilling to negotiate with pirate you attack! Lasers stream across the cold vaccum of space until you emerge the victor. You salvage the remains of their vessel and save a prisoner who joins your crew.")
                print("New Crewmember: Stannis, Money: +15")
                ship_crew.append("Stannis")
                money += 15
            else:
                print(f"{battle_choice2} is not a valid option. Please try again.")
        elif heavy_weapons is True:
            print("You come across a battle between smugglers and a bounty hunter. They both have requested of your help, the smugglers offer you a portion of their goods but the bounty hunter offers you a portion of the bounty reward.")
            print("What will you do?:\nA.) Side with the smugglers they might have valuable goods.\nB.) Side with the bounty hunter, the reward might be greater than the risks.\nC.) My enemies are many, my equals are none. Attack both and claim the rewards for yourself!")
            # Having players put in a nested input to give players more decisions on what to do
            battle_choice3 = input("Your choice (A, B, C): ")
            if battle_choice3 == "A":
                print("You decide to team up with the smugglers and you easily take down the bounty hunter. As thanks the smugglers give you a portion of their loot and you salvage the remains of the bounty hunter's ship.")
                print("Health: -10, Money: +38")
                ship_health -= 10
                money += 38
            elif battle_choice3 == "B":
                print("You decide that its better to take a portion of the bounty than possibly low value goods. You and the bounty hunter easily overwhelm the smugglers and destroy them. The bounty hunter gives you a portion of the bounty and you salvage the remains of the smugglers ship.")
                print("Health: -5, Money: +24")
                ship_health -= 5
                money += 24
            elif battle_choice3 == "C":
                print("You decide its more profitable to take down both ships and claim the rewards for yourself. After engaging in a long gruely battle you come out victorious. Claiming the remains of both ships and collecting the smugglers bounty.")
                print("Health: -48, Money: +80")
                ship_health -= 48
                money += 80
            else:
                print(f"{battle_choice3} is an invalid option. Please try again.")
else:
    print(f"{event_choice} is an invalid option. Please try again.")

# Give players a summary of how they did
print("Game results:\n")
if ship_health <= 55 and ship_health > 0 and money > 60:
    print("Summary: You sacrificed losing your ship to gain wealth. Luckily it worked out for you.")
elif ship_health >= 100 and money >= 40:
    print("Summary: You played a safe and cautious game and left with some spoils.")
elif len(ship_crew) < 3:
    print("Summary: Your recklessness led to the loss of your crewmembers. I hope it was worth it.")
elif ship_health >= 80 and money < 40:
    print("Summary: You played it very safe and unfortunatly came up with nothing. Make some risks if you want to make some money.")
elif len(ship_crew) > 3:
    print("Summary: You worked hard to keep your crew alive and picked up some extra members along the way")
elif ship_health <= 0:
    print("Summary: You failed as a captian. You let you, your ship, and your crew perish.")
else: # If all other checks are False then display this default message
    print("Summary: You played an average game and came out with nothing.")

# Give players a rundown of their stats
print("=== GAME STATS ===")
print(f"Ship name: {ship_name}")
print(f"Ship choice: {ship_choice}")
print(f"Event Choices: {event_choices}")
print(f"Ship Health: {ship_health}")
print(f"Ship Crew: {ship_crew}")
print(f"Money: {money}")