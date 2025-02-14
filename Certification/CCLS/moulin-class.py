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
        self._grains_carie = 0  # total 1
        self._grains_casse = 0  # if < 5 = total 2 // ref-bon
        self._grains_maigres = 0  # total 2
        self._grains_echaudes = 0  # total 2
        self._grains_etranders = 0  # total 2
        self._grains_roux = 0  # total 2
        self._grains_mouchtes = 0  # total 2
        self._grain_punises = 0  # total 2
        self._grains_piques = 0  # total 2
        self._grain_boute = 0  # if < 5 total 2 // ref-bon
        self._ble_tendre = 0  # obs (Prix a Débattre) // if <0.25 with total 3// > 0.25 alone // bon-ref
        self._indice_notin = 0  # total 3
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
    def grains_echaudes(self):
        return self._grains_echaudes

    @grains_echaudes.setter
    def grains_echaudes(self, value):
        self._grains_echaudes = value

    @property
    def grains_etranders(self):
        return self._grains_etranders

    @grains_etranders.setter
    def grains_etranders(self, value):
        self._grains_etranders = value

    @property
    def grains_roux(self):
        return self._grains_roux

    @grains_roux.setter
    def grains_roux(self, value):
        self._grains_roux = value

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
    def indice_notin(self):
        return self._indice_notin

    @indice_notin.setter
    def grains_mitadines(self, value):
        self._indice_notin = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def total_premier_category(self):
        return self._matiers_inertes + self._debris_vegetaux + self._grains_sans_valeur + self._grains_carie

    def total_dexieum_category(self):
        return self._grains_casse + self.grains_mouchtes + self._grains_echaudes + self._grain_boute \
               + self._grain_punises + self._grains_piques + self._grains_etranders + self._grains_roux

    def total_mitadines(self):
        return self._ble_tendre + self._indice_notin

    def decision(self):
        decision = Decision.DECISION_1

        if self._insect or self._carie or self._ancien_recolt or self.poid_specifique <= 72 or self.teneur_en_eau > 17 \
                or self.grain_nuisibles >= 2.5 or self.ergot >= 0.001:
            decision = Decision.DECISION_2
        return decision




