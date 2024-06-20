import os

def first_screen():
    print("Welcome to the Lego Shop!")

    print("Here are the stocks today!")
    print("1. WWII Panzerkampfwagen VI Tiger Ausf. E 1/144 scale set - $500")
    print("2. WWII Panzerabwehrkanone 43/1 Ausführung Fahrgestell Panzerkampfwagen III und IV 1/144 scale set - $250")
    print("3. WWII T26E4 Super Pershing 1/144 scale set - $560")
    print("4. WWII IS-6 Soviet tier 8 premium heavy tank 1/144 scale set - $490")
    print("5. WWII Panzerkampfwagen VIII Maus 1/144 scale set - $800")
    print("6. WWII Reaktnivnyj Snarjad (self-propellant rocket) 132 1/144 scale set - $320")
    print("7. Rocket Launcher T34 (Calliope)  1/144 scale set - $260")

    print("Just type the number of the item of your choice.")
    item_choice = input("What set is your choice? = ")
    second_screen(item_choice)

    os.system('cls')


def second_screen(item_choice):
    while True:
        if item_choice == '1':
            print("Thank you~ Please proceed to the payment section!")
            print("Panzerkampfwagen VI Tiger Ausf. E 1/144 scale set for $500")
        elif item_choice == '2':
            print("Thank you~ Please proceed to the payment section!")
            print("Panzerabwehrkanone 43/1 Ausführung Fahrgestell Panzerkampfwagen III und IV 1/144 scale set for $250")
        elif item_choice == '3':
            print("Thank you~ Please proceed to the payment section!")
            print("T26E4 Super Pershing 1/144 scale set for $560")
        elif item_choice == '4':
            print("Thank you~ Please proceed to the payment section!")
            print("IS-6 Soviet tier 8 premium heavy tank 1/144 scale set for $490")
        elif item_choice == '5':
            print("Thank you~ Please proceed to the payment section!")
            print("Panzerkampfwagen VIII Maus 1/144 scale set for $800")
        elif item_choice == '6':
            print("Thank you~ Please proceed to the payment section!")
            print("Reaktnivnyj Snarjad (self-propellant rocket) 132 1/144 scale set for $320")
        elif item_choice == '7':
            print("Thank you~ Please proceed to the payment section!")  
            print("Rocket Launcher T34 (Calliope)  1/144 scale set for $260")
        else:
            print("choose again!")
            break

first_screen()