def set_poid():
    poid = float(input("la Quantité de recolte (q):"))
    return poid


def set_poid_specific():
    ps = float(input("Poid spécifique kg/hl:"))
    if ps == 78:
        observation = "sans bonification ni réfaction"
    elif ps > 78:
        observation = "bonification"
    elif 74 < ps < 78:
        observation = "refaction"
    elif ps < 74:
        observation = "refuser"

    return ps, observation


def set_humidite():
    humidite = float(input("Humidité %:"))
    if humidite <= 17:
        observation = "accpter"
    else:
        observation = "refuser"
    return humidite


def set_grain_nuisibles():
    gn = float(input("Grains nuisibles  %:"))
    if 0.25 >= gn > 0.05:
        observation = "refaction"
    elif gn <= 0.05:
        obesrvation = "accepter"
    else:
        observation = "refuse"
    return gn, obesrvation


def set_ergot():
    ergot = float(input("ergot  %:"))
    print(ergot)
    # observation
    print("observation")
    if ergot < 0.001:
        observation = "accepter"
    else:
        observation = "refuse"

    return ergot, observation


def set_debris_vegetaux():
    debris_vegetaux = float(input("les débris végétaux  %:"))
    return debris_vegetaux


def set_matiere_inertes():
    mi = float(input("matiérs inertes  %:"))
    return mi


def set_grains_sons_valour():
    gsv = float(input("grains sons valours  %:"))
    return gsv


def set_grains_caries():
    gcr = float(input("grains cariés  %:"))
    return gcr


def set_grains_casse():
    gcs = float(input("Grains cassés  %:"))
    if gcs <= 3:
        observation = "sans bonification ni réfaction"
    else:
        observation = "réfaction"
    return gcs, observation


def set_grains_maigres():
    gm = float(input("Grains maigres  %:"))
    return gm


def set_grains_echaudes():
    gech = float(input("Grains échaudés  %:"))
    return gech


def set_grains_etranders():
    geb = float(input("Grains etranders utilisable pour le bétail  %:"))
    return geb


def set_grains_roux():
    groux = float(input("Grains de blé dur roux  %:"))
    return groux


def set_grains_mouchetes():
    gfm = float(input("Grains fortemnt mouchetés  %:"))
    return gfm


def set_grain_boute():
    gb = float(input("Grains bouté  %:"))
    if gb <= 4:
        observation = "sans bonification ni réfaction"
    else:
        observation = "refaction"
    return gb, observation


def set_grain_punaises():
    gp = float(input("Grains punaisés  %:"))
    return gp


def set_grains_piques():
    gpq = float(input("Grains piqués  %:"))
    return gpq


def set_indice_notin():
    inm = float(input("indice notin (mitadinès):"))
    return inm


def set_ble_tendre():
    blt = float(input("Blé Tendre dans Blé Dur   %:"))
    if 5 >= blt > 2.5:
        observation = "réfaction"
    elif blt < 2.5:
        observation = "Classé comme Graines mitadinès "
    elif blt > 5:
        observation = "Prix a dépattre "

    return blt, observation


def bonification(ps, gn, dv, mi, gsv, gcr, gcs, gm, gech, geb, groux, gfm, gb, gp, gpq, inm, blt):
    total_premier_category = dv + mi + gsv + gcr
    total_dexieum_category = gm + gech + geb + groux + gfm + gcs + gb + gp + gpq
    total_metadines = inm + blt
    total_value = 0.00
    if 77.99 >= ps >= 77.75:
        vps = -0.25
        print(vps)
    elif 77.749 >= ps >= 77.5:
        vps = -0.5
        print(vps)
    elif 77.499 >= ps >= 77.25:
        vps = -0.75
        print(vps)
    elif 77.249 >= ps >= 77:
        vps = -1
        print(vps)
    elif 76.99 >= ps >= 76.75:
        vps = -1.35
        print(vps)
    elif 76.749 >= ps >= 76.5:
        vps = -1.7
        print(vps)
    elif 76.499 >= ps >= 76.25:
        vps = -2.05
        print(vps)
    elif 76.249 >= ps >= 76:
        vps = -2.4
        print(vps)
    elif 75.999 >= ps >= 75.75:
        vps = -2.9
        print(vps)
    elif 75.749 >= ps >= 75.5:
        vps = -3.4
        print(vps)
    elif 75.499 >= ps >= 75.25:
        vps = -3.9
        print(vps)
    elif 75.249 >= ps >= 75:
        vps = -4.4
        print(vps)
    elif 74.999 >= ps >= 74.75:
        vps = -4.9
        print(vps)
    elif 74.749 >= ps >= 74.5:
        vps = -5.4
        print(vps)
    elif 74.999 >= ps >= 74.25:
        vps = -5.9
        print(vps)
    elif 74.249 >= ps >= 74:
        vps = -6.4
        print(vps)
    elif 78.001 <= ps <= 78.25:
        vps = +0.15
        print(vps)
    elif 78.251 <= ps <= 78.5:
        vps = +0.3
        print(vps)
    elif 78.501 <= ps <= 78.75:
        vps = +0.45
        print(vps)
    elif 78.751 <= ps <= 79:
        vps = +0.6
        print(vps)
    elif 79.001 <= ps <= 79.25:
        vps = +0.75
        print(vps)
    elif 79.251 <= ps <= 79.5:
        vps = +0.9
        print(vps)
    elif 79.501 <= ps <= 79.75:
        vps = +1.05
        print(vps)
    elif 79.751 <= ps <= 80:
        vps = +1.20
        print(vps)
    elif 80.001 <= ps <= 80.25:
        vps = +1.35
        print(vps)
    elif 80.251 <= ps <= 80.5:
        vps = +1.5
        print(vps)
    elif 80.501 <= ps <= 80.75:
        vps = +1.65
        print(vps)
    elif 80.751 <= ps <= 81:
        vps = +1.80
        print(vps)
    elif 81.001 <= ps <= 81.25:
        vps = +1.95
        print(vps)
    elif 81.251 <= ps <= 81.5:
        vps = +2.1
        print(vps)
    elif 81.501 <= ps <= 81.75:
        vps = +2.25
        print(vps)
    elif 81.751 <= ps <= 82:
        vps = +2.4
        print(vps)
    elif 82.001 <= ps <= 82.25:
        vps = +2.5
        print(vps)
    elif 82.251 <= ps <= 82.5:
        vps = +2.6
        print(vps)
    elif 82.501 <= ps <= 82.75:
        vps = +2.7
        print(vps)
    elif 82.751 <= ps <= 83:
        vps = +2.8
        print(vps)
    elif 83.001 <= ps <= 83.25:
        vps = +2.85
        print(vps)
    elif 83.251 <= ps <= 83.5:
        vps = +2.9
        print(vps)
    elif 83.5 <= ps <= 83.75:
        vps = +2.95
        print(vps)
    elif 83.751 <= ps <= 84:
        vps = +3
        print(vps)
    elif 84.001 <= ps <= 84.25:
        vps = +3.05
        print(vps)
    elif 84.251 <= ps <= 84.5:
        vps = +3.1
        print(vps)
    elif 84.501 <= ps <= 84.75:
        vps = +3.15
        print(vps)
    elif 84.751 <= ps <= 85:
        vps = +3.2
        print(vps)
    elif 85.001 <= ps <= 85.25:
        vps = +3.25
        print(vps)
    elif 85.251 <= ps <= 85.5:
        vps = +3.3
        print(vps)
    elif 85.501 <= ps <= 85.75:
        vps = +3.35
        print(vps)
    elif ps > 85.75:
        vps = +3.35

    if 0.051 <= gn <= 0.1:
        vgn = -0.05
        print(vgn)
    elif 0.101 <= gn <= 0.15:
        vgn = -0.1
        print(vgn)
    elif 0.151 <= gn <= 0.2:
        vgn = -0.15
        print(vgn)
    elif 0.201 <= gn <= 0.25:
        vgn = -0.2
        print(vgn)
    if 0.999 >= total_premier_category >= 0.75:
        vt1 = +0.15
        print(vt1)
    elif 0.749 >= total_premier_category >= 0.5:
        vt1 = +0.3
        print(vt1)
    elif 0.499 >= total_premier_category >= 0.25:
        vt1 = +0.45
        print(vt1)
    elif 0.249 >= total_premier_category >= 0:
        vt1 = +0.6
        print(vt1)
    elif 1.01 <= total_premier_category <= 1.25:
        vt1 = -0.15
        print(vt1)
    elif 1.26 <= total_premier_category <= 1.5:
        vt1 = -0.3
        print(vt1)
    elif 1.51 <= total_premier_category <= 1.75:
        vt1 = -0.45
        print(vt1)
    elif 1.76 <= total_premier_category <= 2:
        vt1 = -0.6
        print(vt1)
    elif 2.01 <= total_premier_category <= 2.25:
        vt1 = -0.75
        print(vt1)
    elif 2.26 <= total_premier_category <= 2.5:
        vt1 = -0.9
        print(vt1)
    elif 2.51 <= total_premier_category <= 2.75:
        vt1 = -1.05
        print(vt1)
    elif 2.76 <= total_premier_category <= 3:
        vt1 = -1.2

    if 3.01 <= gcs <= 3.25:
        vgcs = -0.05
        print(vgcs)
    elif 3.26 <= gcs <= 3.5:
        vgcs = -0.1
        print(vgcs)
    elif 3.51 <= gcs <= 3.75:
        vgcs = -0.15
        print(vgcs)
    elif 3.76 <= gcs <= 4:
        vgcs = -0.2
        print(vgcs)
    elif 4.01 <= gcs <= 4.25:
        vgcs = -0.25
        print()
    elif 4.26 <= gcs <= 4.5:
        vgcs = -0.3
        print(vgcs)
    elif 4.51 <= gcs <= 4.75:
        vgcs = -0.35
        print(vgcs)
    elif 4.76 <= gcs <= 5:
        vgcs = -0.4
        print(vgcs)
    elif 5.01 <= gcs <= 5.25:
        vgcs = -0.475
        print(vgcs)
    elif 5.26 <= gcs <= 5.5:
        vgcs = -0.55
        print(vgcs)
    elif 5.51 <= gcs <= 5.75:
        vgcs = -0.625
        print(vgcs)
    elif 5.76 <= gcs <= 6:
        vgcs = -0.7
        print(vgcs)
    elif 6.01 <= gcs <= 6.25:
        vgcs = -0.775
        print(vgcs)
    elif 6.26 <= gcs <= 6.5:
        vgcs = -0.850
        print(vgcs)
    elif 6.51 <= gcs <= 6.75:
        vgcs = -0, 925
        print(vgcs)
    elif 6.76 <= gcs <= 7:
        vgcs = -1.0
        print(vgcs)
    elif 7.01 <= gcs <= 7.25:
        vgcs = -1.075
        print(vgcs)
    elif 7.26 <= gcs <= 7.5:
        vgcs = -1.15
        print(vgcs)
    elif 7.51 <= gcs <= 7.75:
        vgcs = -1.225
        print(vgcs)
    elif 7.76 <= gcs <= 8:
        vgcs: -1.3
        print(vgcs)

    if 4.01 <= gb <= 5:
        vgb = -0.05
        print(vgb)
    elif 5.01 <= gb <= 6:
        vgb = -0.15
        print(vgb)
    elif 6.01 <= gb <= 7:
        vgb = -0.25
        print(vgb)
    else:
        vgb = 0

    if 10.01 <= total_dexieum_category <= 10.25:
        vt2 = -0.075
        print(vt2)
    elif 10.26 <= total_dexieum_category <= 10.5:
        vt2 = -0.15
        print(vt2)
    elif 10.51 <= total_dexieum_category <= 10.75:
        vt2 = -0.225
        print(vt2)
    elif 10.76 <= total_dexieum_category <= 11:
        vt2 = -0.3
        print(vt2)
    elif 11.01 <= total_dexieum_category <= 11.25:
        vt2 = -0.375
        print(vt2)
    elif 11.26 <= total_dexieum_category <= 11.5:
        vt2 = -0.45
        print(vt2)
    elif 11.51 <= total_dexieum_category <= 11.75:
        vt2 = -0.525
        print(vt2)
    elif 11.76 <= total_dexieum_category <= 12:
        vt2 = -0.6
        print(vt2)
    elif 12.01 <= total_dexieum_category <= 12.25:
        vt2 = -0.675
        print(vt2)
    elif 12.26 <= total_dexieum_category <= 12.5:
        vt2 = -0.75
        print(vt2)
    elif 12.51 <= total_dexieum_category <= 12.75:
        vt2 = -0.825
        print(vt2)
    elif 12.76 <= total_dexieum_category <= 13:
        vt2 = -0.9
        print(vt2)

    elif 13.01 <= total_dexieum_category <= 13.25:
        vt2 = -0.975
        print(vt2)

    elif 13.26 <= total_dexieum_category <= 13.5:
        vt2 = -1.05
        print(vt2)
    elif 13.51 <= total_dexieum_category <= 13.75:
        vt2 = -1.125
        print(vt2)

    elif 13.76 <= total_dexieum_category <= 14:
        vt2 = -1.2
        print(vt2)
    elif 14.01 <= total_dexieum_category <= 14.25:
        vt2 = -1.275
        print(vt2)

    elif 14.26 <= total_dexieum_category <= 14.5:
        vt2 = -1.35
        print(vt2)
    elif 14.51 <= total_dexieum_category <= 14.75:
        vt2 = -1.425
        print(vt2)
    elif 14.76 <= total_dexieum_category <= 15:
        vt2 = -1.5
        print(vt2)

    elif 15.01 <= total_dexieum_category <= 15.25:
        vt2 = -1.6
        print(vt2)

    elif 15.26 <= total_dexieum_category <= 14.5:
        vt2 = -1.7
        print(vt2)

    elif 15.51 <= total_dexieum_category <= 15.75:
        vt2 = -1.8
        print(vt2)
    elif 15.76 <= total_dexieum_category <= 16:
        vt2 = -1.9
        print(vt2)
    else:
        vt2 = 0

    if 2.51 <= blt <= 2.75:
        vblt = -0.025
        print(vblt)
    elif 2.76 <= blt <= 3:
        vblt = -0.05
        print(vblt)

    elif 3.01 <= blt <= 3.25:
        vblt = -0.75
        print(vblt)
    elif 3.26 <= blt <= 3.5:
        vblt = -0.1
        print(vblt)
    elif 3.51 <= blt <= 3.75:
        vblt = -0.125
        print(vblt)
    elif 3.76 <= blt <= 4:
        vblt = -0.15
        print(vblt)

    elif 4.01 <= blt <= 4.25:
        vblt = -0.175
        print(vblt)
    elif 4.26 <= blt <= 4.5:
        vblt = -0.05
        print(vblt)
    elif 4.51 <= blt <= 4.75:
        vblt = -0.05
        print(vblt)
    elif 4.76 <= blt <= 5:
        vblt = -0.05
        print(vblt)
    elif blt > 5:
        vblt = 0
        print("Prix a dépattre ")
    elif blt < 2.5:
        vblt = 0

    if 11 >= total_metadines >= 10.01:
        vt3 = +0.13
        print(vt3)
    elif 10 >= total_metadines >= 9.01:
        vt3 = +0.195
        print(vt3)

    elif 9 >= total_metadines >= 0:
        vt3 = +0.26
        print(vt3)

    elif 13 >= total_metadines >= 12.01:
        vt3 = -0.065
        print(vt3)

    elif 14 >= total_metadines >= 13.01:
        vt3 = -0.14
        print(vt3)

    elif 15 >= total_metadines >= 14.01:
        vt3 = -0.225
        print(vt3)

    elif 16 >= total_metadines >= 15.01:
        vt3 = -0.32
        print(vt3)
    elif 17 >= total_metadines >= 16.01:
        vt3 = -0.425
        print(vt3)

    elif 18 >= total_metadines >= 17.01:
        vt3 = -0.555
        print(vt3)

    elif 19 >= total_metadines >= 18.01:
        vt3 = -0.675
        print(vt3)

    elif 20 >= total_metadines >= 19.01:
        vt3 = -0.825
        print(vt3)

    elif 21 >= total_metadines >= 20.01:
        vt3 = -0.975
        print(vt3)

    elif 22 >= total_metadines >= 21.01:
        vt3 = -1.15
        print(vt3)

    elif 23 >= total_metadines >= 22.01:
        vt3 = -1.325
        print(vt3)
    elif 24 >= total_metadines >= 23.01:
        vt3 = -1.525
        print(vt3)
    elif 25 >= total_metadines >= 24.01:
        vt3 = -1.7
        print(vt3)
    elif 26 >= total_metadines >= 25.01:
        vt3 = -1.9
        print(vt3)

    elif 27 >= total_metadines >= 26.01:
        vt3 = -2.1
        print(vt3)
    elif 28 >= total_metadines >= 27.01:
        vt3 = -2.3
        print(vt3)
    elif 29 >= total_metadines >= 28.01:
        vt3 = -2.5
        print(vt3)

    elif 30 >= total_metadines >= 29.01:
        vt3 = -2.75
        print(vt3)

    elif 31 >= total_metadines >= 30.01:
        vt3 = -3
        print(vt3)

    elif 32 >= total_metadines >= 31.01:
        vt3 = -3.25
        print(vt3)

    elif 33 >= total_metadines >= 32.01:
        vt3 = -3.5
        print(vt3)

    elif 34 >= total_metadines >= 33.01:
        vt3 = -3.75
        print(vt3)

    elif 2.51 >= total_metadines >= 2.75:
        vt3 = -0.025
        print(vt3)

    elif 2.76 >= total_metadines >= 3:
        vt3 = -0.075
        print(vt3)

    elif 3.25 >= total_metadines >= 3.01:
        vt3 = -0.1
        print(vt3)

    elif 3.26 >= total_metadines >= 3.5:
        vt3 = -0.1
        print(vt3)

    elif 3.51 >= total_metadines >= 3.75:
        vt3 = -0.125
        print(vt3)
    elif 3.76 >= total_metadines >= 4:
        vt3 = -0.15
        print(vt3)

    total_value = vps + vgn + vt1 + vgcs + vt2 + vgb + vblt + vt3
    return total_value, vps, vgn, vt1, vgcs, vt2, vt3, vblt, vgb


ps = set_poid_specific()
gn = set_grain_nuisibles()
dv = set_debris_vegetaux()
mi = set_matiere_inertes()
gsv = set_grains_sons_valour()
gcr = set_grains_caries()
gcs = set_grains_casse()
gm = set_grains_maigres()
gech = set_grains_echaudes()
geb = set_grains_etranders()
groux = set_grains_roux()
gfm = set_grains_mouchetes()
gb = set_grain_boute()
gp = set_grain_punaises()
gpq = set_grains_piques()
inm = set_indice_notin()
blt = set_ble_tendre()

total_value, vps, vgn, vt1, vgcs, vt2, vt3, vblt, vgb = bonification(ps, gn, dv, mi, gsv, gcr, gcs, gm, gech, geb,
                                                                     groux, gfm, gb, gp, gpq, inm, blt)
print("bonification total ", total_value)
print("bonification 1er category ", vt1)
print("bonification 2eme category ", vt2)
print("bonification grain metadine ", vt3)
print("bonification poids specific ", vps)
print("bonification grain nuisible ", vgn)
print("bonification grain cassé ", vgcs)
print("bonification ble tendre ", vblt)
print("bonification grain boute ", vgb)


