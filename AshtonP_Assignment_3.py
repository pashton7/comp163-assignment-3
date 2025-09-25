# GITHUB LINK
# Initialize our starting variables and ask for user input
ship_name = input("Enter the name of your ship: ")
ship_health = 100
ship_crew = ["Steve","Roe","E.T"]
ship_weapons_damage = 10
has_scanner = False
money = 0

game_event = ["Salvage","Battle","Rescue"]

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
    ship_weapons_damage += 10
else:
    print(f"{ship_choice} is an invalid option. Please try again.")

print("Now that your ready to venture into space let's decide what you want to do.")
print(f"Choose from the following options on what you want to do {game_event}: ")
event_choice = input(f"Your choice {game_event}: ")


if event_choice == "Salvage":
    if has_scanner == True:
        print("Your scanners picked up no dangerous lifeforms or dangerous ships, leading you to a successful salvage. You gained +25 Money")
        credits += 25
    elif ship_choice == "A":
        print("Because you have no scanners you are unaware of any danger. While attempting to salvage a rouge turret fires upon your ship. Ship Health: -10, Money: +15")
        ship_health -= 10
        money += 15
    elif ship_choice == "C":
        print("Being unable to scan for danger has you cautious, you fire your cannons to ensure the wreck is safe to salvage, destroying some of the loot in the process. Money: +6")
        money += 6
    game_event.remove("Salvage")
elif event_choice == "Rescue":
    if has_scanner == True:
        print("""After recieving a distress signal you scan the vessel for danger. Your scanners pick up that 
              the distress signal is coming from a crew of dangerous rouge androids
              you destroy their vessel and salvage the wreck. Money: +10
              """)
    elif ship_choice == "A":
        print("You've just recieved a distress signal, but you are unaware of any danger that might be present.")
        print("You must choice your next decision wisely: A.) Take no chances and destroy the ship\nB.) Take the chance of saving lives")
        rescue_choice = input("Your choice (A,B): ")
        if rescue_choice == "A":
            print("Unwilling to take any risks you destroy their ship. Unfortunatly those aboard were infact in need of aid. But at least you were able to salvage something. Money: +20")
            money += 20
        elif rescue_choice == "B":
            print("Being the selfless captain you are you take the risk and help those in need. Luckily for you the crew you saved were peaceful. In their gratitude they offer you money and one pledges himself to your crew.")
            print(f'Crew member gained: Rogers, Money: +10')
        else:
            print(f"'{rescue_choice}' is not a valid option. Please try again.")
    elif ship_choice == "C":
        print("After recieving a message requesting aid you jump to the rescue. Encountering a large vessel poised for attack!")
        print("After a lengthy and hard fought battle you save the endangered crew but not without casualties. Luckily the crew you saved is  greatful and compensated you the best they could.")
        print(f"Ship damaged: -30, Crew member lost: {ship_crew[1]}, Money: +25")
        ship_health -= 30
        ship_crew.pop(1)
        money +=25