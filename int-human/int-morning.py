# Start

# vakna upp
vaken = "n"
print("Du sover som en stock...")
while vaken == "n":
    vaken = input("Vaknar du? [y/n] ").lower()

# duscha5
print("Du masar dig upp och släpar dig i duschen.")
print("Någon har lämmnat en brödrost i din dusch")

duscha = input("Flyttar du på brödrosten? [y/n] ").lower()

if duscha == "n":     #if, else sats om man ska du eller icket då man duschar pga att man duschar med brödrosten
    print("Du elchockas och dör") 
    exit()
elif duscha == "y":
    print("Kallt vatten sköljer över dig.")
else:
    print("Does not compute")
# Kläder

season = False     #
while season == False:
    season = input("Vilken årstid är det? [vår, vinter, sommar, höst]").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt och halt ute!")
        print("Ta på anti kylla kläderna")
    elif season == "sommar":
            print("Sommar, flipflops och badbyxor.")
    else:
            season = False
        
resa = input("Moppe? [y/n] ").lower()
