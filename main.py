#le poid de recolte en quintaux
poids = float(input("la Quantité de recolte (q):"))

print(poids)

#le Poid spécifique
#valeur
print("entrée la valeure")
ps= float(input("Poid spécifique kg/hl:"))
print(ps)
#observation
print("observation")
if ps == 78:
    print("sans bonification ni réfaction")
elif ps > 78:
    print("bonification")
elif ps >74 and ps < 78:
    print(" refaction")
elif ps < 74:
    print("refuser")

#Bonification/Rèfaction(DA)/q
print("Bonification/Rèfaction(DA)/q")
vps = 0.00
if ps <= 77.99 and ps >= 77.75:
    vps = -0.25
    print(vps)
elif ps <=77.749 and ps >= 77.5:
    vps = -0.5
    print(vps)
elif ps <= 77.499 and ps >= 77.25:
    vps = -0.75
    print(vps)
elif ps <= 77.249 and ps >= 77:
    vps = -1
    print(vps)
elif ps <= 76.99 and ps>=76.75:
    vps = -1.35
    print(vps)
elif ps<=76.749 and ps>=76.5:
    vps = -1.7
    print(vps)
elif ps <= 76.499 and ps>=76.25:
    vps = -2.05
    print(vps)
elif ps <= 76.249 and ps >= 76:
    vps = -2.4
    print(vps)
elif ps <= 75.999 and ps >=75.75:
    vps = -2.9
    print(vps)
elif ps <= 75.749 and ps >= 75.5:
    vps = -3.4
    print(vps)
elif ps <=75.499 and ps >=75.25:
    vps = -3.9
    print(vps)
elif ps <=75.249 and ps>=75:
    vps = -4.4
    print(vps)
elif ps<=74.999 and ps>=74.75:
    vps = -4.9
    print(vps)
elif ps <= 74.749 and ps>=74.5:
    vps = -5.4
    print(vps)
elif ps<=74.999 and ps >=74.25:
    vps = -5.9
    print(vps)
elif ps <= 74.249 and ps>=74:
    vps = -6.4
    print(vps)
elif ps>=78.001 and ps<=78.25:
    vps = +0.15
    print(vps)
elif ps>=78.251 and ps<=78.5:
    vps = +0.3
    print(vps)
elif ps >=78.501 and ps<=78.75:
    vps = +0.45
    print(vps)
elif ps>=78.751 and ps<=79:
    vps = +0.6
    print(vps)
elif ps>=79.001 and ps <=79.25:
    vps = +0.75
    print(vps)
elif ps>=79.251 and ps<=79.5:
    vps = +0.9
    print(vps)
elif ps>=79.501 and ps<=79.75:
    vps = +1.05
    print(vps)
elif ps>=79.751 and ps<=80:
    vps = +1.20
    print(vps)
elif ps>=80.001 and ps<=80.25:
    vps = +1.35
    print(vps)
elif ps>=80.251 and ps<=80.5:
    vps = +1.5
    print(vps)
elif ps>=80.501 and ps<=80.75:
    vps = +1.65
    print(vps)
elif ps>=80.751 and ps<=81:
    vps = +1.80
    print(vps)
elif ps>=81.001 and ps<=81.25:
    vps = +1.95
    print(vps)
elif ps>=81.251 and ps<=81.5:
    vps = +2.1
    print(vps)
elif ps>=81.501 and ps<=81.75:
    vps = +2.25
    print(vps)
elif ps>=81.751 and ps<=82:
    vps = +2.4
    print(vps)
elif ps>=82.001 and ps<=82.25:
    vps = +2.5
    print(vps)
elif ps>=82.251 and ps<=82.5:
    vps = +2.6
    print(vps)
elif ps>=82.501 and ps<=82.75:
    vps = +2.7
    print(vps)
elif ps>=82.751 and ps<=83:
    vps = +2.8
    print(vps)
elif ps>=83.001 and ps<=83.25:
    vps = +2.85
    print(vps)
elif ps>=83.251 and ps<=83.5:
    vps = +2.9
    print(vps)
elif ps>=83.5 and ps<=83.75:
    vps = +2.95
    print(vps)
elif ps>=83.751 and ps<=84:
    vps = +3
    print(vps)
elif ps>=84.001 and ps<=84.25:
    vps = +3.05
    print(vps)
elif ps>=84.251 and ps<=84.5:
    vps = +3.1
    print(vps)
elif ps>=84.501 and ps<=84.75:
    vps = +3.15
    print(vps)
elif ps>=84.751 and ps<=85:
    vps = +3.2
    print(vps)
elif ps>=85.001 and ps<=85.25:
    vps = +3.25
    print(vps)
elif ps>=85.251 and ps<=85.5:
    vps = +3.3
    print(vps)
elif ps>=85.501 and ps<=85.75:
    vps = +3.35
    print(vps)
elif ps>85.75:
    vps = +3.35
    print(vps)
else: print("refuser")

#Humidité %
#valeur
print("entrée la valeure")
h= float(input("Humidité %:"))
print(h)
#observation
print("observation")
if h<= 17:
    print("accepter")
else: print("refuser")
#Bonification/Rèfaction(DA)/q
print("Bonification/Rèfaction(DA)/q")
print("-")
#Grains nuisibles  %
#valeur
print("entrée la valeure")
gn= float(input("Grains nuisibles  %:"))
print(gn)
#observation
print("observation")
if gn<=0.25 and gn>0.05:
    print("refaction")
elif gn<=0.05:
    print("accepter")
else:print("refuse")
#Bonification/Rèfaction(DA)/q
print("Bonification/Rèfaction(DA)/q")
vgn = 0.00
if gn>=0.051 and gn<=0.1:
    vgn = -0.05
    print(vgn)
elif gn>=0.101 and gn<=0.15:
    vgn = -0.1
    print(vgn)
elif gn>=0.151 and gn<=0.2:
    vgn = -0.15
    print(vgn)
elif gn>=0.201 and gn<=0.25:
    vgn = -0.2
    print(vgn)

#ergot  %
print("entrée la valeure")
e= float(input("ergot  %:"))
print(e)
#observation
print("observation")
if e<0.001:
    print("accepter")
else: print("refuser")
#Impurtès de 1er catégorie
#les débris végétaux  %
print("entrée la valeure")
dv= float(input("les débris végétaux  %:"))
print(dv)
#matiérs inertes  %
print("entrée la valeure")
mi= float(input("matiérs inertes  %:"))
print(mi)
#grains sons valours  %
print("entrée la valeure")
gsv= float(input("grains sons valours  %:"))
print(gsv)
#grains cariés  %
print("entrée la valeure")
gcr = float(input("grains cariés  %:"))
print(gcr)
# totale de Impurtès de 1er catégorie
t1 = dv + mi + gsv + gcr
print("total de 1er categorie:",t1)
#observation
print("observation")
if t1<=1:
    print("sans bonification ni réfaction")
else:print("réfaction")
#Bonification/Rèfaction(DA)/q
print("Bonification/Rèfaction(DA)/q")
vt1 = 0.00
if t1<=0.999 and t1>=0.75:
    vt1 = +0.15
    print(vt1)
elif  t1<=0.749 and t1>=0.5:
    vt1 = +0.3
    print(vt1)
elif t1<=0.499 and t1>=0.25:
    vt1 = +0.45
    print(vt1)
elif  t1<=0.249 and t1>=0:
    vt1 = +0.6
    print(vt1)
elif t1>=1.01 and t1<=1.25:
    vt1 = -0.15
    print(vt1)
elif t1>=1.26 and t1<=1.5:
    vt1 = -0.3
    print(vt1)
elif t1>=1.51 and t1<=1.75:
    vt1 = -0.45
    print(vt1)
elif t1>=1.76 and t1<=2:
    vt1 = -0.6
    print(vt1)
elif t1>=2.01 and t1<=2.25:
    vt1 = -0.75
    print(vt1)
elif t1>=2.26 and t1<=2.5:
    vt1 = -0.9
    print(vt1)
elif t1>=2.51 and t1<=2.75:
    vt1 = -1.05
    print(vt1)
elif t1>=2.76 and t1<=3:
    vt1 = -1.2
    print(vt1)

#Impurtès de 2eme catégorie
#Grains cassés  %
print("entrée la valeure")
gcs= float(input("Grains cassés  %:"))
print(gcs)
#observation
print("observation")
if gcs<=3:
    print("sans bonification ni réfaction")
else: print("réfaction")
#Bonification/Rèfaction(DA)/q
print("Bonification/Rèfaction(DA)/q")
vgcs = 0.00
if gcs>=3.01 and gcs<=3.25:
    vgcs = -0.05
    print(vgcs)
elif gcs>=3.26 and gcs<=3.5:
    vgcs = -0.1
    print(vgcs)
elif gcs>=3.51 and gcs<=3.75:
    vgcs = -0.15
    print(vgcs)
elif gcs>=3.76 and gcs<=4:
    vgcs = -0.2
    print(vgcs)
elif gcs>=4.01 and gcs<=4.25:
    vgcs = -0.25
    print()
elif gcs>=4.26 and gcs<=4.5:
    vgcs = -0.3
    print(vgcs)
elif gcs>=4.51 and gcs<=4.75:
    vgcs = -0.35
    print(vgcs)
elif gcs>=4.76 and gcs<=5:
    vgcs = -0.4
    print(vgcs)
elif gcs>=5.01 and gcs<=5.25:
    vgcs = -0.475
    print(vgcs)
elif gcs>=5.26 and gcs<=5.5:
    vgcs = -0.55
    print(vgcs)
elif gcs>=5.51 and gcs<=5.75:
    vgcs = -0.625
    print(vgcs)
elif gcs>=5.76 and gcs<=6:
    vgcs = -0.7
    print(vgcs)
elif gcs>=6.01 and gcs<=6.25:
    vgcs = -0.775
    print(vgcs)
elif gcs>=6.26 and gcs<=6.5:
    vgcs = -0.850
    print(vgcs)
elif gcs>=6.51 and gcs<=6.75:
    vgcs = -0,925
    print(vgcs)
elif gcs>=6.76 and gcs<=7:
    vgcs = -1.0
    print(vgcs)
elif gcs>=7.01 and gcs<=7.25:
    vgcs = -1.075
    print(vgcs)
elif gcs>=7.26 and gcs<=7.5:
    vgcs = -1.15
    print(vgcs)
elif gcs>=7.51 and gcs<=7.75:
    vgcs = -1.225
    print(vgcs)
elif gcs>=7.76 and gcs<=8:
    vgcs : -1.3
    print(vgcs)

print("entrée la valeure")
gm= float(input("Grains maigres  %:"))
print(gm)


print("entrée la valeure")
gech= float(input("Grains échaudés  %:"))
print(gech)


print("entrée la valeure")
geb= float(input("Grains etranders utilisable pour le bétail  %:"))
print(geb)


print("entrée la valeure")
groux= float(input("Grains de blé dur roux  %:"))
print(groux)


print("entrée la valeure")
gfm= float(input("Grains fortemnt mouchetés  %:"))
print(gfm)


#Grains boutés   %

gb= float(input("Grains bouté  %:"))
print(gb)
if gb<=4:
    print("sans bonification ni réfaction")
else: print("refaction")
vgb = 0.00

if gb>=4.01 and gb<=5:

    vgb = -0.05
    print(vgb)
elif gb>=5.01 and gb<=6:
       vgb = -0.15
       print(vgb)
elif gb>=6.01 and gb<=7:
       vgb = -0.25
       print(vgb)
else:
    vgb = 0
    print(vgb)
#Grains punaisés  %
gp = float(input("Grains punaisés  %:"))
print(gp)
#Grains piqués  %
gpq = float(input("Grains piqués  %:"))
print(gpq)
#total de 2éme catégori
t2 = gcs+gm+gech+geb+groux+gfm+gb+gp+gpq
print(t2)
if t2<=10:
    print("sans bonification ni réfaction")
else: print("refaction")
vt2 = 0.00
if t2>=10.01 and t2<=10.25:
    vt2= -0.075
    print(vt2)
elif t2>=10.26 and t2<=10.5:
    vt2 =-0.15
    print(vt2)
elif t2>=10.51 and t2<=10.75:
    vt2 = -0.225
    print(vt2)
elif t2>=10.76 and t2<=11:
    vt2 = -0.3
    print(vt2)
elif t2>=11.01 and t2<=11.25:
    vt2 = -0.375
    print(vt2)
elif t2>=11.26 and t2<=11.5:
    vt2 = -0.45
    print(vt2)
elif t2>=11.51 and t2<=11.75:
    vt2 = -0.525
    print(vt2)
elif t2>=11.76 and t2<=12:
    vt2 = -0.6
    print(vt2)
elif t2>=12.01 and t2<=12.25:
    vt2 = -0.675
    print(vt2)
elif t2>=12.26 and t2<=12.5:
    vt2 = -0.75
    print(vt2)
elif t2>=12.51 and t2<=12.75:
    vt2 = -0.825
    print(vt2)
elif t2>=12.76 and t2<=13:
    vt2 = -0.9
    print(vt2)

elif t2>=13.01 and t2<=13.25:
    vt2 = -0.975
    print(vt2)

elif t2>=13.26 and t2<=13.5:
    vt2 = -1.05
    print(vt2)
elif t2>=13.51 and t2<=13.75:
    vt2 = -1.125
    print(vt2)

elif t2>=13.76 and t2<=14:
    vt2 = -1.2
    print(vt2)
elif t2 >= 14.01 and t2 <= 14.25:
    vt2 = -1.275
    print(vt2)

elif t2>=14.26 and t2<=14.5:
    vt2 = -1.35
    print(vt2)
elif t2 >= 14.51 and t2 <= 14.75:
    vt2 = -1.425
    print(vt2)
elif t2>=14.76 and t2<=15:
    vt2 = -1.5
    print(vt2)

elif t2>=15.01 and t2<=15.25:
    vt2 = -1.6
    print(vt2)

elif t2>=15.26 and t2<=14.5:
    vt2 = -1.7
    print(vt2)

elif t2>=15.51 and t2<=15.75:
    vt2 = -1.8
    print(vt2)
elif t2>=15.76 and t2<=16:
    vt2 = -1.9
    print(vt2)
else:
    vt2 = 0
    print(vt2)
vtotale = vgcs + vt2 + vgb
#Graines mitadinès
#indice notin (mitadinès)
inm = float(input("indice notin (mitadinès):"))
print (inm)
#Blé Tendre dans Blé Dur   %
blt = float(input("Blé Tendre dans Blé Dur   %:"))
print(blt)
if blt<=5 and blt>2.5:
    print("réfaction")
elif blt<2.5:
    print("Classé comme Graines mitadinès ")
elif blt>5:
    print("Prix a dépattre ")
vblt =0.00
if blt>=2.51 and blt<=2.75:
    vblt = -0.025
    print(vblt)
elif blt>=2.76 and blt<=3:
    vblt = -0.05
    print(vblt)

elif blt>=3.01 and blt<=3.25:
    vblt = -0.75
    print(vblt)
elif blt>=3.26 and blt<=3.5:
    vblt = -0.1
    print(vblt)
elif blt>=3.51 and blt<=3.75:
    vblt = -0.125
    print(vblt)
elif blt>=3.76 and blt<=4:
    vblt = -0.15
    print(vblt)

elif blt>=4.01 and blt<=4.25:
    vblt = -0.175
    print(vblt)
elif blt>=4.26 and blt<=4.5:
    vblt = -0.05
    print(vblt)
elif blt>=4.51 and blt<=4.75:
    vblt = -0.05
    print(vblt)
elif blt>=4.76 and blt<=5:
    vblt = -0.05
    print(vblt)
elif blt>5:
    vblt = 0
    print("Prix a dépattre ")
elif blt<2.5:
    vblt = 0
    print("Classé comme Graines mitadinès ")
#total des Graines mitadinès
t3 = blt + inm
print(t3)
if t3<=12 and t3>=11.1:
    print("sans bonification ni réfaction")
elif t3<=11:
    print("bonificatione")
elif t3>12:
    print("réfaction")


vt3 = 0.00
if t3<=11 and t3>=10.01:
    vt3 = +0.13
    print(vt3)
elif t3 <= 10 and t3>=9.01:
    vt3 = +0.195
    print(vt3)

elif t3<=9 and t3>=0:
    vt3 = +0.26
    print(vt3)

elif t3<= 13 and t3>= 12.01:
    vt3 = -0.065
    print(vt3)

elif t3<=14 and t3>=13.01:
    vt3 = -0.14
    print(vt3)

elif t3 <= 15 and t3 >= 14.01:
    vt3 = -0.225
    print(vt3)

elif t3 <= 16 and t3 >= 15.01:
    vt3 = -0.32
    print(vt3)
elif t3 <= 17 and t3 >= 16.01:
     vt3 = -0.425
     print(vt3)

elif t3 <= 18 and t3 >= 17.01:
     vt3 = -0.555
     print(vt3)

elif t3 <= 19 and t3 >= 18.01:
     vt3 = -0.675
     print(vt3)

elif t3 <= 20 and t3 >= 19.01:
      vt3 = -0.825
      print(vt3)

elif t3 <= 21 and t3 >= 20.01:
     vt3 = -0.975
     print(vt3)

elif t3 <= 22 and t3 >= 21.01:
     vt3 = -1.15
     print(vt3)

elif t3 <= 23 and t3 >= 22.01:
     vt3 = -1.325
     print(vt3)
elif t3 <= 24 and t3 >= 23.01:
     vt3 = -1.525
     print(vt3)
elif t3 <= 25 and t3 >= 24.01:
     vt3 = -1.7
     print(vt3)
elif t3 <= 26 and t3 >= 25.01:
     vt3 = -1.9
     print(vt3)

elif t3 <= 27 and t3 >= 26.01:
     vt3 = -2.1
     print(vt3)
elif t3 <= 28 and t3 >= 27.01:
     vt3 = -2.3
     print(vt3)
elif t3 <= 29 and t3 >= 28.01:
     vt3 = -2.5
     print(vt3)

elif t3 <= 30 and t3 >= 29.01:
     vt3 = -2.75
     print(vt3)

elif t3 <= 31 and t3 >= 30.01:
    vt3 = -3
    print(vt3)

elif t3 <= 32 and t3 >= 31.01:
    vt3 = -3.25
    print(vt3)

elif t3 <= 33 and t3 >= 32.01:
   vt3 = -3.5
   print(vt3)

elif t3 <= 34 and t3 >= 33.01:
   vt3 = -3.75
   print(vt3)

elif t3 <= 2.51 and t3 >= 2.75:
   vt3 = -0.025
   print(vt3)

elif t3 <= 2.76 and t3 >= 3:
   vt3 = -0.075
   print(vt3)

elif t3 <= 3.25 and t3 >= 3.01:
   vt3 = -0.1
   print(vt3)

elif t3 <= 3.26 and t3 >= 3.5:
   vt3 = -0.1
   print(vt3)

elif t3 <= 3.51 and t3 >= 3.75:
   vt3 = -0.125
   print(vt3)
elif t3 <= 3.76 and t3 >= 4:
   vt3 = -0.15
   print(vt3)






vtotale3 = vt3 + vblt
print("totale grain métadiné",vtotale3)




prix_1q = float(input("Le prix de vente/q:"))
print(prix_1q)

prix_final = poids * prix_1q
print("le prix final de récolte", prix_final)

totale_DA = vps + vgn + vt1 + vtotale + vtotale3
print("Total: (DA) 1q ", totale_DA)

t_br = totale_DA * poids
print("total(bonification/rèfaction)(DA):", t_br)
