def set_poid():
    poid = float(input("la Quantité de recolte (q):"))
    return poid


def set_poid_specific():
    poid_specifique = float(input("Poid spécifique kg/hl:"))
    if poid_specifique == 78:
        observation = "sans bonification ni réfaction"
    elif poid_specifique > 78:
        observation = "bonification"
    elif 74 < poid_specifique < 78:
        observation = "refaction"
    elif poid_specifique < 74:
        observation = "refuser"

    return poid_specifique


def set_humidite():
    humidite = float(input("Humidité %:"))
    if humidite <= 17:
        observation = "accpter"
    else:
        observation = "refuser"
    return humidite


def set_grain_nuisibles():
    grains_nuisible = float(input("Grains nuisibles  %:"))
    if 0.25 >= grains_nuisible > 0.05:
        observation = "refaction"
    elif grains_nuisible <= 0.05:
        obesrvation = "accepter"
    else:
        observation = "refuse"
    return grains_nuisible


def set_ergot():
    ergot = float(input("ergot  %:"))
    print(ergot)
    # observation
    print("observation")
    if ergot < 0.001:
        observation = "accepter"
    else:
        observation = "refuse"

    return ergot


def set_debris_vegetaux():
    debris_vegetaux = float(input("les débris végétaux  %:"))
    return debris_vegetaux


def set_matiere_inertes():
    matiers_inertes = float(input("matiérs inertes  %:"))
    return matiers_inertes


def set_grains_sons_valour():
    grains_sons_valours = float(input("grains sons valours  %:"))
    return grains_sons_valours


def set_grains_caries():
    grains_caries = float(input("grains cariés  %:"))
    return grains_caries


def set_grains_casse():
    grains_casse = float(input("Grains cassés  %:"))
    if grains_casse <= 3:
        observation = "sans bonification ni réfaction"
    else:
        observation = "réfaction"
    return grains_casse


def set_grains_maigres():
    grains_maigres = float(input("Grains maigres  %:"))
    return grains_maigres


def set_grains_echaudes():
    grains_echaudes = float(input("Grains échaudés  %:"))
    return grains_echaudes


def set_grains_etranders():
    grains_etrander = float(input("Grains etranders utilisable pour le bétail  %:"))
    return grains_etrander


def set_grains_roux():
    grains_de_ble_dur_roux = float(input("Grains de blé dur roux  %:"))
    return grains_de_ble_dur_roux


def set_grains_mouchetes():
    grains_mouchetes = float(input("Grains fortemnt mouchetés  %:"))
    return grains_mouchetes


def set_grain_boute():
    grain_boute = float(input("Grains bouté  %:"))
    if grain_boute <= 4:
        observation = "sans bonification ni réfaction"
    else:
        observation = "refaction"
    return grain_boute


def set_grain_punaises():
    grain_punaise = float(input("Grains punaisés  %:"))
    return grain_punaise


def set_grains_piques():
    grains_pique = float(input("Grains piqués  %:"))
    return grains_pique


def set_indice_notin():
    indice_notin = float(input("indice notin (mitadinès):"))
    return indice_notin


def set_ble_tendre():
    ble_tendre_dans_ble_dur = float(input("Blé Tendre dans Blé Dur   %:"))

    return ble_tendre_dans_ble_dur

def observation_(poid_specifique, humidite,grains_nuisible,ergot, grains_casse, grain_boute, ble_tendre_dans_ble_dur):
    total_premier_category = debris_vegetaux + matiers_inertes + grains_sons_valours + grains_caries
    total_dexieum_category = grains_maigres + grains_echaudes + grains_etrander + grains_de_ble_dur_roux + grains_mouchetes + grains_casse + grain_boute + grain_punaise + grains_pique
    total_metadines = indice_notin + ble_tendre_dans_ble_dur
    if poid_specifique == 78:
        obsrvation_poid_sprcifique = "sans bonification ni réfaction"
    elif poid_specifique > 78:
        obsrvation_poid_sprcifique = "bonification"
    elif 74 < poid_specifique < 78:
        obsrvation_poid_sprcifique = " refaction"
    elif poid_specifique< 74:
        obsrvation_poid_sprcifique = "refuser"
    else:obsrvation_poid_sprcifique = "-"

    if humidite <= 17:
        obsrvation_humidite ="accepter"
    else:
        obsrvation_humidite ="refuser"

    if 0.25 >= grains_nuisible > 0.05:
        obsrvation_grains_nuisible = "refaction"
    elif grains_nuisible <= 0.05:
        obsrvation_grains_nuisible ="accepter"
    else:
        obsrvation_grains_nuisible ="refuse"

    if ergot < 0.001:
        obsrvation_ergot = "accepter"
    else:
        obsrvation_ergot ="refuser"

    if total_premier_category <= 1:
        obsrvation_total_premier_category = "sans bonification ni réfaction"
    else:
        obsrvation_total_premier_category = "réfaction"

    if grains_casse <= 3:
        obsrvation_grains_casse =  "sans bonification ni réfaction"
    else:
        obsrvation_grains_casse ="réfaction"

    if grain_boute <= 4:
        obsrvation_grain_boute = "sans bonification ni réfaction"
    else:
        obsrvation_grain_boute = "refaction"


    if total_dexieum_category <= 10:
        obsrvation_total_dexieum_category = "sans bonification ni réfaction"
    else:
        obsrvation_total_dexieum_category ="refaction"

    if 5 >= ble_tendre_dans_ble_dur > 2.5:
        obsrvation_ble_tendre_dans_ble_dur = "réfaction"
    elif ble_tendre_dans_ble_dur < 2.5:
         obsrvation_ble_tendre_dans_ble_dur = "Classé comme Graines mitadinès "
    elif ble_tendre_dans_ble_dur > 5:
        obsrvation_ble_tendre_dans_ble_dur ="Prix a dépattre "
    else: obsrvation_ble_tendre_dans_ble_dur = "-"

    if 12 >= total_metadines>= 11.1:
        obsrvation_total_metadines ="sans bonification ni réfaction"
    elif total_metadines <= 11:
        obsrvation_total_metadines = "bonificatione"
    elif total_metadines > 12:
        obsrvation_total_metadines = "réfaction"
    else:obsrvation_total_metadines = "-"

    return obsrvation_poid_sprcifique, obsrvation_humidite, obsrvation_grains_nuisible, obsrvation_ergot, \
           obsrvation_total_premier_category , obsrvation_grains_casse, obsrvation_grain_boute,\
           obsrvation_total_dexieum_category , obsrvation_ble_tendre_dans_ble_dur, obsrvation_total_metadines






def bonification(poid_specifique, grains_nuisible, debris_vegetaux, matiers_inertes, grains_sons_valours, grains_caries, grains_casse,
                 grains_maigres, grains_echaudes, grains_etrander, grains_de_ble_dur_roux, grains_mouchetes, grain_boute, grain_punaise,
                 grains_pique, ble_tendre_dans_ble_dur):
    total_premier_category = debris_vegetaux + matiers_inertes + grains_sons_valours + grains_caries
    total_dexieum_category = grains_maigres + grains_echaudes + grains_etrander + grains_de_ble_dur_roux + grains_mouchetes + grains_casse + grain_boute + grain_punaise + grains_pique
    total_metadines = indice_notin + ble_tendre_dans_ble_dur
    total_value = 0.00
    if 77.99 >= poid_specifique >= 77.75:
        valeur_poid_specifique = -0.25
        print(valeur_poid_specifique)
    elif 77.749 >= poid_specifique >= 77.5:
        valeur_poid_specifique = -0.5
        print(valeur_poid_specifique)
    elif 77.499 >= poid_specifique >= 77.25:
        valeur_poid_specifique = -0.75
        print(valeur_poid_specifique)
    elif 77.249 >= poid_specifique >= 77:
        valeur_poid_specifique = -1
        print(valeur_poid_specifique)
    elif 76.99 >= poid_specifique >= 76.75:
        valeur_poid_specifique = -1.35
        print(valeur_poid_specifique)
    elif 76.749 >= poid_specifique >= 76.5:
        valeur_poid_specifique = -1.7
        print(valeur_poid_specifique)
    elif 76.499 >= poid_specifique >= 76.25:
        valeur_poid_specifique = -2.05
        print(valeur_poid_specifique)
    elif 76.249 >= poid_specifique >= 76:
        valeur_poid_specifique = -2.4
        print(valeur_poid_specifique)
    elif 75.999 >= poid_specifique >= 75.75:
        valeur_poid_specifique = -2.9
        print(valeur_poid_specifique)
    elif 75.749 >= poid_specifique >= 75.5:
        valeur_poid_specifique = -3.4
        print(valeur_poid_specifique)
    elif 75.499 >= poid_specifique >= 75.25:
        valeur_poid_specifique = -3.9
        print(valeur_poid_specifique)
    elif 75.249 >= poid_specifique >= 75:
        valeur_poid_specifique = -4.4
        print(valeur_poid_specifique)
    elif 74.999 >= poid_specifique >= 74.75:
        valeur_poid_specifique = -4.9
        print(valeur_poid_specifique)
    elif 74.749 >= poid_specifique >= 74.5:
        valeur_poid_specifique = -5.4
        print(valeur_poid_specifique)
    elif 74.999 >= poid_specifique >= 74.25:
        valeur_poid_specifique = -5.9
        print(valeur_poid_specifique)
    elif 74.249 >= poid_specifique >= 74:
        valeur_poid_specifique = -6.4
        print(valeur_poid_specifique)
    elif 78.001 <= poid_specifique <= 78.25:
        valeur_poid_specifique = +0.15
        print(valeur_poid_specifique)
    elif 78.251 <= poid_specifique <= 78.5:
        valeur_poid_specifique = +0.3
        print(valeur_poid_specifique)
    elif 78.501 <= poid_specifique <= 78.75:
        valeur_poid_specifique = +0.45
        print(valeur_poid_specifique)
    elif 78.751 <= poid_specifique <= 79:
        valeur_poid_specifique = +0.6
        print(valeur_poid_specifique)
    elif 79.001 <= poid_specifique <= 79.25:
        valeur_poid_specifique = +0.75
        print(valeur_poid_specifique)
    elif 79.251 <= poid_specifique <= 79.5:
        valeur_poid_specifique = +0.9
        print(valeur_poid_specifique)
    elif 79.501 <= poid_specifique <= 79.75:
        valeur_poid_specifique = +1.05
        print(valeur_poid_specifique)
    elif 79.751 <= poid_specifique <= 80:
        valeur_poid_specifique = +1.20
        print(valeur_poid_specifique)
    elif 80.001 <= poid_specifique <= 80.25:
        valeur_poid_specifique = +1.35
        print(valeur_poid_specifique)
    elif 80.251 <= poid_specifique <= 80.5:
        valeur_poid_specifique = +1.5
        print(valeur_poid_specifique)
    elif 80.501 <= poid_specifique <= 80.75:
        valeur_poid_specifique = +1.65
        print(valeur_poid_specifique)
    elif 80.751 <= poid_specifique <= 81:
        valeur_poid_specifique = +1.80
        print(valeur_poid_specifique)
    elif 81.001 <= poid_specifique <= 81.25:
        valeur_poid_specifique = +1.95
        print(valeur_poid_specifique)
    elif 81.251 <= poid_specifique <= 81.5:
        valeur_poid_specifique = +2.1
        print(valeur_poid_specifique)
    elif 81.501 <= poid_specifique <= 81.75:
        valeur_poid_specifique = +2.25
        print(valeur_poid_specifique)
    elif 81.751 <= poid_specifique <= 82:
        valeur_poid_specifique = +2.4
        print(valeur_poid_specifique)
    elif 82.001 <= poid_specifique <= 82.25:
        valeur_poid_specifique = +2.5
        print(valeur_poid_specifique)
    elif 82.251 <= poid_specifique <= 82.5:
        valeur_poid_specifique = +2.6
        print(valeur_poid_specifique)
    elif 82.501 <= poid_specifique <= 82.75:
        valeur_poid_specifique = +2.7
        print(valeur_poid_specifique)
    elif 82.751 <= poid_specifique <= 83:
        valeur_poid_specifique = +2.8
        print(valeur_poid_specifique)
    elif 83.001 <= poid_specifique <= 83.25:
        valeur_poid_specifique = +2.85
        print(valeur_poid_specifique)
    elif 83.251 <= poid_specifique <= 83.5:
        valeur_poid_specifique = +2.9
        print(valeur_poid_specifique)
    elif 83.5 <= poid_specifique <= 83.75:
        valeur_poid_specifique = +2.95
        print(valeur_poid_specifique)
    elif 83.751 <= poid_specifique <= 84:
        valeur_poid_specifique = +3
        print(valeur_poid_specifique)
    elif 84.001 <= poid_specifique <= 84.25:
        valeur_poid_specifique = +3.05
        print(valeur_poid_specifique)
    elif 84.251 <= poid_specifique <= 84.5:
        valeur_poid_specifique = +3.1
        print(valeur_poid_specifique)
    elif 84.501 <= poid_specifique <= 84.75:
        valeur_poid_specifique = +3.15
        print(valeur_poid_specifique)
    elif 84.751 <= poid_specifique <= 85:
        valeur_poid_specifique = +3.2
        print(valeur_poid_specifique)
    elif 85.001 <= poid_specifique <= 85.25:
        valeur_poid_specifique = +3.25
        print(valeur_poid_specifique)
    elif 85.251 <= poid_specifique <= 85.5:
        valeur_poid_specifique = +3.3
        print(valeur_poid_specifique)
    elif 85.501 <= poid_specifique <= 85.75:
        valeur_poid_specifique = +3.35
        print(valeur_poid_specifique)
    elif poid_specifique > 85.75:
        valeur_poid_specifique = +3.35
    else:
        valeur_poid_specifique = 0.00

    if 0.051 <= grains_nuisible <= 0.1:
        bon_ref_grains_nuisible = -0.05
        print(bon_ref_grains_nuisible)
    elif 0.101 <= grains_nuisible <= 0.15:
        bon_ref_grains_nuisible = -0.1
        print(bon_ref_grains_nuisible)
    elif 0.151 <= grains_nuisible <= 0.2:
        bon_ref_grains_nuisible = -0.15
        print(bon_ref_grains_nuisible)
    elif 0.201 <= grains_nuisible <= 0.25:
        bon_ref_grains_nuisible = -0.2
        print(bon_ref_grains_nuisible)
    else:
        bon_ref_grains_nuisible = 0.00

    if 0.999 >= total_premier_category >= 0.75:
        bon_ref_total_premier_category = +0.15
        print(bon_ref_total_premier_category)
    elif 0.749 >= total_premier_category >= 0.5:
        bon_ref_total_premier_category = +0.3
        print(bon_ref_total_premier_category)
    elif 0.499 >= total_premier_category >= 0.25:
        bon_ref_total_premier_category = +0.45
        print(bon_ref_total_premier_category)
    elif 0.249 >= total_premier_category >= 0:
        bon_ref_total_premier_category = +0.6
        print(bon_ref_total_premier_category)
    elif 1.01 <= total_premier_category <= 1.25:
        bon_ref_total_premier_category = -0.15
        print(bon_ref_total_premier_category)
    elif 1.26 <= total_premier_category <= 1.5:
        bon_ref_total_premier_category = -0.3
        print(bon_ref_total_premier_category)
    elif 1.51 <= total_premier_category <= 1.75:
        bon_ref_total_premier_category = -0.45
        print(bon_ref_total_premier_category)
    elif 1.76 <= total_premier_category <= 2:
        bon_ref_total_premier_category = -0.6
        print(bon_ref_total_premier_category)
    elif 2.01 <= total_premier_category <= 2.25:
        bon_ref_total_premier_category = -0.75
        print(bon_ref_total_premier_category)
    elif 2.26 <= total_premier_category <= 2.5:
        bon_ref_total_premier_category = -0.9
        print(bon_ref_total_premier_category)
    elif 2.51 <= total_premier_category <= 2.75:
        bon_ref_total_premier_category = -1.05
        print(bon_ref_total_premier_category)
    elif 2.76 <= total_premier_category <= 3:
        bon_ref_total_premier_category = -1.2
    else:
        bon_ref_total_premier_category = 0

    if 3.01 <= grains_casse <= 3.25:
        bon_ref_grains_casse = -0.05
        print(bon_ref_grains_casse)
    elif 3.26 <= grains_casse <= 3.5:
        bon_ref_grains_casse = -0.1
        print(bon_ref_grains_casse)
    elif 3.51 <= grains_casse <= 3.75:
        bon_ref_grains_casse = -0.15
        print(bon_ref_grains_casse)
    elif 3.76 <= grains_casse <= 4:
        bon_ref_grains_casse = -0.2
        print(bon_ref_grains_casse)
    elif 4.01 <= grains_casse <= 4.25:
        bon_ref_grains_casse = -0.25
        print()
    elif 4.26 <= grains_casse <= 4.5:
        bon_ref_grains_casse = -0.3
        print(bon_ref_grains_casse)
    elif 4.51 <= grains_casse <= 4.75:
        bon_ref_grains_casse = -0.35
        print(bon_ref_grains_casse)
    elif 4.76 <= grains_casse <= 5:
        bon_ref_grains_casse = -0.4
        print(bon_ref_grains_casse)
    elif 5.01 <= grains_casse <= 5.25:
        bon_ref_grains_casse = -0.475
        print(bon_ref_grains_casse)
    elif 5.26 <= grains_casse <= 5.5:
        bon_ref_grains_casse = -0.55
        print(bon_ref_grains_casse)
    elif 5.51 <= grains_casse <= 5.75:
        bon_ref_grains_casse = -0.625
        print(bon_ref_grains_casse)
    elif 5.76 <= grains_casse <= 6:
        bon_ref_grains_casse = -0.7
        print(bon_ref_grains_casse)
    elif 6.01 <= grains_casse <= 6.25:
        bon_ref_grains_casse = -0.775
        print(bon_ref_grains_casse)
    elif 6.26 <= grains_casse <= 6.5:
        bon_ref_grains_casse = -0.850
        print(bon_ref_grains_casse)
    elif 6.51 <= grains_casse <= 6.75:
        bon_ref_grains_casse = -0, 925
        print(bon_ref_grains_casse)
    elif 6.76 <= grains_casse <= 7:
        bon_ref_grains_casse = -1.0
        print(bon_ref_grains_casse)
    elif 7.01 <= grains_casse <= 7.25:
        bon_ref_grains_casse = -1.075
        print(bon_ref_grains_casse)
    elif 7.26 <= grains_casse <= 7.5:
        bon_ref_grains_casse = -1.15
        print(bon_ref_grains_casse)
    elif 7.51 <= grains_casse <= 7.75:
        bon_ref_grains_casse = -1.225
        print(bon_ref_grains_casse)
    elif 7.76 <= grains_casse <= 8:
        bon_ref_grains_casse: -1.3
        print(bon_ref_grains_casse)
    else :
        bon_ref_grains_casse = 0.00

    if 4.01 <= grain_boute <= 5:
        bon_ref_grain_boute = -0.05
        print(bon_ref_grain_boute)
    elif 5.01 <= grain_boute <= 6:
        bon_ref_grain_boute = -0.15
        print(bon_ref_grain_boute)
    elif 6.01 <= grain_boute <= 7:
        bon_ref_grain_boute = -0.25
        print(bon_ref_grain_boute)
    else:
        bon_ref_grain_boute = 0

    if 10.01 <= total_dexieum_category <= 10.25:
        bon_ref_total_dexieum_category = -0.075
        print(bon_ref_total_dexieum_category)
    elif 10.26 <= total_dexieum_category <= 10.5:
        bon_ref_total_dexieum_category = -0.15
        print(bon_ref_total_dexieum_category)
    elif 10.51 <= total_dexieum_category <= 10.75:
        bon_ref_total_dexieum_category = -0.225
        print(bon_ref_total_dexieum_category)
    elif 10.76 <= total_dexieum_category <= 11:
        bon_ref_total_dexieum_category = -0.3
        print(bon_ref_total_dexieum_category)
    elif 11.01 <= total_dexieum_category <= 11.25:
        bon_ref_total_dexieum_category = -0.375
        print(bon_ref_total_dexieum_category)
    elif 11.26 <= total_dexieum_category <= 11.5:
        bon_ref_total_dexieum_category = -0.45
        print(bon_ref_total_dexieum_category)
    elif 11.51 <= total_dexieum_category <= 11.75:
        bon_ref_total_dexieum_category = -0.525
        print(bon_ref_total_dexieum_category)
    elif 11.76 <= total_dexieum_category <= 12:
        bon_ref_total_dexieum_category = -0.6
        print(bon_ref_total_dexieum_category)
    elif 12.01 <= total_dexieum_category <= 12.25:
        bon_ref_total_dexieum_category = -0.675
        print(bon_ref_total_dexieum_category)
    elif 12.26 <= total_dexieum_category <= 12.5:
        bon_ref_total_dexieum_category = -0.75
        print(bon_ref_total_dexieum_category)
    elif 12.51 <= total_dexieum_category <= 12.75:
        bon_ref_total_dexieum_category = -0.825
        print(bon_ref_total_dexieum_category)
    elif 12.76 <= total_dexieum_category <= 13:
        bon_ref_total_dexieum_category = -0.9
        print(bon_ref_total_dexieum_category)

    elif 13.01 <= total_dexieum_category <= 13.25:
        bon_ref_total_dexieum_category = -0.975
        print(bon_ref_total_dexieum_category)

    elif 13.26 <= total_dexieum_category <= 13.5:
        bon_ref_total_dexieum_category = -1.05
        print(bon_ref_total_dexieum_category)
    elif 13.51 <= total_dexieum_category <= 13.75:
        bon_ref_total_dexieum_category = -1.125
        print(bon_ref_total_dexieum_category)

    elif 13.76 <= total_dexieum_category <= 14:
        bon_ref_total_dexieum_category = -1.2
        print(bon_ref_total_dexieum_category)
    elif 14.01 <= total_dexieum_category <= 14.25:
        bon_ref_total_dexieum_category = -1.275
        print(bon_ref_total_dexieum_category)

    elif 14.26 <= total_dexieum_category <= 14.5:
        bon_ref_total_dexieum_category = -1.35
        print(bon_ref_total_dexieum_category)
    elif 14.51 <= total_dexieum_category <= 14.75:
        bon_ref_total_dexieum_category = -1.425
        print(bon_ref_total_dexieum_category)
    elif 14.76 <= total_dexieum_category <= 15:
        bon_ref_total_dexieum_category = -1.5
        print(bon_ref_total_dexieum_category)

    elif 15.01 <= total_dexieum_category <= 15.25:
        bon_ref_total_dexieum_category = -1.6
        print(bon_ref_total_dexieum_category)

    elif 15.26 <= total_dexieum_category <= 14.5:
        bon_ref_total_dexieum_category = -1.7
        print(bon_ref_total_dexieum_category)

    elif 15.51 <= total_dexieum_category <= 15.75:
        bon_ref_total_dexieum_category = -1.8
        print(bon_ref_total_dexieum_category)
    elif 15.76 <= total_dexieum_category <= 16:
        bon_ref_total_dexieum_category = -1.9
        print(bon_ref_total_dexieum_category)
    else:
        bon_ref_total_dexieum_category = 0

    if 2.51 <= ble_tendre_dans_ble_dur <= 2.75:
        bon_ref_ble_tendre_dans_ble_dur = -0.025
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 2.76 <= ble_tendre_dans_ble_dur <= 3:
        bon_ref_ble_tendre_dans_ble_dur = -0.05
        print(bon_ref_ble_tendre_dans_ble_dur)

    elif 3.01 <= ble_tendre_dans_ble_dur <= 3.25:
        bon_ref_ble_tendre_dans_ble_dur = -0.75
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 3.26 <= ble_tendre_dans_ble_dur <= 3.5:
        bon_ref_ble_tendre_dans_ble_dur = -0.1
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 3.51 <= ble_tendre_dans_ble_dur <= 3.75:
        bon_ref_ble_tendre_dans_ble_dur = -0.125
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 3.76 <= ble_tendre_dans_ble_dur <= 4:
        bon_ref_ble_tendre_dans_ble_dur = -0.15
        print(bon_ref_ble_tendre_dans_ble_dur)

    elif 4.01 <= ble_tendre_dans_ble_dur <= 4.25:
        bon_ref_ble_tendre_dans_ble_dur = -0.175
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 4.26 <= ble_tendre_dans_ble_dur <= 4.5:
        bon_ref_ble_tendre_dans_ble_dur = -0.05
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 4.51 <= ble_tendre_dans_ble_dur <= 4.75:
        bon_ref_ble_tendre_dans_ble_dur = -0.05
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif 4.76 <= ble_tendre_dans_ble_dur <= 5:
        bon_ref_ble_tendre_dans_ble_dur = -0.05
        print(bon_ref_ble_tendre_dans_ble_dur)
    elif ble_tendre_dans_ble_dur > 5:
        bon_ref_ble_tendre_dans_ble_dur = 0
        print("Prix a dépattre ")
    elif ble_tendre_dans_ble_dur < 2.5:
        bon_ref_ble_tendre_dans_ble_dur = 0
    else:
        bon_ref_ble_tendre_dans_ble_dur = 0.00

    if 11 >= total_metadines >= 10.01:
        bon_ref_total_metadines = +0.13
        print(bon_ref_total_metadines)
    elif 10 >= total_metadines >= 9.01:
        bon_ref_total_metadines = +0.195
        print(bon_ref_total_metadines)

    elif 9 >= total_metadines >= 0:
        bon_ref_total_metadines = +0.26
        print(bon_ref_total_metadines)

    elif 13 >= total_metadines >= 12.01:
        bon_ref_total_metadines = -0.065
        print(bon_ref_total_metadines)

    elif 14 >= total_metadines >= 13.01:
        bon_ref_total_metadines = -0.14
        print(bon_ref_total_metadines)

    elif 15 >= total_metadines >= 14.01:
        bon_ref_total_metadines = -0.225
        print(bon_ref_total_metadines)

    elif 16 >= total_metadines >= 15.01:
        bon_ref_total_metadines = -0.32
        print(bon_ref_total_metadines)
    elif 17 >= total_metadines >= 16.01:
        bon_ref_total_metadines = -0.425
        print(bon_ref_total_metadines)

    elif 18 >= total_metadines >= 17.01:
        bon_ref_total_metadines = -0.555
        print(bon_ref_total_metadines)

    elif 19 >= total_metadines >= 18.01:
        bon_ref_total_metadines = -0.675
        print(bon_ref_total_metadines)

    elif 20 >= total_metadines >= 19.01:
        bon_ref_total_metadines = -0.825
        print(bon_ref_total_metadines)

    elif 21 >= total_metadines >= 20.01:
        bon_ref_total_metadines = -0.975
        print(bon_ref_total_metadines)

    elif 22 >= total_metadines >= 21.01:
        bon_ref_total_metadines = -1.15
        print(bon_ref_total_metadines)

    elif 23 >= total_metadines >= 22.01:
        bon_ref_total_metadines = -1.325
        print(bon_ref_total_metadines)
    elif 24 >= total_metadines >= 23.01:
        bon_ref_total_metadines = -1.525
        print(bon_ref_total_metadines)
    elif 25 >= total_metadines >= 24.01:
        bon_ref_total_metadines = -1.7
        print(bon_ref_total_metadines)
    elif 26 >= total_metadines >= 25.01:
        bon_ref_total_metadines = -1.9
        print(bon_ref_total_metadines)

    elif 27 >= total_metadines >= 26.01:
        bon_ref_total_metadines = -2.1
        print(bon_ref_total_metadines)
    elif 28 >= total_metadines >= 27.01:
        bon_ref_total_metadines = -2.3
        print(bon_ref_total_metadines)
    elif 29 >= total_metadines >= 28.01:
        bon_ref_total_metadines = -2.5
        print(bon_ref_total_metadines)

    elif 30 >= total_metadines >= 29.01:
        bon_ref_total_metadines = -2.75
        print(bon_ref_total_metadines)

    elif 31 >= total_metadines >= 30.01:
        bon_ref_total_metadines = -3
        print(bon_ref_total_metadines)

    elif 32 >= total_metadines >= 31.01:
        bon_ref_total_metadines = -3.25
        print(bon_ref_total_metadines)

    elif 33 >= total_metadines >= 32.01:
        bon_ref_total_metadines = -3.5
        print(bon_ref_total_metadines)

    elif 34 >= total_metadines >= 33.01:
        bon_ref_total_metadines = -3.75
        print(bon_ref_total_metadines)

    elif 2.51 >= total_metadines >= 2.75:
        bon_ref_total_metadines = -0.025
        print(bon_ref_total_metadines)

    elif 2.76 >= total_metadines >= 3:
        bon_ref_total_metadines = -0.075
        print(bon_ref_total_metadines)

    elif 3.25 >= total_metadines >= 3.01:
        bon_ref_total_metadines = -0.1
        print(bon_ref_total_metadines)

    elif 3.26 >= total_metadines >= 3.5:
        bon_ref_total_metadines = -0.1
        print(bon_ref_total_metadines)

    elif 3.51 >= total_metadines >= 3.75:
        bon_ref_total_metadines = -0.125
        print(bon_ref_total_metadines)
    elif 3.76 >= total_metadines >= 4:
        bon_ref_total_metadines = -0.15
        print(bon_ref_total_metadines)
    else:
        bon_ref_total_metadines = 0.00

    total_value = valeur_poid_specifique + bon_ref_grains_nuisible + bon_ref_total_premier_category + bon_ref_grains_casse + bon_ref_total_dexieum_category + bon_ref_grain_boute + bon_ref_ble_tendre_dans_ble_dur + bon_ref_total_metadines
    return total_value, valeur_poid_specifique, bon_ref_grains_nuisible, bon_ref_total_premier_category, bon_ref_grains_casse, bon_ref_total_dexieum_category, bon_ref_total_metadines, bon_ref_ble_tendre_dans_ble_dur, bon_ref_grain_boute


poid_specifique = set_poid_specific()
humidite = set_humidite()
ergot = set_ergot()
grains_nuisible = set_grain_nuisibles()
debris_vegetaux = set_debris_vegetaux()
matiers_inertes = set_matiere_inertes()
grains_sons_valours = set_grains_sons_valour()
grains_caries = set_grains_caries()
grains_casse = set_grains_casse()
grains_maigres = set_grains_maigres()
grains_echaudes = set_grains_echaudes()
grains_etrander = set_grains_etranders()
grains_de_ble_dur_roux = set_grains_roux()
grains_mouchetes = set_grains_mouchetes()
grain_boute = set_grain_boute()
grain_punaise = set_grain_punaises()
grains_pique = set_grains_piques()
indice_notin = set_indice_notin()
ble_tendre_dans_ble_dur = set_ble_tendre()


obsrvation_poid_sprcifique, obsrvation_humidite, obsrvation_grains_nuisible, obsrvation_ergot, \
           obsrvation_total_premier_category , obsrvation_grains_casse, obsrvation_grain_boute,\
           obsrvation_total_dexieum_category , obsrvation_ble_tendre_dans_ble_dur, obsrvation_total_metadines\
    = observation_(poid_specifique, humidite ,grains_nuisible, ergot, grains_casse, grain_boute, ble_tendre_dans_ble_dur)


total_value, valeur_poid_specifique, bon_ref_grains_nuisible\
    , bon_ref_total_premier_category, bon_ref_grains_casse ,bon_ref_grain_boute,bon_ref_total_dexieum_category\
    , bon_ref_ble_tendre_dans_ble_dur, bon_ref_total_metadines = bonification(poid_specifique, grains_nuisible,
                                                                              debris_vegetaux, matiers_inertes,
                                                                              grains_sons_valours, grains_caries,
                                                                              grains_casse, grains_maigres,
                                                                              grains_echaudes, grains_etrander,
                                                                              grains_de_ble_dur_roux, grains_mouchetes
                                                                              , grain_boute, grain_punaise, grains_pique
                                                                              , indice_notin, ble_tendre_dans_ble_dur)




print("observastion poids specific",obsrvation_poid_sprcifique)
print("observastion poids specific",obsrvation_humidite)
print("observastion poids specific",obsrvation_grains_nuisible)
print("observastion poids specific",obsrvation_ergot)
print("observastion poids specific",obsrvation_total_premier_category)
print("observastion poids specific",obsrvation_grains_casse)
print("observastion poids specific",obsrvation_grain_boute)
print("observastion poids specific",obsrvation_total_dexieum_category)
print("observastion poids specific",obsrvation_ble_tendre_dans_ble_dur)
print("observastion poids specific",obsrvation_total_metadines)





print("bonification poids specific ", valeur_poid_specifique)
print("bonification grain nuisible ", bon_ref_grains_nuisible)
print("bonification 1er category ", bon_ref_total_premier_category)

print("bonification grain cassé ", bon_ref_grains_casse)
print("bonification grain boute ", bon_ref_grain_boute)
print("bonification 2eme category ", bon_ref_total_dexieum_category)

print("bonification ble tendre ", bon_ref_ble_tendre_dans_ble_dur)
print("bonification grain metadine ", bon_ref_total_metadines)

print("bonification total ", total_value)

