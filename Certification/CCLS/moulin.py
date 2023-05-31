
def decision(p_specifique, teneur_eau , nuisible , ergot):
    observation_list = []
    if p_specifique == 78:
        observation_list.append("sans bonification ni réfaction")
    elif p_specifique > 78:
        observation_list.append("bonification")
    elif 74 < p_specifique < 78:
        observation_list.append("refaction")
    elif p_specifique < 74:
        observation_list.append("Refuse")
    if teneur_eau<= 17:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    if 0.25 >= nuisible > 0.05:
        observation_list.append("refaction")
    elif nuisible <= 0.05:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    if ergot < 0.001:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    keys = ["Poids specifique", "teneur en eau", "Grain nuisible", "ergot" ]
    my_dict = dict(zip(keys, observation_list))

    if my_dict["Poids specifique"] == "Refuse":
          Decision = "Refuse"
    elif my_dict["teneur en eau"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["Grain nuisible"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["ergot"] == "Refuse":
        Decision = "Refuse"
    else: Decision = "accept"
    return Decision



def decision_prix_debbattre(ble_tendre ):
    observation_list = []

    if 5 >= ble_tendre > 2.5:
        observation_list.append("réfaction")
    elif ble_tendre < 2.5:
        observation_list.append("Classé comme Graines mitadinès ")
    elif ble_tendre > 5:
        observation_list.append("prix a débattre")

    keys = [ "ble tendre"]
    my_dict = dict(zip(keys, observation_list))

    if my_dict["ble tendre"] == "prix a débattre":
         dcs = "prix a débattre"

    else: dcs = "refaction normale"
    return dcs


def set_poid_specifique():
    p_specifique = float(input("Poid spécifique kg/hl:"))
    return p_specifique
def poi_specifique(p_specifique):
    global ob_p_specifique
    if p_specifique == 78:
        ob_p_specifique = "sans bonification ni réfaction"
    elif p_specifique > 78:
        ob_p_specifique = "bonification"
    elif 74 < p_specifique < 78:
         ob_p_specifique = "refaction"
    elif p_specifique < 74:
        ob_p_specifique = "refuser"
    if 77.99 >= p_specifique >= 77.75:
        bon_p_specifique = -0.25
    elif 77.749 >= p_specifique >= 77.5:
        bon_p_specifique = -0.5
    elif 77.499 >= p_specifique >= 77.25:
        bon_p_specifique = -0.75
    elif 77.249 >= p_specifique >= 77:
        bon_p_specifique = -1
    elif 76.99 >= p_specifique >= 76.75:
        bon_p_specifique = -1.35
    elif 76.749 >= p_specifique >= 76.5:
        bon_p_specifique = -1.7
    elif 76.499 >= p_specifique >= 76.25:
        bon_p_specifique = -2.05
    elif 76.249 >= p_specifique >= 76:
        bon_p_specifique = -2.4
    elif 75.999 >= p_specifique >= 75.75:
        bon_p_specifique = -2.9
    elif 75.749 >= p_specifique >= 75.5:
        bon_p_specifique = -3.4
    elif 75.499 >= p_specifique >= 75.25:
        bon_p_specifique = -3.9
    elif 75.249 >= p_specifique >= 75:
        bon_p_specifique = -4.4
    elif 74.999 >= p_specifique >= 74.75:
        bon_p_specifique = -4.9

    elif 74.749 >= p_specifique >= 74.5:
        bon_p_specifique = -5.4
    elif 74.999 >= p_specifique >= 74.25:
        bon_p_specifique = -5.9
    elif 74.249 >= p_specifique >= 74:
        bon_p_specifique = -6.4
    elif 78.001 <= p_specifique <= 78.25:
        bon_p_specifique = +0.15
    elif 78.251 <= p_specifique <= 78.5:
        bon_p_specifique = +0.3
    elif 78.501 <= p_specifique <= 78.75:
        bon_p_specifique = +0.45
    elif 78.751 <= p_specifique <= 79:
        bon_p_specifique = +0.6
    elif 79.001 <= p_specifique <= 79.25:
        bon_p_specifique = +0.75
    elif 79.251 <= p_specifique <= 79.5:
        bon_p_specifique = +0.9
    elif 79.501 <= p_specifique <= 79.75:
        bon_p_specifique = +1.05
    elif 79.751 <= p_specifique <= 80:
        bon_p_specifique = +1.20
    elif 80.001 <= p_specifique <= 80.25:
        bon_p_specifique = +1.35
    elif 80.251 <= p_specifique <= 80.5:
        bon_p_specifique = +1.5
    elif 80.501 <= p_specifique <= 80.75:
        bon_p_specifique = +1.65
    elif 80.751 <= p_specifique <= 81:
        bon_p_specifique = +1.80
    elif 81.001 <= p_specifique <= 81.25:
        bon_p_specifique = +1.95
    elif 81.251 <= p_specifique <= 81.5:
        bon_p_specifique = +2.1
    elif 81.501 <= p_specifique <= 81.75:
        bon_p_specifique = +2.25
    elif 81.751 <= p_specifique <= 82:
        bon_p_specifique = +2.4
    elif 82.001 <= p_specifique <= 82.25:
        bon_p_specifique = +2.5
    elif 82.251 <= p_specifique <= 82.5:
        bon_p_specifique = +2.6
    elif 82.501 <= p_specifique <= 82.75:
        bon_p_specifique = +2.7
    elif 82.751 <= p_specifique <= 83:
        bon_p_specifique = +2.8
    elif 83.001 <= p_specifique <= 83.25:
        bon_p_specifique = +2.85
    elif 83.251 <= p_specifique <= 83.5:
        bon_p_specifique = +2.9
    elif 83.5 <= p_specifique <= 83.75:
        bon_p_specifique = +2.95
    elif 83.751 <= p_specifique <= 84:
        bon_p_specifique = +3
    elif 84.001 <= p_specifique <= 84.25:
        bon_p_specifique = +3.05
    elif 84.251 <= p_specifique <= 84.5:
        bon_p_specifique = +3.1
    elif 84.501 <= p_specifique <= 84.75:
        bon_p_specifique = +3.15
    elif 84.751 <= p_specifique <= 85:
        bon_p_specifique = +3.2
    elif 85.001 <= p_specifique <= 85.25:
        bon_p_specifique = +3.25
    elif 85.251 <= p_specifique <= 85.5:
        bon_p_specifique = +3.3
    elif 85.501 <= p_specifique <= 85.75:
        bon_p_specifique = +3.35
    elif p_specifique > 85.75:
        bon_p_specifique = +3.35
    else:
        bon_p_specifique = 0.00
    return bon_p_specifique,ob_p_specifique

def set_humidite():
    teneur_eau = float(input("teneur en eau %:"))
    return teneur_eau
def hemuditi(humidite):
    if humidite <= 17:
       ob_humidite= "accepter"
    else:
        ob_humidite= "refuser"
    return ob_humidite
def set_grain_nuisibles():
    g_nuisibles = float(input("Grains nuisibles  %:"))
    return g_nuisibles
def grain_nuisibles(nuisibles):
    if 0.25 >= nuisibles > 0.05:
        ob_g_nuisible ="refaction"
    elif nuisibles <= 0.05:
        ob_g_nuisible ="accepter"
    else:
        ob_g_nuisible ="Refuse"

    if 0.051 <= nuisibles <= 0.1:
        bon_g_nuisibles = -0.05
    elif 0.101 <= nuisibles <= 0.15:
        bon_g_nuisibles = -0.1
    elif 0.151 <= nuisibles <= 0.2:
        bon_g_nuisibles = -0.15
    elif 0.201 <= nuisibles <= 0.25:
        bon_g_nuisibles = -0.2
    else:
        bon_g_nuisibles = 0.00
    return bon_g_nuisibles , ob_g_nuisible

def set_ergot():
    ergot = float(input("ergot  %:"))
    return ergot
def ergo_t(ergot):
    if ergot < 0.001:
        ob_ergot ="accepter"
    else:
        ob_ergot ="refuse"
    return ob_ergot


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
def calcule_totale_1er_category(debris_vegetaux ,matiers_ineretes ,sans_valeur,g_caries):
    total1=debris_vegetaux  +matiers_ineretes+sans_valeur +g_caries
    return total1
def totale_1er_category(total_premier_category):
    if total_premier_category <= 1:
        ob_1er_category = "sans bonification ni réfaction"
    else:
        ob_1er_category = "réfaction"
    if 0.999 >= total_premier_category >= 0.75:
        bon_premier_category = +0.15
    elif 0.749 >= total_premier_category >= 0.5:
        bon_premier_category = +0.3
    elif 0.499 >= total_premier_category >= 0.25:
        bon_premier_category = +0.45
    elif 0.249 >= total_premier_category >= 0:
        bon_premier_category = +0.6
    elif 1.01 <= total_premier_category <= 1.25:
        bon_premier_category = -0.15
    elif 1.26 <= total_premier_category <= 1.5:
        bon_premier_category = -0.3
    elif 1.51 <= total_premier_category <= 1.75:
        bon_premier_category = -0.45
    elif 1.76 <= total_premier_category <= 2:
        bon_premier_category = -0.6
    elif 2.01 <= total_premier_category <= 2.25:
        bon_premier_category = -0.75
    elif 2.26 <= total_premier_category <= 2.5:
        bon_premier_category = -0.9
    elif 2.51 <= total_premier_category <= 2.75:
        bon_premier_category = -1.05
    elif 2.76 <= total_premier_category <= 3:
        bon_premier_category = -1.2
    else:
        bon_premier_category = 0
    return bon_premier_category , ob_1er_category

def set_grains_casse():
    g_casse = float(input("Grains cassés  %:"))
    return g_casse
def grains_casse(g_casse):
    if g_casse <= 3:
        ob_casse = "sans bonification ni réfaction"
    else:
        ob_casse ="réfaction"
    if 3.01 <= g_casse <= 3.25:
        bon_casse = -0.05
    elif 3.26 <= g_casse <= 3.5:
        bon_casse = -0.1
    elif 3.51 <= g_casse <= 3.75:
        bon_casse = -0.15
    elif 3.76 <= g_casse <= 4:
        bon_casse = -0.2
    elif 4.01 <= g_casse <= 4.25:
        bon_casse = -0.25
    elif 4.26 <= g_casse <= 4.5:
        bon_casse = -0.3
    elif 4.51 <= g_casse <= 4.75:
        bon_casse = -0.35
    elif 4.76 <= g_casse <= 5:
        bon_casse = -0.4
    elif 5.01 <= g_casse <= 5.25:
        bon_casse = -0.475
    elif 5.26 <= g_casse <= 5.5:
        bon_casse = -0.55
    elif 5.51 <= g_casse <= 5.75:
        bon_casse = -0.625
    elif 5.76 <= g_casse <= 6:
        bon_casse = -0.7
    elif 6.01 <= g_casse <= 6.25:
        bon_casse = -0.775
    elif 6.26 <= g_casse <= 6.5:
        bon_casse = -0.850
    elif 6.51 <= g_casse <= 6.75:
        bon_casse = -0, 925
    elif 6.76 <= g_casse <= 7:
        bon_casse = -1.0
    elif 7.01 <= g_casse <= 7.25:
        bon_casse = -1.075
    elif 7.26 <= g_casse <= 7.5:
        bon_casse = -1.15
    elif 7.51 <= g_casse <= 7.75:
        bon_casse = -1.225
    elif 7.76 <= g_casse <= 8:
        bon_casse = -1.3
    else:
        bon_casse = 0.00
    return bon_casse, ob_casse
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
    return g_boute
def grain_boute(g_boute):
    if g_boute <= 4:
        ob_boute = "sans bonification ni réfaction"
    else:
        ob_boute = "refaction"
    if 4.01 <= g_boute <= 5:
        bon_boute = -0.05
    elif 5.01 <= g_boute <= 6:
        bon_boute = -0.15
    elif 6.01 <= g_boute <= 7:
        bon_boute = -0.25
    else:
        bon_boute = 0
    return  bon_boute , ob_boute

def set_grain_punaises():
    g_punaises = float(input("Grains punaisés  %:"))
    return g_punaises
def set_grains_piques():
    g_piques = float(input("Grains piqués  %:"))
    return g_piques
def calcule_totale_2eme_category(g_maigres , g_echaudes , g_etranders , g_roux , g_mouchetes , g_casse , g_boute , g_punaises , g_piques):
    total_dexieum_category = g_maigres + g_echaudes + g_etranders + g_roux + g_mouchetes + g_casse + g_boute + g_punaises + g_piques
    return total_dexieum_category
def totale_2eme_category(total_dexieum_category):
    if total_dexieum_category <= 10:
        ob_t_2eme_category ="sans bonification ni réfaction"
    else:
        ob_t_2eme_category ="refaction"
    if 10.01 <= total_dexieum_category <= 10.25:
        bon_dexieum_category = -0.075
    elif 10.26 <= total_dexieum_category <= 10.5:
        bon_dexieum_category = -0.15
    elif 10.51 <= total_dexieum_category <= 10.75:
        bon_dexieum_category = -0.225
    elif 10.76 <= total_dexieum_category <= 11:
        bon_dexieum_category = -0.3
    elif 11.01 <= total_dexieum_category <= 11.25:
        bon_dexieum_category = -0.375

    elif 11.26 <= total_dexieum_category <= 11.5:
        bon_dexieum_category = -0.45
    elif 11.51 <= total_dexieum_category <= 11.75:
        bon_dexieum_category = -0.525
    elif 11.76 <= total_dexieum_category <= 12:
        bon_dexieum_category = -0.6
    elif 12.01 <= total_dexieum_category <= 12.25:
        bon_dexieum_category = -0.675
    elif 12.26 <= total_dexieum_category <= 12.5:
        bon_dexieum_category = -0.75
    elif 12.51 <= total_dexieum_category <= 12.75:
        bon_dexieum_category = -0.825
    elif 12.76 <= total_dexieum_category <= 13:
        bon_dexieum_category = -0.9
    elif 13.01 <= total_dexieum_category <= 13.25:
        bon_dexieum_category = -0.975
    elif 13.26 <= total_dexieum_category <= 13.5:
        bon_dexieum_category = -1.05
    elif 13.51 <= total_dexieum_category <= 13.75:
        bon_dexieum_category = -1.125
    elif 13.76 <= total_dexieum_category <= 14:
        bon_dexieum_category = -1.2
    elif 14.01 <= total_dexieum_category <= 14.25:
        bon_dexieum_category = -1.275
    elif 14.26 <= total_dexieum_category <= 14.5:
        bon_dexieum_category = -1.35
    elif 14.51 <= total_dexieum_category <= 14.75:
        bon_dexieum_category = -1.425
    elif 14.76 <= total_dexieum_category <= 15:
        bon_dexieum_category = -1.5
    elif 15.01 <= total_dexieum_category <= 15.25:
        bon_dexieum_category = -1.6
    elif 15.26 <= total_dexieum_category <= 14.5:
        bon_dexieum_category = -1.7
    elif 15.51 <= total_dexieum_category <= 15.75:
        bon_dexieum_category = -1.8
        print(bon_dexieum_category)
    elif 15.76 <= total_dexieum_category <= 16:
        bon_dexieum_category = -1.9
        print(bon_dexieum_category)
    else:
        bon_dexieum_category = 0
    return bon_dexieum_category , ob_t_2eme_category

    
def set_indice_notin():
    indice_notin = float(input("indice notin (mitadinès):"))
    return indice_notin
def set_ble_tendre():
    ble_tendre = float(input("Blé Tendre dans Blé Dur   %:"))
    return ble_tendre
def ble_tendre_(ble_tendre):
    global ob_ble_tendre
    if 5 >= ble_tendre > 2.5:
       ob_ble_tendre ="réfaction"
    elif ble_tendre < 2.5:
        ob_ble_tendre ="Classé comme Graines mitadinès "
    elif ble_tendre > 5:
        ob_ble_tendre ="Prix a dépattre "
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
    elif ble_tendre < 2.5:
        bon_ble_tendre = 0
    else:
        bon_ble_tendre = 0.00
    return bon_ble_tendre , ob_ble_tendre
def calcul_totale_metadine(indice_notin , ble_tendre):
    total_metadines = indice_notin + ble_tendre
    return total_metadines
def totale_metadine(total_metadines):
    global ob_t_metadine
    if 12 >= total_metadines >= 11.1:
        ob_t_metadine = "sans bonification ni réfaction"
    elif total_metadines <= 11:
        ob_t_metadine = "bonification"
    elif total_metadines > 12:
        ob_t_metadine = "réfaction"
    if 11 >= total_metadines >= 10.01:
        bon_metadines_category = +0.13
    elif 10 >= total_metadines >= 9.01:
        bon_metadines_category = +0.195
    elif 9 >= total_metadines >= 0:
        bon_metadines_category = +0.26
    elif 13 >= total_metadines >= 12.01:
        bon_metadines_category = -0.065
    elif 14 >= total_metadines >= 13.01:
        bon_metadines_category = -0.14
    elif 15 >= total_metadines >= 14.01:
        bon_metadines_category = -0.225
    elif 16 >= total_metadines >= 15.01:
        bon_metadines_category = -0.32
    elif 17 >= total_metadines >= 16.01:
        bon_metadines_category = -0.425
    elif 18 >= total_metadines >= 17.01:
        bon_metadines_category = -0.555
    elif 19 >= total_metadines >= 18.01:
        bon_metadines_category = -0.675
    elif 20 >= total_metadines >= 19.01:
        bon_metadines_category = -0.825
    elif 21 >= total_metadines >= 20.01:
        bon_metadines_category = -0.975
    elif 22 >= total_metadines >= 21.01:
        bon_metadines_category = -1.15
    elif 23 >= total_metadines >= 22.01:
        bon_metadines_category = -1.325
    elif 24 >= total_metadines >= 23.01:
        bon_metadines_category = -1.525
    elif 25 >= total_metadines >= 24.01:
        bon_metadines_category = -1.7
    elif 26 >= total_metadines >= 25.01:
        bon_metadines_category = -1.9
    elif 27 >= total_metadines >= 26.01:
        bon_metadines_category = -2.1
    elif 28 >= total_metadines >= 27.01:
        bon_metadines_category = -2.3
    elif 29 >= total_metadines >= 28.01:
        bon_metadines_category = -2.5
    elif 30 >= total_metadines >= 29.01:
        bon_metadines_category = -2.75
    elif 31 >= total_metadines >= 30.01:
        bon_metadines_category = -3
    elif 32 >= total_metadines >= 31.01:
        bon_metadines_category = -3.25
    elif 33 >= total_metadines >= 32.01:
        bon_metadines_category = -3.5
    elif 34 >= total_metadines >= 33.01:
        bon_metadines_category = -3.75
    elif 2.51 >= total_metadines >= 2.75:
        bon_metadines_category = -0.025
    elif 2.76 >= total_metadines >= 3:
        bon_metadines_category = -0.075
    elif 3.25 >= total_metadines >= 3.01:
        bon_metadines_category = -0.1
    elif 3.26 >= total_metadines >= 3.5:
        bon_metadines_category = -0.1
    elif 3.51 >= total_metadines >= 3.75:
        bon_metadines_category = -0.125
    elif 3.76 >= total_metadines >= 4:
        bon_metadines_category = -0.15
    else:
        bon_metadines_category = 0.00
    return bon_metadines_category , ob_t_metadine




def set_quantity():
    poid = float(input("la Quantité de recolte (q):"))
    return poid

def set_price():
    price = float(input("Le prix de vente/q: "))
    return price


def final_price(quantity, sell_price):
    prix_achat_definitif = quantity * sell_price
    return prix_achat_definitif

def prix_dbtr(dcs,quantity , sell_price,total_bonification):
    if dcs == "prix a débattre":
        prix = float(input("saisie prix a debattre "))
    else: prix =( quantity * sell_price)+total_bonification
    return prix

def  total_bonification(quantity, total):
    t_bonification =quantity * total
    return t_bonification

def total_( bon_p_specifique ,g_nuisible , bon_total_premier_category ,bon_grains_casse ,bon_total_dexieum_category , bon_grain_boute , bon_ble_tendre ,bon_t_metadines):
    total_value = bon_p_specifique +g_nuisible + bon_total_premier_category + bon_grains_casse + bon_total_dexieum_category + bon_grain_boute + bon_ble_tendre + bon_t_metadines
    return total_value





poid_specifique = set_poid_specifique()
bon_p_specifique , ob_p_specifique = poi_specifique(poid_specifique)
print("bonification poid specifique ",bon_p_specifique)
print("observation poid specifique",ob_p_specifique)

teneur_eau = set_humidite()
teneur_en_eau = hemuditi(teneur_eau)
print("observation tenur en eau",teneur_en_eau)
g_nuisibles = set_grain_nuisibles()
bon_nuisible , ob_nuisible  = grain_nuisibles(g_nuisibles)
print("bonification grains nuisible",bon_nuisible )
print("observation gains nuisible:",ob_nuisible)

ergot = set_ergot()
ergot_ = ergo_t(ergot)
print("observation ergo",ergot_)
first_decision = decision(poid_specifique,teneur_eau,g_nuisibles,ergot)
print("first decision :",first_decision)
print("*******************************************************************************")
debris_vegetaux = set_debris_vegetaux()
matiere_inertes = set_matiere_inertes()
sans_valeur = set_grains_sans_valeur()
g_caries = set_grains_caries()
t = calcule_totale_1er_category(debris_vegetaux ,matiere_inertes,sans_valeur,g_caries)
print("totale 1er category",t)
bon_total_1,ob_total_1  = totale_1er_category(t)
print("bonfication totale 1er category :",bon_total_1)
print("observation totale 1er category :",ob_total_1)

g_casse = set_grains_casse()
bon_casse , ob_casse = grains_casse(g_casse)
print("bonification g casse:", bon_casse)
print("observation casse", ob_casse)
g_maigres = set_grains_maigres()
g_echaudes = set_grains_echaudes()
g_etranders = set_grains_etranders()
g_roux = set_grains_roux()
g_mouchetes = set_grains_mouchetes()
g_boutes = set_grain_boute()
bon_gr_boute, ob_gr_boute = grain_boute(g_boutes)
print("bonification boute :",bon_gr_boute)
print("observation boute",ob_gr_boute)

g_punaises = set_grain_punaises()
g_piques = set_grains_piques()
t2 = calcule_totale_2eme_category(g_piques,g_punaises,g_boutes,g_mouchetes,g_roux,g_etranders,g_echaudes,g_maigres,g_casse)
total2 = totale_2eme_category(t2)
indice_notin = set_indice_notin()
ble_tendre = set_ble_tendre()
bon_bl_tendrs , ob_bl_tendre = ble_tendre_(ble_tendre)
print("bonification ble tendre :", bon_bl_tendrs)
print("observation ble tendre:", ob_bl_tendre)
total_metadines =calcul_totale_metadine(indice_notin,ble_tendre)
bon_t_m , ob_t_m= totale_metadine(total_metadines)
print("bonification totale metadines:",bon_t_m)
print("observation totale metadine :",ob_t_m)


decisions2 = decision_prix_debbattre(ble_tendre)
print("decision prix debbattre:", decisions2)
quantity = set_quantity()
s_price = set_price()
total_bon_value = total_(bon_p_specifique, bon_nuisible,bon_total_1,bon_casse,bon_gr_boute, t2,bon_bl_tendrs ,bon_t_m)
print("total bonification",total_bon_value)

p=prix_dbtr(decisions2, quantity, s_price , total_bon_value)
print("prix d'achet définitif(DA)",p)





