
def decision(p_specifique, teneur_eau , nuisible , ergot,existance_insecte_vivante ,presence_carie ,ancien_recolt):
    observation_list = []
    if 76 <= p_specifique <= 80:
        observation_list.append("sans bonification ni réfaction ")
    elif p_specifique > 80:
        observation_list.append("bonification ")
    elif 72 < p_specifique < 76:
        observation_list.append("rèfaction")
    elif p_specifique <= 72:
        observation_list.append("Refuse")
    if teneur_eau <= 17:
        observation_list.append("accepter")
    else: observation_list.append("Refuse")
    if nuisible <= 2.5:
        observation_list.append("sans bonification ni rèfaction")
    else:
        observation_list.append("Refuse")
    if ergot < 0.001:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    if existance_insecte_vivante == 0:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    if presence_carie == 0:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    if ancien_recolt ==0:
        observation_list.append("accepter")
    else:
        observation_list.append("Refuse")
    keys = ["Poids specifique", "teneur en eau", "Grain nuisible", "ergot" ,"existance insecte vivante","presence carie","ancien recolt"]
    my_dict = dict(zip(keys, observation_list))

    if my_dict["Poids specifique"] == "Refuse":
          Decision = "Refuse"
    elif my_dict["teneur en eau"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["Grain nuisible"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["ergot"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["ancien recolt"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["existance insecte vivante"] == "Refuse":
        Decision = "Refuse"
    elif my_dict["presence carie"] == "Refuse":
        Decision = "Refuse"
    else: Decision = "accepter"
    return Decision
def decision_prix_debbattre(total_premier_category ,total_dexieum_category,ble_tendre , total_metadine_category):
    observation_list = []
    if 1 <= total_premier_category <= 3:
        observation_list.append("sans bonification ni rèfaction")
    elif total_premier_category < 1:
        observation_list.append("bonification")
    elif 3 < total_premier_category < 6:
        observation_list.append("rèfaction")
    elif total_premier_category >= 6:
        observation_list.append("prix a débattre")

    if 1 <= total_dexieum_category <= 10:
        observation_list.append("sans bonification ni rèfaction")
    elif 10 < total_dexieum_category <= 20:
        observation_list.append("rèfaction")
    elif total_dexieum_category > 20:
        observation_list.append("prix a débattre")
    if ble_tendre <= 5:
        observation_list.append("bonification ")
    elif 5 < ble_tendre <= 10:
        observation_list.append("rèfaction")
    elif ble_tendre > 10:
        observation_list.append("prix a débattre")

    if total_metadine_category < 10:
        observation_list.append("bonification")
    elif 10 <= total_metadine_category <= 20:
        observation_list.append("sans bonification ni rèfaction")
    elif 20 < total_metadine_category < 70:
        observation_list.append("rèfaction")
    elif total_metadine_category >= 70:
        observation_list.append("prix a débattre")
    keys = [ "Total premiere category", "Total Dexieum category", "ble tendre", "Total metadine category"]
    my_dict = dict(zip(keys, observation_list))
    if my_dict["Total premiere category"] == "prix a débattre":
         dcs = "prix a débattre"
    elif my_dict["Total Dexieum category"] == "prix a débattre":
         dcs = "prix a débattre"
    elif my_dict["ble tendre"] == "prix a débattre":
         dcs = "prix a débattre"
         print("prix de ble tendre")
    elif my_dict["Total Dexieum category"] == "prix a débattre":
         dcs = "prix a débattre"
    else: dcs = "refaction normale"
    return dcs


def set_existance_insecte_vivante():
    existance_insecte_vivante = float(input("existance insecte vivante 1=oui 0=non"))
    return existance_insecte_vivante
def existance_insecte_vivante(existance_insecte_vivante):
    if existance_insecte_vivante == 0:
        ob_insect ="accepter"
    else:
        ob_insect = "Refuse"
    return ob_insect

def set_presence_carie():
    presence_carie = float(input("presence carie 1=oui 0=non :"))
    return presence_carie
def presence_carie(existance_caris):
    if existance_caris== 0:
        ob_carie ="accepter"
    else:
        ob_carie = "Refuse"
    return ob_carie

def set_ancien_recolt():
    ancien_recolt = float(input("ancien recolt 1=oui 0=non :"))
    return ancien_recolt
def ob_ancien_recolt_(ancien_recolt):
    if ancien_recolt== 0:
        ob_recolt ="accepter"
    else:
        ob_recolt = "Refuse"
    return ob_recolt








def set_poid_specific():
    poid_specifique = float(input("Poid spécifique kg/hl:"))
    return poid_specifique
def p_specific(poid_specifique):

    global ob_p_specifique
    if 76 <= poid_specifique <= 80:
        ob_p_specifique = "sans bonification ni réfaction "
    elif poid_specifique > 80:
        ob_p_specifique ="Bonification"
    elif 72 < poid_specifique < 76:
        ob_p_specifique = "Rèfaction"
    elif poid_specifique <= 72:
        ob_p_specifique = "Refuse"

    if 80.001 <= poid_specifique <= 80.25:
        valeur_poid_specifique = +0.15
    elif 80.251 <= poid_specifique <= 80.5:
        valeur_poid_specifique = +0.3
    elif 80.501 <= poid_specifique <= 80.75:
        valeur_poid_specifique = +0.45
    elif 80.751 <= poid_specifique <= 81:
        valeur_poid_specifique = +0.6
    elif 81.001 <= poid_specifique <= 81.25:
        valeur_poid_specifique = +0.75
    elif 81.251 <= poid_specifique <= 81.5:
        valeur_poid_specifique = +0.9
    elif 81.51 <= poid_specifique <= 81.75:
        valeur_poid_specifique = +1.05
    elif 81.751 <= poid_specifique <= 82:
        valeur_poid_specifique = +1.2
    elif 82.001 <= poid_specifique <= 82.25:
        valeur_poid_specifique = +1.3
    elif 82.251 <= poid_specifique <= 82.5:
        valeur_poid_specifique = +1.4
    elif 82.501 <= poid_specifique <= 82.75:
        valeur_poid_specifique = +1.5
    elif 82.751 <= poid_specifique <= 83:
        valeur_poid_specifique = +1.6
    elif 83.001 <= poid_specifique <= 83.25:
        valeur_poid_specifique = +1.65
    elif 83.251 <= poid_specifique <= 83.5:
        valeur_poid_specifique = +1.7
    elif 83.501 <= poid_specifique <= 83.75:
        valeur_poid_specifique= +1.75
    elif 83.751 <= poid_specifique <= 84:
        valeur_poid_specifique = +1.8
    elif 74.999 >= poid_specifique >= 75.75:
        valeur_poid_specifique = -0.1
    elif 75.749 >= poid_specifique >= 75.5:
        valeur_poid_specifique = -0.2
    elif 75.499 >= poid_specifique >= 75.25:
        valeur_poid_specifique = -0.3
    elif 75.299 >= poid_specifique >= 75:
        valeur_poid_specifique = -0.4
    elif 74.999 >= poid_specifique >= 74.75:
        valeur_poid_specifique = -0.6
    elif 74.749 >= poid_specifique >= 74.5:
        valeur_poid_specifique = -0.8
    elif 74.499 >= poid_specifique >= 74.25:
        valeur_poid_specifique = -1
    elif 74.249 >= poid_specifique >= 74:
        valeur_poid_specifique = -1.2
    elif 73.999 >= poid_specifique >= 73.75:
        valeur_poid_specifique = -1.5
    elif 73.749 >= poid_specifique >= 73.5:
        valeur_poid_specifique = -1.8
    elif 73.499 >= poid_specifique >= 73.25:
        valeur_poid_specifique = -2.1
    elif 73.249 >= poid_specifique >= 73:
        valeur_poid_specifique = -2.4
    elif 72.999 >= poid_specifique >= 72.75:
        valeur_poid_specifique = -2.7
    elif 72.749 >= poid_specifique >= 72.5:
        valeur_poid_specifique = -3
    elif 72.499 >= poid_specifique >= 72.25:
        valeur_poid_specifique = -3.3
    elif 72.249 >= poid_specifique >= 72:
        valeur_poid_specifique = -3.6
    elif poid_specifique < 72:
        valeur_poid_specifique = 0
        print("refuser")
    else:
        valeur_poid_specifique = 0.00
    return valeur_poid_specifique, ob_p_specifique


def set_teneur_en_eau():
    teneur_en_eau = float(input("teneur en eau%:"))

    return teneur_en_eau
def teneur_eau(teneur_en_eau):
    if teneur_en_eau <= 17:
       ob_teneur_en_eau = "accepter"
    else:
        ob_teneur_en_eau = "refuser"
    return  ob_teneur_en_eau

def set_grain_nuisibles():
    grains_nuisible = float(input("Grains nuisibles  %:"))

    return grains_nuisible
def grain_nuisibles(nuisible):
    if nuisible <= 2.5:
        ob_grain_nuisibles = "sans bonification ni rèfaction"
    else: ob_grain_nuisibles = "Refuser"
    return ob_grain_nuisibles

def set_ergot():
    ergot = float(input("ergot  %:"))

    return ergot
def ergott(ergot):
    if ergot < 0.001:
        ob_ergot = "accepter"
    else:
        ob_ergot = "refuse"
    return ob_ergot
def set_debris_vegetaux():
    debris_vegetaux = float(input("les débris végétaux  %:"))
    return debris_vegetaux


def set_matiere_inertes():
    matiers_inertes = float(input("matiérs inertes  %:"))
    return matiers_inertes


def set_grains_sons_valour():
    grains_sons_valours = float(input("grains sons valours  %:"))
    return grains_sons_valours

def calcul_1er_category(debris_vegetaux ,matiers_inertes ,grains_nuisible , grains_sons_valours):
    total_premier_category = debris_vegetaux + matiers_inertes + grains_nuisible + grains_sons_valours
    return total_premier_category
def premier_category(total_premier_category):
    global ob_premier_category
    if 1 <= total_premier_category <= 3:
        ob_premier_category ="sans bonification ni rèfaction"
    elif total_premier_category < 1:
        ob_premier_category ="bonification"
    elif 3 < total_premier_category < 6:
        ob_premier_category ="rèfaction"
    elif total_premier_category >= 6:
        ob_premier_category = "prix a débattue"

    if 0.999 >= total_premier_category >= 0.75:
        bon_ref_total_premier_category = +0.125
    elif 0.749 >= total_premier_category >= 0.5:
        bon_ref_total_premier_category = +0.25
    elif 0.499 >= total_premier_category >= 0.25:
        bon_ref_total_premier_category = +0.375
    elif 0.249 >= total_premier_category >= 0:
        bon_ref_total_premier_category = +0.5
    elif 3.001 <= total_premier_category <= 3.25:
        bon_ref_total_premier_category = -0.125
    elif 3.251 <= total_premier_category <= 3.5:
        bon_ref_total_premier_category = -0.25
    elif 3.501 <= total_premier_category <= 3.75:
        bon_ref_total_premier_category = -0.375
    elif 3.751 <= total_premier_category <= 4:
        bon_ref_total_premier_category = -0.5
    elif 4.001 <= total_premier_category <= 4.25:
        bon_ref_total_premier_category = -0.625
    elif 4.251 <= total_premier_category <= 4.5:
        bon_ref_total_premier_category = -0.75
    elif 4.501 <= total_premier_category <= 4.75:
        bon_ref_total_premier_category = -0.875
    elif 4.751 <= total_premier_category <= 5:
        bon_ref_total_premier_category = -1
    elif 5.001 <= total_premier_category <= 5.25:
        bon_ref_total_premier_category = -1.125
    elif 5.251 <= total_premier_category <= 5.5:
        bon_ref_total_premier_category = -1.25
    elif 5.501 <= total_premier_category <= 5.75:
        bon_ref_total_premier_category = -1.375
    elif 5.751 <= total_premier_category <= 6:
        bon_ref_total_premier_category = -1.5
    elif total_premier_category > 6:
        bon_ref_total_premier_category = 0
    else:
        bon_ref_total_premier_category = 0
    return bon_ref_total_premier_category, ob_premier_category

def set_grains_casse():
    grains_casse = float(input("Grains cassés  %:"))

    return grains_casse
def grains_casse(grains_casse):
    if grains_casse <= 5:
        ob_grains_casse = "sans bonification ni réfaction"
    else:
        ob_grains_casse = "réfaction"

    if 5.001 <= grains_casse <= 5.25:
        bon_ref_grains_casse = -0.075
    elif 5.251 <= grains_casse <= 5.5:
        bon_ref_grains_casse = -0.15
    elif 5.501 <= grains_casse <= 5.75:
        bon_ref_grains_casse = -0.225
    elif 5.751 <= grains_casse <= 6:
        bon_ref_grains_casse = -0.3
    elif 6.001 <= grains_casse <= 6.25:
        bon_ref_grains_casse = -0.375
    elif 6.251 <= grains_casse <= 6.5:
        bon_ref_grains_casse = -0.45
    elif 6.501 <= grains_casse <= 6.75:
        bon_ref_grains_casse = -0.525
    elif 6.751 <= grains_casse <= 7:
        bon_ref_grains_casse = -0.6
    elif 5 >= grains_casse >= 0:
        bon_ref_grains_casse = 0
    else:
        bon_ref_grains_casse = 0.00
    return bon_ref_grains_casse, ob_grains_casse
def set_grains_maigres():
    grains_maigres = float(input("Grains maigres  %:"))
    return grains_maigres

def set_grains_mouchetes():
    grains_mouchetes = float(input("Grains  mouchetés  %:"))
    return grains_mouchetes
def set_grain_punaises():
    grain_punaise = float(input("Grains punaisés  %:"))
    return grain_punaise


def set_grains_piques():
    grains_pique = float(input("Grains piqués  %:"))
    return grains_pique

def set_grain_boute():
    grain_boute = float(input("Grains bouté  %:"))
    return grain_boute
def grain_boute(grain_boute):
    global ob_grain_boute
    if grain_boute <= 5:
        ob_grain_boute = " bonification "
    else:
        ob_grain_boute = "refaction"
    if 5.001 <= grain_boute <= 6:
        bon_ref_grain_boute = -0.05
    elif 6.001 <= grain_boute <= 7:
        bon_ref_grain_boute = -0.1
    elif 7.001 <= grain_boute <= 8:
        bon_ref_grain_boute = -0.15
    elif 8.001 <= grain_boute <= 9:
        bon_ref_grain_boute = -0.2
    elif 9.001 <= grain_boute <= 10:
        bon_ref_grain_boute = -0.25
    elif 10.001 <= grain_boute <= 11:
        bon_ref_grain_boute = -0.3
    elif 11.001 <= grain_boute <= 12:
        bon_ref_grain_boute = -0.35
    elif 12.001 <= grain_boute <= 13:
        bon_ref_grain_boute = -0.4
    elif 13.001 <= grain_boute <= 14:
        bon_ref_grain_boute = -0.45
    elif 14.001 <= grain_boute <= 15:
        bon_ref_grain_boute = -0.5
    elif grain_boute>15:
        bon_ref_grain_boute = 0.5
    elif grain_boute<=5:
        bon_ref_grain_boute = 0
    else:
        bon_ref_grain_boute = 0
    return bon_ref_grain_boute, ob_grain_boute
def calcul_2eme_category(grains_casse  ,maigres, mouchetes , grain_boute, punaises , pique):
    global total_dexieum_category
    if grain_boute <=5 and grains_casse <=5 :
        total_dexieum_category =grains_casse + maigres + mouchetes + grain_boute + punaises + pique
    elif grain_boute > 5 and grains_casse > 5:
        total_dexieum_category = maigres + mouchetes + punaises + pique
    elif grain_boute >= 5:
        total_dexieum_category = grains_casse + maigres + mouchetes + punaises + pique
    elif grains_casse >= 5:
        total_dexieum_category = maigres + mouchetes + grain_boute + punaises + pique
    return total_dexieum_category

def dexieum_category(total_dexieum_category):
    global ob_total_dexieum_category
    if 0 <= total_dexieum_category <= 10:
        ob_total_dexieum_category = "sans bonification ni rèfaction"
    elif 10 < total_dexieum_category <= 20:
        ob_total_dexieum_category = "rèfaction"
    elif total_dexieum_category > 20:
        ob_total_dexieum_category = "prix a débattre"

    if 10.001 <= total_dexieum_category <= 11:
        bon_total_dexieum_category = -0.5
    elif 11.001 <= total_dexieum_category <= 12:
        bon_total_dexieum_category = -1
    elif 12.001 <= total_dexieum_category <= 13:
        bon_total_dexieum_category = -1.5
    elif 13.001 <= total_dexieum_category <= 14:
        bon_total_dexieum_category = -2
    elif 14.001 <= total_dexieum_category <= 15:
        bon_total_dexieum_category = -2.5
    elif 15.001 <= total_dexieum_category <= 16:
        bon_total_dexieum_category = -3
    elif 16.001 <= total_dexieum_category <= 17:
        bon_total_dexieum_category = -3.5
    elif 17.001 <= total_dexieum_category <= 18:
        bon_total_dexieum_category = -4
    elif 18.001 <= total_dexieum_category <= 19:
        bon_total_dexieum_category = -4.5
    elif 19.001 <= total_dexieum_category <= 20:
        bon_total_dexieum_category = -5
    elif total_dexieum_category > 20:
        bon_total_dexieum_category = 0
    elif total_dexieum_category <= 10:
        bon_total_dexieum_category = 0
    else:
        bon_total_dexieum_category = 0
    return bon_total_dexieum_category, ob_total_dexieum_category

def set_autres_cereales():
    autres_cereales = float(input("autres cereales:"))
    return autres_cereales


def set_ble_tendre():
    ble_tendre_dans_ble_dur = float(input("Blé Tendre dans Blé Dur   %:"))
    return ble_tendre_dans_ble_dur
def ble_tendre(ble_tendre_dans_ble_dur):
    global ob_ble_tendre
    if ble_tendre_dans_ble_dur <= 5:
        ob_ble_tendre ="sans bonification ni refaction "
    elif 5 < ble_tendre_dans_ble_dur <= 10:
        ob_ble_tendre = "rèfaction"
    elif ble_tendre_dans_ble_dur > 10:
        ob_ble_tendre ="prix a débattue"

    if 5.001 <= ble_tendre_dans_ble_dur <= 5.25:
        bon_ref_ble_tendre = -36.75
    elif 5.251 <= ble_tendre_dans_ble_dur <= 5.5:
        bon_ref_ble_tendre = -38.5
    elif 5.501 <= ble_tendre_dans_ble_dur <= 5.75:
        bon_ref_ble_tendre = -40.25
    elif 5.751 <= ble_tendre_dans_ble_dur <= 6:
        bon_ref_ble_tendre = -42
    elif 6.001 <= ble_tendre_dans_ble_dur <= 6.25:
        bon_ref_ble_tendre = -43.75
    elif 6.251 <= ble_tendre_dans_ble_dur <= 6.5:
        bon_ref_ble_tendre = -45.5
    elif 6.501 <= ble_tendre_dans_ble_dur <= 6.75:
        bon_ref_ble_tendre = -47.25
    elif 6.751 <= ble_tendre_dans_ble_dur <= 7:
        bon_ref_ble_tendre = -49
    elif 7.001 <= ble_tendre_dans_ble_dur <= 7.25:
        bon_ref_ble_tendre = -50.75
    elif 7.251 <= ble_tendre_dans_ble_dur <= 7.5:
        bon_ref_ble_tendre = -52.5
    elif 7.501 <= ble_tendre_dans_ble_dur <= 7.75:
        bon_ref_ble_tendre = -54.25
    elif 7.751 <= ble_tendre_dans_ble_dur <= 8:
        bon_ref_ble_tendre = -56
    elif 8.001 <= ble_tendre_dans_ble_dur <= 8.25:
        bon_ref_ble_tendre = -57.75
    elif 8.251 <= ble_tendre_dans_ble_dur <= 8.5:
        bon_ref_ble_tendre = -59.5
    elif 8.501 <= ble_tendre_dans_ble_dur <= 8.75:
        bon_ref_ble_tendre = -61.25
    elif 8.751 <= ble_tendre_dans_ble_dur <= 9:
        bon_ref_ble_tendre = -63
    elif 9.001 <= ble_tendre_dans_ble_dur <= 9.25:
        bon_ref_ble_tendre = -64.75
    elif 9.251 <= ble_tendre_dans_ble_dur <= 9.5:
        bon_ref_ble_tendre = -66.5
    elif 9.501 <= ble_tendre_dans_ble_dur <= 9.75:
        bon_ref_ble_tendre = -68.25
    elif 9.751 <= ble_tendre_dans_ble_dur <= 10:
        bon_ref_ble_tendre = -70
    elif ble_tendre_dans_ble_dur > 10:
        bon_ref_ble_tendre = 0
    else:
        bon_ref_ble_tendre = 0.00
    return bon_ref_ble_tendre, ob_ble_tendre
def set_Grains_mitadines():
    grains_mitadines = float(input("Grains mitadinès %:"))
    return grains_mitadines
def calcul_total_mitadines(ble_tendre_dans_ble_dur , grains_mitadines ):
    if ble_tendre_dans_ble_dur < 2.5:
        total_metadines = ble_tendre_dans_ble_dur + grains_mitadines
    else: total_metadines = grains_mitadines
    return total_metadines

def total_mitadines_category(total_metadines):
    global ob_mitadines_category
    if total_metadines < 10:
       ob_mitadines_category ="bonification"
    elif 10 <= total_metadines <= 20:
        ob_mitadines_category ="sans bonification ni rèfaction"
    elif 20 < total_metadines < 70:
        ob_mitadines_category ="rèfaction"
    elif total_metadines >= 70:
       ob_mitadines_category ="prix a débattue"
    if 0 <= total_metadines <= 10:
        bon_ref_total_metadines = +0.5
    elif 10.001 <= total_metadines <= 20:
        bon_ref_total_metadines = 0
    elif 20.001 <= total_metadines <= 21:
        bon_ref_total_metadines = -0.05
    elif 21.001 <= total_metadines <= 22:
        bon_ref_total_metadines = -0.1
    elif 22.001 <= total_metadines <= 23:
        bon_ref_total_metadines = -0.15
    elif 23.001 <= total_metadines <= 24:
        bon_ref_total_metadines = -0.2
    elif 24.001 <= total_metadines <= 25:
        bon_ref_total_metadines = -0.25
    elif 25.001 <= total_metadines <= 26:
        bon_ref_total_metadines = -0.3
    elif 26.001 <= total_metadines <= 27:
        bon_ref_total_metadines = -0.35
    elif 27.001 <= total_metadines <= 28:
        bon_ref_total_metadines = -0.4
    elif 28.001 <= total_metadines <= 29:
        bon_ref_total_metadines = -0.45
    elif 29.001 <= total_metadines <= 30:
        bon_ref_total_metadines = -0.5
    elif 30.001 <= total_metadines <= 31:
        bon_ref_total_metadines = -0.55
    elif 31.001 <= total_metadines <= 32:
        bon_ref_total_metadines = -0.6
    elif 32.001 <= total_metadines <= 33:
        bon_ref_total_metadines = -0.65
    elif 33.001 <= total_metadines <= 34:
        bon_ref_total_metadines = -0.7
    elif 34.001 <= total_metadines <= 35:
        bon_ref_total_metadines = -0.75
    elif 35.001 <= total_metadines <= 36:
        bon_ref_total_metadines = -0.8
    elif 36.001 <= total_metadines <= 37:
        bon_ref_total_metadines = -0.85
    elif 37.001 <= total_metadines <= 38:
        bon_ref_total_metadines = -0.9
    elif 38.001 <= total_metadines <= 39:
        bon_ref_total_metadines = -0.95
    elif 39.001 <= total_metadines <= 40:
        bon_ref_total_metadines = -1
    elif 40.001 <= total_metadines <= 41:
        bon_ref_total_metadines = -1.05
    elif 41.001 <= total_metadines <= 42:
        bon_ref_total_metadines = -1.1
    elif 42.001 <= total_metadines <= 43:
        bon_ref_total_metadines = -1.15
    elif 43.001 <= total_metadines <= 44:
        bon_ref_total_metadines = -1.2
    elif 44.001 <= total_metadines <= 45:
        bon_ref_total_metadines = -1.25
    elif 45.001 <= total_metadines <= 46:
        bon_ref_total_metadines = -1.3
    elif 46.001 <= total_metadines <= 47:
        bon_ref_total_metadines = -1.35
    elif 47.001 <= total_metadines <= 48:
        bon_ref_total_metadines = -1.4
    elif 48.001 <= total_metadines <= 49:
        bon_ref_total_metadines = -1.45
    elif 49.001 <= total_metadines <= 50:
        bon_ref_total_metadines = -1.5
    elif 50.001 <= total_metadines <= 51:
        bon_ref_total_metadines = -1.55
    elif 51.001 <= total_metadines <= 52:
        bon_ref_total_metadines = -1.6
    elif 52.001 <= total_metadines <= 53:
        bon_ref_total_metadines = -1.65
    elif 53.001 <= total_metadines <= 54:
        bon_ref_total_metadines = -1.7
    elif 54.001 <= total_metadines <= 55:
        bon_ref_total_metadines = -1.75
    elif 55.001 <= total_metadines <= 56:
        bon_ref_total_metadines = -1.8
    elif 56.001 <= total_metadines <= 57:
        bon_ref_total_metadines = - 1.85
    elif 57.001 <= total_metadines <= 58:
        bon_ref_total_metadines = -1.9
    elif 58.001 <= total_metadines <= 59:
        bon_ref_total_metadines = -1.95
    elif 59.001 <= total_metadines <= 60:
        bon_ref_total_metadines = -2
    elif 60.001 <= total_metadines <= 61:
        bon_ref_total_metadines = -2.05
    elif 61.001 <= total_metadines <= 62:
        bon_ref_total_metadines = -2.1
    elif 62.001 <= total_metadines <= 63:
        bon_ref_total_metadines = -2.15
    elif 63.001 <= total_metadines <= 64:
        bon_ref_total_metadines = -2.2
    elif 64.001 <= total_metadines <= 65:
        bon_ref_total_metadines = -2.25
    elif 65.001 <= total_metadines <= 66:
        bon_ref_total_metadines = -2.3
    elif 66.001 <= total_metadines <= 67:
        bon_ref_total_metadines = -2.35
    elif 67.001 <= total_metadines <= 68:
        bon_ref_total_metadines = -2.4
    elif 68.001 <= total_metadines <= 69:
        bon_ref_total_metadines = -2.45
    elif 69.001 <= total_metadines <= 70:
        bon_ref_total_metadines = -2.5
    elif total_metadines > 70:
        bon_ref_total_metadines = 0
    else:
        bon_ref_total_metadines = 0.00
    return bon_ref_total_metadines,ob_mitadines_category



def set_quantity():
    poid = float(input("la Quantité de recolte (q):"))
    return poid

def set_price():
    price = float(input("Le prix de vente/q: "))
    return price


def final_price(quantity, sell_price):
    prix_achat_definitif = quantity * sell_price
    return prix_achat_definitif

def prix_dbtr(dcs ,total_bonification):
    if dcs == "prix a débattre":
        prix = float(input("saisie prix a debattre "))
    else: prix = total_bonification
    return prix

def total_bonification(quantity, total):
    t_bonification =quantity * total
    return t_bonification

def total_( bon_p_specifique , bon_total_premier_category ,bon_grains_casse ,bon_total_dexieum_category , bon_grain_boute , bon_ble_tendre ,bon_t_metadines):
    total_value = bon_p_specifique + bon_total_premier_category + bon_grains_casse + bon_total_dexieum_category + bon_grain_boute + bon_ble_tendre + bon_t_metadines
    return total_value

insect = set_existance_insecte_vivante()
insct = existance_insecte_vivante(insect)
print("observation mort ou vivant ",insct)
carie = set_presence_carie()
cri = presence_carie(carie)
print("observation carie",cri)

recolt = set_ancien_recolt()
rclt = ob_ancien_recolt_(recolt)
print("observation recolt",recolt)
poi_specifique = set_poid_specific()
bon_specific, ob_specific =p_specific(poi_specifique)
print("bonification poids specific",bon_specific)
print("observasion poids specific",ob_specific)
print("***************************************************")
humidite = set_teneur_en_eau()
teneur_en_eau = teneur_eau(humidite)
print("observation teneure en eau :",teneur_en_eau)
print("*****************************************")
nuisible = set_grain_nuisibles()
g_nuisible = grain_nuisibles(nuisible)
print("observation grains nuisible :",g_nuisible)
print("****************************************")
ergot = set_ergot()
g_ergot= ergott(ergot)
print("observation ergot :",g_ergot)
print("****************************************")



decisions =decision(poi_specifique,humidite,nuisible,ergot ,insect,carie,recolt)
print("first decision:",decisions)
print("-----------------------------------------")
matiers_inertes = set_matiere_inertes()
debris_vegetaux = set_debris_vegetaux()
sons_valours = set_grains_sons_valour()
total_premier_category = calcul_1er_category(debris_vegetaux ,matiers_inertes ,nuisible, sons_valours)
print("totale 1er category", total_premier_category)
bon_t1 ,obt1 =premier_category(total_premier_category)
print("bonification t1:", bon_t1)
print("obbservation t1:", obt1)

grains_casses = set_grains_casse()
bon_g_casse, ob_g_casse = grains_casse(grains_casses)
print("bonification grains casses:",bon_g_casse)
print("observation grains casses", ob_g_casse)

grains_maigres = set_grains_maigres()
grains_mouchetes = set_grains_mouchetes()
grain_punaise = set_grain_punaises()
grains_pique = set_grains_piques()
grain_boutes = set_grain_boute()
bon_boute, ob_boute = grain_boute(grain_boutes)
print("bonification boute", bon_boute)
print("observation boute", ob_boute)
total_dexieumcategory = calcul_2eme_category(grains_casses, grains_maigres, grains_mouchetes, grain_boutes, grain_punaise , grains_pique)
print(total_dexieumcategory)
bon_total_dexieumcategory,ob_total_dexieumcategory= dexieum_category(total_dexieumcategory)
print("bonification totale 2eme category:", bon_total_dexieumcategory )
print("observation totale 2eme category: ", ob_total_dexieumcategory )

autres_cereales = set_autres_cereales()
ble_tendres = set_ble_tendre()
bon_ble_tendres_dans_ble_dur, ob_bon_ble_tendres_dans_ble_dur = ble_tendre(ble_tendres)
print("bonification ble tendre ", bon_ble_tendres_dans_ble_dur)
print("observation ble tendre", ob_bon_ble_tendres_dans_ble_dur )


g_mitadines = set_Grains_mitadines()
t_metadine =calcul_total_mitadines(ble_tendres,g_mitadines)
bon_t_mitadines, ob_t_mitadines =total_mitadines_category(t_metadine)
print(" bonification totale metadine",bon_t_mitadines)
print("observation totale metadine",ob_t_mitadines)

decisions2 = decision_prix_debbattre(total_premier_category,total_dexieumcategory,ble_tendres,t_metadine)
print("decision prix ", decisions2)
quantity = set_quantity()

total_bon_value = total_( bon_specific , bon_t1 ,bon_g_casse ,bon_total_dexieumcategory , bon_boute , bon_ble_tendres_dans_ble_dur ,bon_t_mitadines)
print("totale bonification refaction :",total_bon_value)

p=prix_dbtr(decisions2 , total_bon_value)
print("prix  :",p)




































