#import random

userPin = 1234

if userPin != int(input("Skriv in din pinkod: ")):
    

#f = open("saldo.txt", "r")
#saldo = int(f.read())
#print (saldo)
#f.close()
#saldo = 0.0
#if pin != userPin:
#    exit()
#file = open("saldo.txt", "r+")
#saldo = file.read()
#print(saldo)
#file.close()

#saldo = 0.0
# #saldo = random.randint (0,100000000)
f = open("saldo.txt", 'r') #
saldo = float(f.read())
f.close()



menu = 0
while menu != 4:  #Detta är en loop som fungerar som en meny, med en vilkors sats med olika funktioner
    print ("menu 1 instättning")
    print ("menu 2 uttag")  
    print ("menu 3 Balance")
    print ("menu 4 Avsluta")
    print("Ditt saldo är: " + str(saldo) + "kr")
    menu = int(input("Skriv in ditt val[1, 2, 3, 4]: "))
    if menu == 1: 
        saldo = saldo + float(input("Gör en insättning: "))
    elif menu == 2:
        saldo = saldo - float(input("Gör ett uttag: "))
    elif menu == 3:
        print (saldo)
    else:
        print("Fel eller avslut")
f = open('saldo.txt', 'w')
f.write(str(saldo))
f.close()





#while menu != 3:
#    menu = int(input("Skriv in ditt val: "))
#    if menu ==1: 
#        print("insättning")
#    elif menu == 2:
#        print("uttag")
#    else:
#        print("Fel eller avslut")

