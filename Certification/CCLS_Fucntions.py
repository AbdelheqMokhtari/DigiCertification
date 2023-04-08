def set_poid():
    poid = float(input("la Quantité de recolte (q):"))
    return poid


def set_price():
    price = float(input("Le prix de vente/q: "))


def set_poid_specifique():
    p_specifique = float(input("Poid spécifique kg/hl:"))
    if p_specifique == 78:
        observation = "sans bonification ni réfaction"
    elif p_specifique > 78:
        observation = "bonification"
    elif 74 < p_specifique < 78:
        observation = "refaction"
    elif p_specifique < 74:
        observation = "refuser"

    return p_specifique


def set_humidite():
    humidite = float(input("Humidité %:"))
    if humidite <= 17:
        observation = "accpter"
    else:
        observation = "refuser"
    return humidite


def set_grain_nuisibles():
    g_nuisibles = float(input("Grains nuisibles  %:"))
    if 0.25 >= g_nuisibles > 0.05:
        observation = "refaction"
    elif g_nuisibles <= 0.05:
        observation = "accepter"
    else:
        observation = "refuse"
    return g_nuisibles


def set_ergot():
    ergot = float(input("ergot  %:"))
    if ergot < 0.001:
        observation = "accepter"
    else:
        observation = "refuse"

    return ergot


def set_debris_vegetaux():
    debris_vegetaux = float(input("les débris végétaux  %:"))
    return debris_vegetaux


def set_matiere_inertes():
    matiers_ineretes = float(input("matiérs inertes  %:"))
    return matiers_ineretes


def set_grains_sans_valeur():
    sans_valeur = float(input("grains sans valeur  %:"))
    return sans_valeur


def set_grains_caries():
    g_caries = float(input("grains cariés  %:"))
    return g_caries


def set_grains_casse():
    g_casse = float(input("Grains cassés  %:"))
    if g_casse <= 3:
        observation = "sans bonification ni réfaction"
    else:
        observation = "réfaction"
    return g_casse


def set_grains_maigres():
    g_maigres = float(input("Grains maigres  %:"))
    return g_maigres


def set_grains_echaudes():
    g_echaudes = float(input("Grains échaudés  %:"))
    return g_echaudes


def set_grains_etranders():
    g_etranders = float(input("Grains etranders utilisable pour le bétail  %:"))
    return g_etranders


def set_grains_roux():
    g_roux = float(input("Grains de blé dur roux  %:"))
    return g_roux


def set_grains_mouchetes():
    g_mouchetes = float(input("Grains fortemnt mouchetés  %:"))
    return g_mouchetes


def set_grain_boute():
    g_boute = float(input("Grains bouté  %:"))
    if g_boute <= 4:
        observation = "sans bonification ni réfaction"
    else:
        observation = "refaction"
    return g_boute


def set_grain_punaises():
    g_punaises = float(input("Grains punaisés  %:"))
    return g_punaises


def set_grains_piques():
    g_piques = float(input("Grains piqués  %:"))
    return g_piques


def set_indice_notin():
    indice_notin = float(input("indice notin (mitadinès):"))
    return indice_notin


def set_ble_tendre():
    ble_tendre = float(input("Blé Tendre dans Blé Dur   %:"))
    if 5 >= ble_tendre > 2.5:
        observation = "réfaction"
    elif ble_tendre < 2.5:
        observation = "Classé comme Graines mitadinès "
    elif ble_tendre > 5:
        observation = "Prix a dépattre "

    return ble_tendre


def bonification(p_specifique, nuisibles, debris_vegetaux, matiers_ineretes, sans_valeur, g_caries, g_casse, g_maigres,
                 g_echaudes, g_etranders, g_roux, g_mouchetes, g_boute, g_punaises, g_piques, indice_notin, ble_tendre):
    total_premier_category = debris_vegetaux + matiers_ineretes + sans_valeur + g_caries
    total_dexieum_category = g_maigres + g_echaudes + g_etranders + g_roux + g_mouchetes + g_casse + g_boute + \
                             g_punaises + g_piques
    total_metadines = indice_notin + ble_tendre

    if 77.99 >= p_specifique >= 77.75:
        bon_p_specifique = -0.25
        print(bon_p_specifique)
    elif 77.749 >= p_specifique >= 77.5:
        bon_p_specifique = -0.5
        print(bon_p_specifique)
    elif 77.499 >= p_specifique >= 77.25:
        bon_p_specifique = -0.75
        print(bon_p_specifique)
    elif 77.249 >= p_specifique >= 77:
        bon_p_specifique = -1
        print(bon_p_specifique)
    elif 76.99 >= p_specifique >= 76.75:
        bon_p_specifique = -1.35
        print(bon_p_specifique)
    elif 76.749 >= p_specifique >= 76.5:
        bon_p_specifique = -1.7
        print(bon_p_specifique)
    elif 76.499 >= p_specifique >= 76.25:
        bon_p_specifique = -2.05
        print(bon_p_specifique)
    elif 76.249 >= p_specifique >= 76:
        bon_p_specifique = -2.4
        print(bon_p_specifique)
    elif 75.999 >= p_specifique >= 75.75:
        bon_p_specifique = -2.9
        print(bon_p_specifique)
    elif 75.749 >= p_specifique >= 75.5:
        bon_p_specifique = -3.4
        print(bon_p_specifique)
    elif 75.499 >= p_specifique >= 75.25:
        bon_p_specifique = -3.9
        print(bon_p_specifique)
    elif 75.249 >= p_specifique >= 75:
        bon_p_specifique = -4.4
        print(bon_p_specifique)
    elif 74.999 >= p_specifique >= 74.75:
        bon_p_specifique = -4.9
        print(bon_p_specifique)
    elif 74.749 >= p_specifique >= 74.5:
        bon_p_specifique = -5.4
        print(bon_p_specifique)
    elif 74.999 >= p_specifique >= 74.25:
        bon_p_specifique = -5.9
        print(bon_p_specifique)
    elif 74.249 >= p_specifique >= 74:
        bon_p_specifique = -6.4
        print(bon_p_specifique)
    elif 78.001 <= p_specifique <= 78.25:
        bon_p_specifique = +0.15
        print(bon_p_specifique)
    elif 78.251 <= p_specifique <= 78.5:
        bon_p_specifique = +0.3
        print(bon_p_specifique)
    elif 78.501 <= p_specifique <= 78.75:
        bon_p_specifique = +0.45
        print(bon_p_specifique)
    elif 78.751 <= p_specifique <= 79:
        bon_p_specifique = +0.6
        print(bon_p_specifique)
    elif 79.001 <= p_specifique <= 79.25:
        bon_p_specifique = +0.75
        print(bon_p_specifique)
    elif 79.251 <= p_specifique <= 79.5:
        bon_p_specifique = +0.9
        print(bon_p_specifique)
    elif 79.501 <= p_specifique <= 79.75:
        bon_p_specifique = +1.05
        print(bon_p_specifique)
    elif 79.751 <= p_specifique <= 80:
        bon_p_specifique = +1.20
        print(bon_p_specifique)
    elif 80.001 <= p_specifique <= 80.25:
        bon_p_specifique = +1.35
        print(bon_p_specifique)
    elif 80.251 <= p_specifique <= 80.5:
        bon_p_specifique = +1.5
        print(bon_p_specifique)
    elif 80.501 <= p_specifique <= 80.75:
        bon_p_specifique = +1.65
        print(bon_p_specifique)
    elif 80.751 <= p_specifique <= 81:
        bon_p_specifique = +1.80
        print(bon_p_specifique)
    elif 81.001 <= p_specifique <= 81.25:
        bon_p_specifique = +1.95
        print(bon_p_specifique)
    elif 81.251 <= p_specifique <= 81.5:
        bon_p_specifique = +2.1
        print(bon_p_specifique)
    elif 81.501 <= p_specifique <= 81.75:
        bon_p_specifique = +2.25
        print(bon_p_specifique)
    elif 81.751 <= p_specifique <= 82:
        bon_p_specifique = +2.4
        print(bon_p_specifique)
    elif 82.001 <= p_specifique <= 82.25:
        bon_p_specifique = +2.5
        print(bon_p_specifique)
    elif 82.251 <= p_specifique <= 82.5:
        bon_p_specifique = +2.6
        print(bon_p_specifique)
    elif 82.501 <= p_specifique <= 82.75:
        bon_p_specifique = +2.7
        print(bon_p_specifique)
    elif 82.751 <= p_specifique <= 83:
        bon_p_specifique = +2.8
        print(bon_p_specifique)
    elif 83.001 <= p_specifique <= 83.25:
        bon_p_specifique = +2.85
        print(bon_p_specifique)
    elif 83.251 <= p_specifique <= 83.5:
        bon_p_specifique = +2.9
        print(bon_p_specifique)
    elif 83.5 <= p_specifique <= 83.75:
        bon_p_specifique = +2.95
        print(bon_p_specifique)
    elif 83.751 <= p_specifique <= 84:
        bon_p_specifique = +3
        print(bon_p_specifique)
    elif 84.001 <= p_specifique <= 84.25:
        bon_p_specifique = +3.05
        print(bon_p_specifique)
    elif 84.251 <= p_specifique <= 84.5:
        bon_p_specifique = +3.1
        print(bon_p_specifique)
    elif 84.501 <= p_specifique <= 84.75:
        bon_p_specifique = +3.15
        print(bon_p_specifique)
    elif 84.751 <= p_specifique <= 85:
        bon_p_specifique = +3.2
        print(bon_p_specifique)
    elif 85.001 <= p_specifique <= 85.25:
        bon_p_specifique = +3.25
        print(bon_p_specifique)
    elif 85.251 <= p_specifique <= 85.5:
        bon_p_specifique = +3.3
        print(bon_p_specifique)
    elif 85.501 <= p_specifique <= 85.75:
        bon_p_specifique = +3.35
        print(bon_p_specifique)
    elif p_specifique > 85.75:
        bon_p_specifique = +3.35
    else:
        bon_p_specifique = 0.00

    if 0.051 <= nuisibles <= 0.1:
        bon_g_nuisibles = -0.05
        print(bon_g_nuisibles)
    elif 0.101 <= nuisibles <= 0.15:
        bon_g_nuisibles = -0.1
        print(bon_g_nuisibles)
    elif 0.151 <= nuisibles <= 0.2:
        bon_g_nuisibles = -0.15
        print(bon_g_nuisibles)
    elif 0.201 <= nuisibles <= 0.25:
        bon_g_nuisibles = -0.2
        print(bon_g_nuisibles)
    else:
        bon_g_nuisibles = 0.00

    if 0.999 >= total_premier_category >= 0.75:
        bon_premier_category = +0.15
        print(bon_premier_category)
    elif 0.749 >= total_premier_category >= 0.5:
        bon_premier_category = +0.3
        print(bon_premier_category)
    elif 0.499 >= total_premier_category >= 0.25:
        bon_premier_category = +0.45
        print(bon_premier_category)
    elif 0.249 >= total_premier_category >= 0:
        bon_premier_category = +0.6
        print(bon_premier_category)
    elif 1.01 <= total_premier_category <= 1.25:
        bon_premier_category = -0.15
        print(bon_premier_category)
    elif 1.26 <= total_premier_category <= 1.5:
        bon_premier_category = -0.3
        print(bon_premier_category)
    elif 1.51 <= total_premier_category <= 1.75:
        bon_premier_category = -0.45
        print(bon_premier_category)
    elif 1.76 <= total_premier_category <= 2:
        bon_premier_category = -0.6
        print(bon_premier_category)
    elif 2.01 <= total_premier_category <= 2.25:
        bon_premier_category = -0.75
        print(bon_premier_category)
    elif 2.26 <= total_premier_category <= 2.5:
        bon_premier_category = -0.9
        print(bon_premier_category)
    elif 2.51 <= total_premier_category <= 2.75:
        bon_premier_category = -1.05
        print(bon_premier_category)
    elif 2.76 <= total_premier_category <= 3:
        bon_premier_category = -1.2
    else:
        bon_premier_category = 0

    if 3.01 <= g_casse <= 3.25:
        bon_casse = -0.05
        print(bon_casse)
    elif 3.26 <= g_casse <= 3.5:
        bon_casse = -0.1
        print(bon_casse)
    elif 3.51 <= g_casse <= 3.75:
        bon_casse = -0.15
        print(bon_casse)
    elif 3.76 <= g_casse <= 4:
        bon_casse = -0.2
        print(bon_casse)
    elif 4.01 <= g_casse <= 4.25:
        bon_casse = -0.25
        print()
    elif 4.26 <= g_casse <= 4.5:
        bon_casse = -0.3
        print(bon_casse)
    elif 4.51 <= g_casse <= 4.75:
        bon_casse = -0.35
        print(bon_casse)
    elif 4.76 <= g_casse <= 5:
        bon_casse = -0.4
        print(bon_casse)
    elif 5.01 <= g_casse <= 5.25:
        bon_casse = -0.475
        print(bon_casse)
    elif 5.26 <= g_casse <= 5.5:
        bon_casse = -0.55
        print(bon_casse)
    elif 5.51 <= g_casse <= 5.75:
        bon_casse = -0.625
        print(bon_casse)
    elif 5.76 <= g_casse <= 6:
        bon_casse = -0.7
        print(bon_casse)
    elif 6.01 <= g_casse <= 6.25:
        bon_casse = -0.775
        print(bon_casse)
    elif 6.26 <= g_casse <= 6.5:
        bon_casse = -0.850
        print(bon_casse)
    elif 6.51 <= g_casse <= 6.75:
        bon_casse = -0, 925
        print(bon_casse)
    elif 6.76 <= g_casse <= 7:
        bon_casse = -1.0
        print(bon_casse)
    elif 7.01 <= g_casse <= 7.25:
        bon_casse = -1.075
        print(bon_casse)
    elif 7.26 <= g_casse <= 7.5:
        bon_casse = -1.15
        print(bon_casse)
    elif 7.51 <= g_casse <= 7.75:
        bon_casse = -1.225
        print(bon_casse)
    elif 7.76 <= g_casse <= 8:
        bon_casse: -1.3
        print(bon_casse)
    else:
        bon_casse = 0.00

    if 4.01 <= g_boute <= 5:
        bon_boute = -0.05
        print(bon_boute)
    elif 5.01 <= g_boute <= 6:
        bon_boute = -0.15
        print(bon_boute)
    elif 6.01 <= g_boute <= 7:
        bon_boute = -0.25
        print(bon_boute)
    else:
        bon_boute = 0

    if 10.01 <= total_dexieum_category <= 10.25:
        bon_dexieum_category = -0.075
        print(bon_dexieum_category)
    elif 10.26 <= total_dexieum_category <= 10.5:
        bon_dexieum_category = -0.15
        print(bon_dexieum_category)
    elif 10.51 <= total_dexieum_category <= 10.75:
        bon_dexieum_category = -0.225
        print(bon_dexieum_category)
    elif 10.76 <= total_dexieum_category <= 11:
        bon_dexieum_category = -0.3
        print(bon_dexieum_category)
    elif 11.01 <= total_dexieum_category <= 11.25:
        bon_dexieum_category = -0.375
        print(bon_dexieum_category)
    elif 11.26 <= total_dexieum_category <= 11.5:
        bon_dexieum_category = -0.45
        print(bon_dexieum_category)
    elif 11.51 <= total_dexieum_category <= 11.75:
        bon_dexieum_category = -0.525
        print(bon_dexieum_category)
    elif 11.76 <= total_dexieum_category <= 12:
        bon_dexieum_category = -0.6
        print(bon_dexieum_category)
    elif 12.01 <= total_dexieum_category <= 12.25:
        bon_dexieum_category = -0.675
        print(bon_dexieum_category)
    elif 12.26 <= total_dexieum_category <= 12.5:
        bon_dexieum_category = -0.75
        print(bon_dexieum_category)
    elif 12.51 <= total_dexieum_category <= 12.75:
        bon_dexieum_category = -0.825
        print(bon_dexieum_category)
    elif 12.76 <= total_dexieum_category <= 13:
        bon_dexieum_category = -0.9
        print(bon_dexieum_category)

    elif 13.01 <= total_dexieum_category <= 13.25:
        bon_dexieum_category = -0.975
        print(bon_dexieum_category)

    elif 13.26 <= total_dexieum_category <= 13.5:
        bon_dexieum_category = -1.05
        print(bon_dexieum_category)
    elif 13.51 <= total_dexieum_category <= 13.75:
        bon_dexieum_category = -1.125
        print(bon_dexieum_category)

    elif 13.76 <= total_dexieum_category <= 14:
        bon_dexieum_category = -1.2
        print(bon_dexieum_category)
    elif 14.01 <= total_dexieum_category <= 14.25:
        bon_dexieum_category = -1.275
        print(bon_dexieum_category)

    elif 14.26 <= total_dexieum_category <= 14.5:
        bon_dexieum_category = -1.35
        print(bon_dexieum_category)
    elif 14.51 <= total_dexieum_category <= 14.75:
        bon_dexieum_category = -1.425
        print(bon_dexieum_category)
    elif 14.76 <= total_dexieum_category <= 15:
        bon_dexieum_category = -1.5
        print(bon_dexieum_category)

    elif 15.01 <= total_dexieum_category <= 15.25:
        bon_dexieum_category = -1.6
        print(bon_dexieum_category)

    elif 15.26 <= total_dexieum_category <= 14.5:
        bon_dexieum_category = -1.7
        print(bon_dexieum_category)

    elif 15.51 <= total_dexieum_category <= 15.75:
        bon_dexieum_category = -1.8
        print(bon_dexieum_category)
    elif 15.76 <= total_dexieum_category <= 16:
        bon_dexieum_category = -1.9
        print(bon_dexieum_category)
    else:
        bon_dexieum_category = 0

    if 2.51 <= ble_tendre <= 2.75:
        bon_ble_tendre = -0.025
        print(bon_ble_tendre)
    elif 2.76 <= ble_tendre <= 3:
        bon_ble_tendre = -0.05
        print(bon_ble_tendre)

    elif 3.01 <= ble_tendre <= 3.25:
        bon_ble_tendre = -0.75
        print(bon_ble_tendre)
    elif 3.26 <= ble_tendre <= 3.5:
        bon_ble_tendre = -0.1
        print(bon_ble_tendre)
    elif 3.51 <= ble_tendre <= 3.75:
        bon_ble_tendre = -0.125
        print(bon_ble_tendre)
    elif 3.76 <= ble_tendre <= 4:
        bon_ble_tendre = -0.15
        print(bon_ble_tendre)

    elif 4.01 <= ble_tendre <= 4.25:
        bon_ble_tendre = -0.175
        print(bon_ble_tendre)
    elif 4.26 <= ble_tendre <= 4.5:
        bon_ble_tendre = -0.05
        print(bon_ble_tendre)
    elif 4.51 <= ble_tendre <= 4.75:
        bon_ble_tendre = -0.05
        print(bon_ble_tendre)
    elif 4.76 <= ble_tendre <= 5:
        bon_ble_tendre = -0.05
        print(bon_ble_tendre)
    elif ble_tendre > 5:
        bon_ble_tendre = 0
        print("Prix a dépattre ")
    elif ble_tendre < 2.5:
        bon_ble_tendre = 0
    else:
        bon_ble_tendre = 0.00

    if 11 >= total_metadines >= 10.01:
        bon_metadines_category = +0.13
        print(bon_metadines_category)
    elif 10 >= total_metadines >= 9.01:
        bon_metadines_category = +0.195
        print(bon_metadines_category)

    elif 9 >= total_metadines >= 0:
        bon_metadines_category = +0.26
        print(bon_metadines_category)

    elif 13 >= total_metadines >= 12.01:
        bon_metadines_category = -0.065
        print(bon_metadines_category)

    elif 14 >= total_metadines >= 13.01:
        bon_metadines_category = -0.14
        print(bon_metadines_category)

    elif 15 >= total_metadines >= 14.01:
        bon_metadines_category = -0.225
        print(bon_metadines_category)

    elif 16 >= total_metadines >= 15.01:
        bon_metadines_category = -0.32
        print(bon_metadines_category)
    elif 17 >= total_metadines >= 16.01:
        bon_metadines_category = -0.425
        print(bon_metadines_category)

    elif 18 >= total_metadines >= 17.01:
        bon_metadines_category = -0.555
        print(bon_metadines_category)

    elif 19 >= total_metadines >= 18.01:
        bon_metadines_category = -0.675
        print(bon_metadines_category)

    elif 20 >= total_metadines >= 19.01:
        bon_metadines_category = -0.825
        print(bon_metadines_category)

    elif 21 >= total_metadines >= 20.01:
        bon_metadines_category = -0.975
        print(bon_metadines_category)

    elif 22 >= total_metadines >= 21.01:
        bon_metadines_category = -1.15
        print(bon_metadines_category)

    elif 23 >= total_metadines >= 22.01:
        bon_metadines_category = -1.325
        print(bon_metadines_category)
    elif 24 >= total_metadines >= 23.01:
        bon_metadines_category = -1.525
        print(bon_metadines_category)
    elif 25 >= total_metadines >= 24.01:
        bon_metadines_category = -1.7
        print(bon_metadines_category)
    elif 26 >= total_metadines >= 25.01:
        bon_metadines_category = -1.9
        print(bon_metadines_category)

    elif 27 >= total_metadines >= 26.01:
        bon_metadines_category = -2.1
        print(bon_metadines_category)
    elif 28 >= total_metadines >= 27.01:
        bon_metadines_category = -2.3
        print(bon_metadines_category)
    elif 29 >= total_metadines >= 28.01:
        bon_metadines_category = -2.5
        print(bon_metadines_category)

    elif 30 >= total_metadines >= 29.01:
        bon_metadines_category = -2.75
        print(bon_metadines_category)

    elif 31 >= total_metadines >= 30.01:
        bon_metadines_category = -3
        print(bon_metadines_category)

    elif 32 >= total_metadines >= 31.01:
        bon_metadines_category = -3.25
        print(bon_metadines_category)

    elif 33 >= total_metadines >= 32.01:
        bon_metadines_category = -3.5
        print(bon_metadines_category)

    elif 34 >= total_metadines >= 33.01:
        bon_metadines_category = -3.75
        print(bon_metadines_category)

    elif 2.51 >= total_metadines >= 2.75:
        bon_metadines_category = -0.025
        print(bon_metadines_category)

    elif 2.76 >= total_metadines >= 3:
        bon_metadines_category = -0.075
        print(bon_metadines_category)

    elif 3.25 >= total_metadines >= 3.01:
        bon_metadines_category = -0.1
        print(bon_metadines_category)

    elif 3.26 >= total_metadines >= 3.5:
        bon_metadines_category = -0.1
        print(bon_metadines_category)

    elif 3.51 >= total_metadines >= 3.75:
        bon_metadines_category = -0.125
        print(bon_metadines_category)
    elif 3.76 >= total_metadines >= 4:
        bon_metadines_category = -0.15
        print(bon_metadines_category)
    else:
        bon_metadines_category = 0.00

    bon_total = bon_p_specifique + bon_g_nuisibles + bon_premier_category + bon_casse + bon_dexieum_category +\
                bon_boute + bon_ble_tendre + bon_metadines_category
    return bon_total, bon_p_specifique, bon_g_nuisibles, bon_premier_category, bon_casse, bon_dexieum_category,\
         bon_ble_tendre, bon_metadines_category, bon_boute


poid_specifique = set_poid_specifique()
humidite = set_humidite()
g_nuisibles = set_grain_nuisibles()
ergot = set_ergot()
debris_vegetaux = set_debris_vegetaux()
matiere_inertes = set_matiere_inertes()
sans_valeur = set_grains_sans_valeur()
g_caries = set_grains_caries()
g_casse = set_grains_casse()
g_maigres = set_grains_maigres()
g_echaudes = set_grains_echaudes()
g_etranders = set_grains_etranders()
g_roux = set_grains_roux()
g_mouchetes = set_grains_mouchetes()
g_boute = set_grain_boute()
g_punaises = set_grain_punaises()
g_piques = set_grains_piques()
indice_notin = set_indice_notin()
ble_tendre = set_ble_tendre()

bon_total, bon_p_specifique, bon_g_nuisibles, bon_premier_category, bon_casse, bon_dexieum_category,\
bon_ble_tendre, bon_metadines_category, bon_boute = bonification(poid_specifique, g_nuisibles, debris_vegetaux,
                                                                     matiere_inertes, sans_valeur, g_caries, g_casse,
                                                                     g_maigres, g_echaudes, g_etranders, g_roux,
                                                                     g_mouchetes, g_boute, g_punaises, g_piques,
                                                                     indice_notin, ble_tendre)

print("bonification poid specifique ", bon_p_specifique)
print("bonification grain nuisible ", bon_g_nuisibles)
print("bonification 1er category ", bon_premier_category)
print("bonification grain cassé ", bon_casse)
print("bonification grain boute ", bon_boute)
print("bonification 2eme category ", bon_dexieum_category)
print("bonification ble tendre ", bon_ble_tendre)
print("bonification grain metadine ", bon_metadines_category)
print("bonification total ", bon_total)








