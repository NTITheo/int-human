import random

pin = 1234

userPin = int(input("Skriv in din pinkod: "))


#saldo = 0.0
#if pin != userPin:
#    exit()
#file = open("saldo.txt", "r+")
#saldo = file.read()
#print(saldo)
#file.close()


saldo = random.randint (0,100000000)
menu = 0
print ("menu 1 instättning")
print ("menu 2 uttag")  
print ("menu 3 avsluta")
while menu != 3:
    print("Ditt saldo är: " + str(saldo) + "kr")
    menu = int(input("Skriv in ditt val[1, 2, 3]: "))
    if menu == 1: 
        saldo = saldo + float(input("Gör en insättning: "))
    elif menu == 2:
        saldo = saldo - float(input("Gör ett uttag: "))
    else:
        print("Fel eller avslut")
f = open('saldo.txt', 'a')
f.write(str(saldo) + "Kr" + '\n')
f.close()





#while menu != 3:
#    menu = int(input("Skriv in ditt val: "))
#    if menu ==1: 
#        print("insättning")
#    elif menu == 2:
#        print("uttag")
#    else:
#        print("Fel eller avslut")

