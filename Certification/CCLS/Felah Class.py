from enum import Enum


class Decision(Enum):
    # DECISION_1 = "Accepté"
    # DECISION_2 = "Refusé"
    DECISION_1 = True
    DECISION_2 = False


class Observation(Enum):
    OBSERVATION_1 = "Accepté"
    OBSERVATION_2 = "Refusé"
    OBSERVATION_3 = "Refaction"
    OBSERVATION_4 = "Bonification"
    OBSERVATION_5 = "Sans bonification ni refaction"
    OBSERVATION_6 = "Prix a Débattre"


class CCLS:
    def __init__(self):
        self._insect = False  # decision
        self._carie = False  # decision
        self._ancien_recolt = False  # decision
        self._poid_specifique = 0  # decision // ref-bon
        self._teneur_en_eau = 0  # decision
        self._grain_nuisibles = 0  # decision // ref-bon
        self._ergot = 0  # decision
        self._debris_vegetaux = 0  # total 1
        self._matiers_inertes = 0  # total 1
        self._grains_sans_valeur = 0  # total 1
        self._grains_casse = 0  # if < 5 = total 2 // ref-bon
        self._grains_maigres = 0  # total 2
        self._grains_mouchtes = 0  # total 2
        self._grain_punises = 0  # total 2
        self._grains_piques = 0  # total 2
        self._grain_boute = 0  # if < 5 total 2 // ref-bon
        self._autres_cereales = 0  #
        self._ble_tendre = 0  # obs (Prix a Débattre) // if <0.25 with total 3// > 0.25 alone // bon-ref
        self._grains_mitadines = 0  # total 3
        self._quantity = None
        self._observation = []
        self._bonification = []

    @property
    def poid_specifique(self):
        return self._poid_specifique

    @poid_specifique.setter
    def poid_specifique(self, value):
        self._poid_specifique = value

    @property
    def teneur_en_eau(self):
        return self._teneur_en_eau

    @teneur_en_eau.setter
    def teneur_en_eau(self, value):
        self._teneur_en_eau = value

    @property
    def grain_nuisibles(self):
        return self._grain_nuisibles

    @grain_nuisibles.setter
    def grain_nuisibles(self, value):
        self._grain_nuisibles = value

    @property
    def ergot(self):
        return self._ergot

    @ergot.setter
    def ergot(self, value):
        self._ergot = value

    @property
    def debris_vegetaux(self):
        return self._debris_vegetaux

    @debris_vegetaux.setter
    def debris_vegetaux(self, value):
        self._debris_vegetaux = value

    @property
    def matiers_inertes(self):
        return self._matiers_inertes

    @matiers_inertes.setter
    def matiers_inertes(self, value):
        self._matiers_inertes = value

    @property
    def grains_sans_valeur(self):
        return self._grains_sans_valeur

    @grains_sans_valeur.setter
    def grains_sans_valeur(self, value):
        self._grains_sans_valeur = value

    @property
    def grains_casse(self):
        return self._grains_casse

    @grains_casse.setter
    def grains_casse(self, value):
        self._grains_casse = value

    @property
    def grains_maigres(self):
        return self._grains_maigres

    @grains_maigres.setter
    def grains_maigres(self, value):
        self._grains_maigres = value

    @property
    def grains_mouchtes(self):
        return self._grains_mouchtes

    @grains_mouchtes.setter
    def grains_mouchtes(self, value):
        self._grains_mouchtes = value

    @property
    def grain_punises(self):
        return self._grain_punises

    @grain_punises.setter
    def grain_punises(self, value):
        self._grain_punises = value

    @property
    def grains_piques(self):
        return self._grains_piques

    @grains_piques.setter
    def grains_piques(self, value):
        self._grains_piques = value

    @property
    def grain_boute(self):
        return self._grain_boute

    @grain_boute.setter
    def grain_boute(self, value):
        self._grain_boute = value

    @property
    def autres_cereales(self):
        return self._autres_cereales

    @autres_cereales.setter
    def autres_cereales(self, value):
        self._autres_cereales = value

    @property
    def ble_tendre(self):
        return self._ble_tendre

    @ble_tendre.setter
    def ble_tendre(self, value):
        self._ble_tendre = value

    @property
    def grains_mitadines(self):
        return self._grains_mitadines

    @grains_mitadines.setter
    def grains_mitadines(self, value):
        self._grains_mitadines = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def total_premier_category(self):
        return self._matiers_inertes + self._debris_vegetaux + self._grains_sans_valeur + self._grain_nuisibles

    def total_dexieum_category(self):
        if self.grains_casse > 5 and self._grain_boute > 5:
            return self.grains_maigres + self.grains_mouchtes + self.grain_punises + self.grains_piques
        elif self._grains_casse > 5:
            return self.grains_maigres + self.grains_mouchtes + self.grain_punises + self.grains_piques + \
                self.grain_boute
        elif self._grain_boute > 5:
            return self.grains_maigres + self.grains_mouchtes + self.grain_punises + self.grains_piques + \
                self.grains_casse
        else:
            return self.grains_maigres + self.grains_mouchtes + self.grain_punises + self.grains_piques + \
                self.grains_casse + self.grain_boute

    def total_mitadines(self):
        if self.ble_tendre > 0.25:
            return self.grains_mitadines
        else:
            return self.grains_mitadines + self.ble_tendre

    def insects_checked(self):
        self._insect = True

    def insects_not_checked(self):
        self._insect = False

    def carie_checked(self):
        self._insect = True

    def carie_not_checked(self):
        self._insect = False

    def ancien_recolt_checked(self):
        self._ancien_recolt = True

    def ancien_recolt_not_checked(self):
        self._ancien_recolt = True

    def decision(self):
        decision = Decision.DECISION_1
        # if self._insect:
        #    decision = Decision.DECISION_2
        # elif self._carie:
        #     decision = Decision.DECISION_2
        # elif self._ancien_recolt:
        #     decision = Decision.DECISION_2
        # elif self.poid_specifique <= 72:
        #     decision = Decision.DECISION_2
        # elif self.teneur_en_eau > 17:
        #     decision = Decision.DECISION_2
        # elif self.grain_nuisibles >= 2.5:
        #     decision = Decision.DECISION_2
        # elif self.ergot >= 0.001:
        #     decision = Decision.DECISION_2
        if self._insect or self._carie or self._ancien_recolt or self.poid_specifique <= 72 or self.teneur_en_eau > 17 \
                or self.grain_nuisibles >= 2.5 or self.ergot >= 0.001:
            decision = Decision.DECISION_2
        return decision

    def bonification_calculation(self):
        calculation = {"insects": None, "carie": None, "ancien recolt": None, "Poids specifique": None,
                       "teneur en eau": None, "grain nuisibles": None, "ergot": None, "Debris vegeteux": None,
                       "Matiers inertes": None, "Grains sans valeur": None, "Grains casse": None,
                       "Grains maigres": None, "Grains Mouchtes": None, "Grains Punises": None, "Grains Piques": None,
                       "Grain boute": None, "ble tendre": None, "Grains mitadines": None,
                       "Total premier category": None, "Total dexieum category:": None, "Total mitadines": None}

        user_input = (self._insect, self._carie, self._ancien_recolt, self._poid_specifique, self._teneur_en_eau,
                      self._grain_nuisibles, self._ergot, self._debris_vegetaux, self._matiers_inertes,
                      self._grains_sans_valeur, self._grains_casse, self._grains_maigres, self._grains_mouchtes,
                      self._grain_punises, self._grains_piques, self._grain_boute, self._ble_tendre,
                      self._grains_mitadines, self.total_premier_category(), self.total_dexieum_category(),
                      self.total_mitadines())

        for i, key in enumerate(calculation.keys()):
            calculation[key] = user_input[i]

        if self._insect:
            self._observation.append(Observation.OBSERVATION_2)
            self._bonification.append(None)
        else:
            self._observation.append(Observation.OBSERVATION_1)
            self._bonification.append(None)

        if self._carie:
            # calculation["carie"] = Observation.OBSERVATION_2
            self._observation.append(Observation.OBSERVATION_2)
            self._bonification.append(None)
        else:
            self._observation.append(Observation.OBSERVATION_1)
            self._bonification.append(None)

        if self._ancien_recolt:
            self._observation.append(Observation.OBSERVATION_2)
            self._bonification.append(None)
        else:
            self._observation.append(Observation.OBSERVATION_1)
            self._bonification.append(None)

        # Poid Specifique observation
        if 76 <= self._poid_specifique <= 80:
            self._observation.append(Observation.OBSERVATION_5)
        elif self._poid_specifique > 80:
            self._observation.append(Observation.OBSERVATION_4)
        elif 72 < self._poid_specifique < 76:
            self._observation.append(Observation.OBSERVATION_3)
        elif self._poid_specifique <= 72:
            self._observation.append(Observation.OBSERVATION_2)

        # Poid Specifique Bonification et refaction
        if 80.001 <= self._poid_specifique <= 80.25:
            self._bonification.append(+0.15)
        elif 80.251 <= self._poid_specifique <= 80.5:
            self._bonification.append(+0.3)
        elif 80.501 <= self._poid_specifique <= 80.75:
            self._bonification.append(+0.45)
        elif 80.751 <= self._poid_specifique <= 81:
            self._bonification.append(+0.6)
        elif 81.001 <= self._poid_specifique <= 81.25:
            self._bonification.append(+0.75)
        elif 81.251 <= self._poid_specifique <= 81.5:
            self._bonification.append(+0.9)
        elif 81.51 <= self._poid_specifique <= 81.75:
            self._bonification.append(+1.05)
        elif 81.751 <= self._poid_specifique <= 82:
            self._bonification.append(+1.2)
        elif 82.001 <= self._poid_specifique <= 82.25:
            self._bonification.append(+1.3)
        elif 82.251 <= self._poid_specifique <= 82.5:
            self._bonification.append(+1.4)
        elif 82.501 <= self._poid_specifique <= 82.75:
            self._bonification.append(+1.5)
        elif 82.751 <= self._poid_specifique <= 83:
            self._bonification.append(+1.6)
        elif 83.001 <= self._poid_specifique <= 83.25:
            self._bonification.append(+1.65)
        elif 83.251 <= self._poid_specifique <= 83.5:
            self._bonification.append(+1.7)
        elif 83.501 <= self._poid_specifique <= 83.75:
            self._bonification.append(+1.75)
        elif 83.751 <= self._poid_specifique <= 84:
            self._bonification.append(+1.8)
        elif 74.999 >= self._poid_specifique >= 75.75:
            self._bonification.append(-0.1)
        elif 75.749 >= self._poid_specifique >= 75.5:
            self._bonification.append(-0.2)
        elif 75.499 >= self._poid_specifique >= 75.25:
            self._bonification.append(-0.3)
        elif 75.299 >= self._poid_specifique >= 75:
            self._bonification.append(-0.4)
        elif 74.999 >= self._poid_specifique >= 74.75:
            self._bonification.append(-0.6)
        elif 74.749 >= self._poid_specifique >= 74.5:
            self._bonification.append(-0.8)
        elif 74.499 >= self._poid_specifique >= 74.25:
            self._bonification.append(-1)
        elif 74.249 >= self._poid_specifique >= 74:
            self._bonification.append(-1.2)
        elif 73.999 >= self._poid_specifique >= 73.75:
            self._bonification.append(-1.5)
        elif 73.749 >= self._poid_specifique >= 73.5:
            self._bonification.append(-1.8)
        elif 73.499 >= self._poid_specifique >= 73.25:
            self._bonification.append(-2.1)
        elif 73.249 >= self._poid_specifique >= 73:
            self._bonification.append(-2.4)
        elif 72.999 >= self._poid_specifique >= 72.75:
            self._bonification.append(-2.7)
        elif 72.749 >= self._poid_specifique >= 72.5:
            self._bonification.append(-3)
        elif 72.499 >= self._poid_specifique >= 72.25:
            self._bonification.append(-3.3)
        elif 72.249 >= self._poid_specifique >= 72:
            self._bonification.append(-3.6)
        elif self._poid_specifique < 72:
            self._bonification.append(0)
        else:
            self._bonification.append(0)

        #  Humidity observation and None bonification
        if self._teneur_en_eau <= 17:
            self._observation.append(Observation.OBSERVATION_1)
            self._bonification.append(None)
        else:
            self._observation.append(Observation.OBSERVATION_2)
            self._bonification.append(None)

        # Grains nuisibles observation and None bonification
        if self._grain_nuisibles <= 2.5:
            self._observation.append(Observation.OBSERVATION_5)
            self._bonification.append(None)
        else:
            self._observation.append(Observation.OBSERVATION_2)
            self._bonification.append(None)

        # Ergot observation and None bonification
        if self._ergot < 0.001:
            self._observation.append(Observation.OBSERVATION_1)
            self._bonification.append(None)
        else:
            self._observation.append(Observation.OBSERVATION_2)
            self._bonification.append(None)

        # Debris vegeteux None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Matiers inertes None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Grains sans valeur None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Grains casse observation
        if self._grains_casse <= 5:
            self._observation.append(Observation.OBSERVATION_5)
        else:
            self._observation.append(Observation.OBSERVATION_3)

        # Grains casse Bonification et refaction
        if 5.001 <= self._grains_casse <= 5.25:
            self._bonification.append(-0.075)
        elif 5.251 <= self._grains_casse <= 5.5:
            self._bonification.append(-0.15)
        elif 5.501 <= self._grains_casse <= 5.75:
            self._bonification.append(-0.225)
        elif 5.751 <= self._grains_casse <= 6:
            self._bonification.append(-0.3)
        elif 6.001 <= self._grains_casse <= 6.25:
            self._bonification.append(-0.375)
        elif 6.251 <= self._grains_casse <= 6.5:
            self._bonification.append(-0.45)
        elif 6.501 <= self._grains_casse <= 6.75:
            self._bonification.append(-0.525)
        elif 6.751 <= self._grains_casse <= 7:
            self._bonification.append(-0.6)
        elif 5 >= self._grains_casse >= 0:
            self._bonification.append(0)
        else:
            self._bonification.append(0)

        # Grains maigres None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Grains Mouchtes None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Grains Punises None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Grains piques None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Grains boute observation
        if self._grain_boute <= 5:
            self._observation.append(Observation.OBSERVATION_4)
        else:
            self._observation.append(Observation.OBSERVATION_3)

        # Grains boute Bonification et refaction
        if 5.001 <= self._grain_boute <= 6:
            self._bonification.append(-0.05)
        elif 6.001 <= self._grain_boute <= 7:
            self._bonification.append(-0.1)
        elif 7.001 <= self._grain_boute <= 8:
            self._bonification.append(-0.15)
        elif 8.001 <= self._grain_boute <= 9:
            self._bonification.append(-0.2)
        elif 9.001 <= self._grain_boute <= 10:
            self._bonification.append(-0.25)
        elif 10.001 <= self._grain_boute <= 11:
            self._bonification.append(-0.3)
        elif 11.001 <= self._grain_boute <= 12:
            self._bonification.append(-0.35)
        elif 12.001 <= self._grain_boute <= 13:
            self._bonification.append(-0.4)
        elif 13.001 <= self._grain_boute <= 14:
            self._bonification.append(-0.45)
        elif 14.001 <= self._grain_boute <= 15:
            self._bonification.append(-0.5)
        elif self._grain_boute > 15:
            self._bonification.append(0.5)
        elif self._grain_boute <= 5:
            self._bonification.append(0)
        else:
            self._bonification.append(0)

        # ble tendre observation
        if self._ble_tendre <= 5:
            self._observation.append(Observation.OBSERVATION_5)
        elif 5 < self._ble_tendre <= 10:
            self._observation.append(Observation.OBSERVATION_3)
        elif self._ble_tendre > 10:
            self._observation.append(Observation.OBSERVATION_6)

        # ble tendre Bonification et refaction
        if 5.001 <= self._ble_tendre <= 5.25:
            self._bonification.append(-36.75)
        elif 5.251 <= self._ble_tendre <= 5.5:
            self._bonification.append(-38.5)
        elif 5.501 <= self._ble_tendre <= 5.75:
            self._bonification.append(-40.25)
        elif 5.751 <= self._ble_tendre <= 6:
            self._bonification.append(-42)
        elif 6.001 <= self._ble_tendre <= 6.25:
            self._bonification.append(-43.75)
        elif 6.251 <= self._ble_tendre <= 6.5:
            self._bonification.append(-45.5)
        elif 6.501 <= self._ble_tendre <= 6.75:
            self._bonification.append(-47.25)
        elif 6.751 <= self._ble_tendre <= 7:
            self._bonification.append(-49)
        elif 7.001 <= self._ble_tendre <= 7.25:
            self._bonification.append(-50.75)
        elif 7.251 <= self._ble_tendre <= 7.5:
            self._bonification.append(-52.5)
        elif 7.501 <= self._ble_tendre <= 7.75:
            self._bonification.append(-54.25)
        elif 7.751 <= self._ble_tendre <= 8:
            self._bonification.append(-56)
        elif 8.001 <= self._ble_tendre <= 8.25:
            self._bonification.append(-57.75)
        elif 8.251 <= self._ble_tendre <= 8.5:
            self._bonification.append(-59.5)
        elif 8.501 <= self._ble_tendre <= 8.75:
            self._bonification.append(-61.25)
        elif 8.751 <= self._ble_tendre <= 9:
            self._bonification.append(-63)
        elif 9.001 <= self._ble_tendre <= 9.25:
            self._bonification.append(-64.75)
        elif 9.251 <= self._ble_tendre <= 9.5:
            self._bonification.append(-66.5)
        elif 9.501 <= self._ble_tendre <= 9.75:
            self._bonification.append(-68.25)
        elif 9.751 <= self._ble_tendre <= 10:
            self._bonification.append(-70)
        elif self._ble_tendre > 10:
            self._bonification.append(float(input("Prix a débattre veuillez enter le prix de refaction : ")) * -1)
        else:
            self._bonification.append(0)

        # Grains mitadines None observation and None bonification
        self._observation.append(None)
        self._bonification.append(None)

        # Premier category observation
        if 1 <= self.total_premier_category() <= 3:
            self._observation.append(Observation.OBSERVATION_5)
        elif self.total_premier_category() < 1:
            self._observation.append(Observation.OBSERVATION_4)
        elif 3 < self.total_premier_category() < 6:
            self._observation.append(Observation.OBSERVATION_3)
        elif self.total_premier_category() >= 6:
            self._observation.append(Observation.OBSERVATION_6)

        # Premier category bonification refaction
        if 0.999 >= self.total_premier_category() >= 0.75:
            self._bonification.append(+0.125)
        elif 0.749 >= self.total_premier_category() >= 0.5:
            self._bonification.append(+0.25)
        elif 0.499 >= self.total_premier_category() >= 0.25:
            self._bonification.append(+0.375)
        elif 0.249 >= self.total_premier_category() >= 0:
            self._bonification.append(+0.5)
        elif 3.001 <= self.total_premier_category() <= 3.25:
            self._bonification.append(-0.125)
        elif 3.251 <= self.total_premier_category() <= 3.5:
            self._bonification.append(-0.25)
        elif 3.501 <= self.total_premier_category() <= 3.75:
            self._bonification.append(-0.375)
        elif 3.751 <= self.total_premier_category() <= 4:
            self._bonification.append(-0.5)
        elif 4.001 <= self.total_premier_category() <= 4.25:
            self._bonification.append(-0.625)
        elif 4.251 <= self.total_premier_category() <= 4.5:
            self._bonification.append(-0.75)
        elif 4.501 <= self.total_premier_category() <= 4.75:
            self._bonification.append(-0.875)
        elif 4.751 <= self.total_premier_category() <= 5:
            self._bonification.append(-1)
        elif 5.001 <= self.total_premier_category() <= 5.25:
            self._bonification.append(-1.125)
        elif 5.251 <= self.total_premier_category() <= 5.5:
            self._bonification.append(-1.25)
        elif 5.501 <= self.total_premier_category() <= 5.75:
            self._bonification.append(-1.375)
        elif 5.751 <= self.total_premier_category() <= 6:
            self._bonification.append(-1.5)
        elif self.total_premier_category() > 6:
            self._bonification.append(float(input("Prix a débattre veuillez enter le prix de refaction : ")) * -1)
        else:
            self._bonification.append(0)

        # Dexieum category observation
        if 0 <= self.total_dexieum_category() <= 10:
            self._observation.append(Observation.OBSERVATION_5)
        elif 10 < self.total_dexieum_category() <= 20:
            self._observation.append(Observation.OBSERVATION_3)
        elif self.total_dexieum_category() > 20:
            self._observation.append(Observation.OBSERVATION_6)

        # Dexieum category bonification and refaction
        if 10.001 <= self.total_dexieum_category() <= 11:
            self._bonification.append(-0.5)
        elif 11.001 <= self.total_dexieum_category() <= 12:
            self._bonification.append(-1)
        elif 12.001 <= self.total_dexieum_category() <= 13:
            self._bonification.append(-1.5)
        elif 13.001 <= self.total_dexieum_category() <= 14:
            self._bonification.append(-2)
        elif 14.001 <= self.total_dexieum_category() <= 15:
            self._bonification.append(-2.5)
        elif 15.001 <= self.total_dexieum_category() <= 16:
            self._bonification.append(-3)
        elif 16.001 <= self.total_dexieum_category() <= 17:
            self._bonification.append(-3.5)
        elif 17.001 <= self.total_dexieum_category() <= 18:
            self._bonification.append(-4)
        elif 18.001 <= self.total_dexieum_category() <= 19:
            self._bonification.append(-4.5)
        elif 19.001 <= self.total_dexieum_category() <= 20:
            self._bonification.append(-5)
        elif self.total_dexieum_category() <= 10:
            self._bonification.append(0)
        elif self.total_dexieum_category() > 20:
            self._bonification.append(float(input("Prix a débattre veuillez enter le prix de refaction : ")) * -1)
        else:
            self._bonification.append(0)

        # Total mitadines Observation
        if self.total_mitadines() < 10:
            self._observation.append(Observation.OBSERVATION_4)
        elif 10 <= self.total_mitadines() <= 20:
            self._observation.append(Observation.OBSERVATION_5)
        elif 20 < self.total_mitadines() < 70:
            self._observation.append(Observation.OBSERVATION_3)
        elif self.total_mitadines() >= 70:
            self._observation.append(Observation.OBSERVATION_6)

        # Total mitadines bonification and refaction
        if 0 <= self.total_mitadines() <= 10:
            self._bonification.append(+0.5)
        elif 10.001 <= self.total_mitadines() <= 20:
            self._bonification.append(0)
        elif 20.001 <= self.total_mitadines() <= 21:
            self._bonification.append(-0.05)
        elif 21.001 <= self.total_mitadines() <= 22:
            self._bonification.append(-0.1)
        elif 22.001 <= self.total_mitadines() <= 23:
            self._bonification.append(-0.15)
        elif 23.001 <= self.total_mitadines() <= 24:
            self._bonification.append(-0.2)
        elif 24.001 <= self.total_mitadines() <= 25:
            self._bonification.append(-0.25)
        elif 25.001 <= self.total_mitadines() <= 26:
            self._bonification.append(-0.3)
        elif 26.001 <= self.total_mitadines() <= 27:
            self._bonification.append(-0.35)
        elif 27.001 <= self.total_mitadines() <= 28:
            self._bonification.append(-0.4)
        elif 28.001 <= self.total_mitadines() <= 29:
            self._bonification.append(-0.45)
        elif 29.001 <= self.total_mitadines() <= 30:
            self._bonification.append(-0.5)
        elif 30.001 <= self.total_mitadines() <= 31:
            self._bonification.append(-0.55)
        elif 31.001 <= self.total_mitadines() <= 32:
            self._bonification.append(-0.6)
        elif 32.001 <= self.total_mitadines() <= 33:
            self._bonification.append(-0.65)
        elif 33.001 <= self.total_mitadines() <= 34:
            self._bonification.append(-0.7)
        elif 34.001 <= self.total_mitadines() <= 35:
            self._bonification.append(-0.75)
        elif 35.001 <= self.total_mitadines() <= 36:
            self._bonification.append(-0.8)
        elif 36.001 <= self.total_mitadines() <= 37:
            self._bonification.append(-0.85)
        elif 37.001 <= self.total_mitadines() <= 38:
            self._bonification.append(-0.9)
        elif 38.001 <= self.total_mitadines() <= 39:
            self._bonification.append(-0.95)
        elif 39.001 <= self.total_mitadines() <= 40:
            self._bonification.append(-1)
        elif 40.001 <= self.total_mitadines() <= 41:
            self._bonification.append(-1.05)
        elif 41.001 <= self.total_mitadines() <= 42:
            self._bonification.append(-1.1)
        elif 42.001 <= self.total_mitadines() <= 43:
            self._bonification.append(-1.15)
        elif 43.001 <= self.total_mitadines() <= 44:
            self._bonification.append(-1.2)
        elif 44.001 <= self.total_mitadines() <= 45:
            self._bonification.append(-1.25)
        elif 45.001 <= self.total_mitadines() <= 46:
            self._bonification.append(-1.3)
        elif 46.001 <= self.total_mitadines() <= 47:
            self._bonification.append(-1.35)
        elif 47.001 <= self.total_mitadines() <= 48:
            self._bonification.append(-1.4)
        elif 48.001 <= self.total_mitadines() <= 49:
            self._bonification.append(-1.45)
        elif 49.001 <= self.total_mitadines() <= 50:
            self._bonification.append(-1.5)
        elif 50.001 <= self.total_mitadines() <= 51:
            self._bonification.append(-1.55)
        elif 51.001 <= self.total_mitadines() <= 52:
            self._bonification.append(-1.6)
        elif 52.001 <= self.total_mitadines() <= 53:
            self._bonification.append(-1.65)
        elif 53.001 <= self.total_mitadines() <= 54:
            self._bonification.append(-1.7)
        elif 54.001 <= self.total_mitadines() <= 55:
            self._bonification.append(-1.75)
        elif 55.001 <= self.total_mitadines() <= 56:
            self._bonification.append(-1.8)
        elif 56.001 <= self.total_mitadines() <= 57:
            self._bonification.append(-1.85)
        elif 57.001 <= self.total_mitadines() <= 58:
            self._bonification.append(-1.9)
        elif 58.001 <= self.total_mitadines() <= 59:
            self._bonification.append(-1.95)
        elif 59.001 <= self.total_mitadines() <= 60:
            self._bonification.append(-2)
        elif 60.001 <= self.total_mitadines() <= 61:
            self._bonification.append(-2.05)
        elif 61.001 <= self.total_mitadines() <= 62:
            self._bonification.append(-2.1)
        elif 62.001 <= self.total_mitadines() <= 63:
            self._bonification.append(-2.15)
        elif 63.001 <= self.total_mitadines() <= 64:
            self._bonification.append(-2.2)
        elif 64.001 <= self.total_mitadines() <= 65:
            self._bonification.append(-2.25)
        elif 65.001 <= self.total_mitadines() <= 66:
            self._bonification.append(-2.3)
        elif 66.001 <= self.total_mitadines() <= 67:
            self._bonification.append(-2.35)
        elif 67.001 <= self.total_mitadines() <= 68:
            self._bonification.append(-2.4)
        elif 68.001 <= self.total_mitadines() <= 69:
            self._bonification.append(-2.45)
        elif 69.001 <= self.total_mitadines() <= 70:
            self._bonification.append(-2.5)
        elif self.total_mitadines() > 70:
            self._bonification.append(float(input("Prix a débattre veuillez enter le prix de refaction : ")) * -1)
        else:
            self._bonification.append(0)

        for i, key in enumerate(calculation.keys()):
            calculation[key] = self._observation[i]

        for i, key in enumerate(calculation.keys()):
            calculation[key] = self._bonification[i]

        print('the total number of observation :', len(self._observation))
        print('the total number of bonification :', len(self._bonification))
        print('the total number of input :', len(user_input))

        return calculation


fellah = CCLS()

print("\n quantity")
fellah.quantity = float(input("quantity (Q) : "))

print("\n calculate ")
fellah.poid_specifique = float(input("Poids_specifique(g) :"))
fellah.teneur_en_eau = float(input("teneur en eau (%) :"))
fellah.grain_nuisibles = float(input("grain nuisibles (%) :"))
fellah.ergot = float(input("ergot (%) :"))

print("\n total mitadines ")

fellah.ble_tendre = float(input("ble tendre (%) :"))
fellah.grains_mitadines = float(input("grains mitadines (%) :"))
print(fellah.total_mitadines())

print("\n 1 st category ")

fellah.matiers_inertes = float(input("matiers inertes (%) :"))
fellah.debris_vegetaux = float(input("debris vegetaux (%) :"))
fellah.grains_sans_valeur = float(input("grains sans valeur (%) :"))
print(fellah.total_premier_category())

print("\n 2 eme category ")

fellah.grains_casse = float(input("grains casse (%) : "))
fellah.grains_maigres = float(input("grains maigres (%) : "))
fellah.grains_mouchtes = float(input("grains mouchtes (%) : "))
fellah.grain_punises = float(input("grains punises (%) : "))
fellah.grains_piques = float(input("grains piques (%) : "))
fellah.grain_boute = float(input("grain boute (%) : "))
print(fellah.total_dexieum_category())
print("\n others")

fellah.autres_cereales = float(input("autres cereales (%) : "))

print("\n Agreage ")
Results = fellah.bonification_calculation()
