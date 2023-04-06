
totale = float(input("le poids d'echontillon"))
print(totale, "g")

#matieres inertes
mi = float(input("matieres inertes:"))
print(mi, "g")
pmi = (mi/totale)*100
print(pmi, "%")



#graines mutilées-débris végétaux-balles-terres-graviers-autr:
graines_mdv = float (input("graines mutilées-débris végétaux-balles-terres-graviers-autr:"))
print(graines_mdv)


#semences dautres plantes
sap = float(input("semences dautres plantes"))
print(sap, "g")


#ble tendre
bt = float(input("ble tendre:"))
print(bt, "g")
pbt = (bt/totale)*100
print(pbt, "%")


#orge
o = float(input(" orge "))
print(o, "g")
po = (o/totale)*100
print(po, "%")


#semences pures
sp = totale-(o+mi+bt)
print(sp, "g")
psp = (sp/totale)*100
print(psp, "%")


#decision
if psp >= 99:
    print("accepter")
    print("pré base et base")
elif psp >= 98:
    print("refuser")
    print("reproduction")
elif psp >= 97:
    print("refuser")
    print("ordinaire")
else: print("refuser")




