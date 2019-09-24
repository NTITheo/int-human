pin = 1234

userPin = int(input("Skriv in din pinkod: "))

if pin != userPin:
    exit()

saldo = 0

menu = 0
print ("menu 1 instättning")
print ("menu 2 uttag")  
print ("menu 3 avsluta")
while menu != 3:
    menu = int(input("Skriv in ditt val: "))
    if menu ==1: 
        print("insättning")
    elif menu == 2:
        print("uttag")
    else:
        print("Fel eller avslut")

