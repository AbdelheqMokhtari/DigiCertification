



class Seed_Ccls:
    def __init__(self, category):



        self._poid_specifique = None
        self._teneur_en_eau = None
        self._matiers_inertes = None
        self._debris_vegetaux = None
        self._nuisible = None
        self._ergot = None
        self._sans_valeur = None
        self.g_caries = None
        self._casse = None
        self._maigres = None
        self.g_echaudes = None
        self.g_etranders=None
        self.g_roux =None
        self._mouchetes = None
        self._punaises = None
        self._pique = None
        self._boute = None
        self._autres_cereales = None
        self.indice_notin = None
        self._ble_tendre= None
        self._g_mitadines = None
        self.set_poid = None
        self.set_price = None
        self._total_premier_category = 0
        self._total_dexieum_category = 0
        self._observation_list = []
        self._total_metadine_category = 0
        self._final_price = 0
        self._total_bonification = 0

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
    def matiers_inertes(self):
        return self._matiers_inertes

    @matiers_inertes.setter
    def matiers_inertes(self, value):
        self._matiers_inertes = value

    @property
    def debris_vegetaux(self):
        return self._debris_vegetaux

    @debris_vegetaux.setter
    def debris_vegetaux(self, value):
        self._debris_vegetaux = value

    @property
    def nuisible(self):
        return self._nuisible

    @nuisible.setter
    def nuisible(self, value):
        self._nuisible = value

    @property
    def ergot(self):
        return self._ergot

    @ergot.setter
    def ergot(self, value):
        self._ergot = value

    @property
    def sans_valeur(self):
        return self._sans_valeur

    @sans_valeur.setter
    def sans_valeur(self, value):
        self._sans_valeur = value

    @property
    def casse(self):
        return self._casse

    @casse.setter
    def casse(self, value):
        self._casse = value

    @property
    def maigres(self):
        return self._maigres

    @maigres.setter
    def maigres(self, value):
        self._maigres = value
    @property
    def g_echaudes(self):
        return self.g_echaudes
    @g_echaudes.setter
    def g_echaudes(self, value):
        self.g_echaudes = value
    @property
    def g_etranders(self):
        return self.g_etranders
    @g_etranders.setter
    def g_etranders(self, value):
        self.g_etranders = value
    @property
    def g_roux(self):
        return self.g_roux
    @g_roux.setter
    def g_roux(self, value):
        self.g_roux =value


    @property
    def mouchetes(self):
        return self._mouchetes

    @mouchetes.setter
    def mouchetes(self, value):
        self._mouchetes = value

    @property
    def punaises(self):
        return self._punaises

    @punaises.setter
    def punaises(self, value):
        self._punaises = value

    @property
    def pique(self):
        return self._pique

    @pique.setter
    def pique(self, value):
        self._pique = value

    @property
    def autres_cereales(self):
        return self._autres_cereales

    @autres_cereales.setter
    def autres_cereales(self, value):
        self.autres_cereales = value

    @property
    def ble_tendre(self):
        return self._ble_tendre

    @ble_tendre.setter
    def ble_tendre(self, value):
        self._ble_tendre = value

    @property
    def g_mitadines(self):
        return self._g_mitadines

    @g_mitadines.setter
    def g_mitadines(self, value):
        self._g_mitadines = value

    @property
    def total_premier_category(self):
        return self._total_premier_category

    @total_premier_category.setter
    def total_premier_category(self, value):
        self._total_premier_category = value

    @property
    def total_dexieum_category(self):
        return self._total_dexieum_category

    @total_dexieum_category.setter
    def total_dexieum_category(self, value):
        self._total_dexieum_category = value

    @property
    def total_metadine_category(self):
        return self._total_metadine_category

    @total_metadine_category.setter
    def total_metadine_category(self, value):
        self._total_metadine_category = value

    @property
    def final_price(self):
        return self._final_price

    @final_price.setter
    def final_price(self, value):
        self._final_price = value

    @property
    def total_bonification(self):
        return self._total_bonification

    @total_bonification.setter
    def total_bonification(self, value):
        self._total_bonification = value
    @property
    def set_poid(self):
        return self.set_poid
    @set_poid.setter
    def set_poid(self, value):
        self.set_poid = value
    @property
    def set_price(self):
        return self.set_price
    @set_price.setter
    def set_price(self, value):
        self.set_price = value

class CCLS_Fellah(Seed_Ccls):
    def __init__(self):
        super().__init__(None)
        self.valeur_poid_specifique = None
        self.bon_ref_total_premier_category = None
        self.bon_ref_grains_casse = None
        self.bon_ref_total_dexieum_category = None
        self.bon_ref_total_metadines = None
        self.bon_ref_ble_tendre_dans_ble_dur = None
        self.bon_ref_grain_boute = None

    def bonification(self):
        total_premier_category = self._debris_vegetaux + self._matiers_inertes + self._nuisible + self._ergot + self._sans_valeur
        if self._casse <= 5:

            self.total_dexieum_category = self._maigres + self._mouchetes + self._casse + self._boute + self._punaises +self._pique
        else:
            self.total_dexieum_category = self._maigres + self._mouchetes + self._boute + self._punaises + self._pique
        self._total_metadine_category = self._ble_tendre + self._g_mitadines
        total_value = 0.00
        if 80.001 <= self.poid_specifique <= 80.25:
            self.valeur_poid_specifique = +0.15
        elif 80.251 <= self.poid_specifique <= 80.5:
            self.valeur_poid_specifique = +0.3
        elif 80.501 <= self.poid_specifique <= 80.75:
            self.valeur_poid_specifique = +0.45
        elif 80.751 <= self.poid_specifique <= 81:
            self.valeur_poid_specifique = +0.6
        elif 81.001 <= self.poid_specifique <= 81.25:
            self.valeur_poid_specifique = +0.75
        elif 81.251 <= self.poid_specifique <= 81.5:
            self.valeur_poid_specifique = +0.9
        elif 81.51 <= self.poid_specifique <= 81.75:
            self.valeur_poid_specifique = +1.05
        elif 81.751 <= self.poid_specifique <= 82:
            self.valeur_poid_specifique = +1.2
        elif 82.001 <= self.poid_specifique <= 82.25:
            self.valeur_poid_specifique = +1.3
        elif 82.251 <= self.poid_specifique <= 82.5:
            self.valeur_poid_specifique = +1.4
        elif 82.501 <= self.poid_specifique <= 82.75:
            self.valeur_poid_specifique = +1.5
        elif 82.751 <= self.poid_specifique <= 83:
            self.valeur_poid_specifique = +1.6
        elif 83.001 <= self.poid_specifique <= 83.25:
            self.valeur_poid_specifique = +1.65
        elif 83.251 <= self.poid_specifique <= 83.5:
            self.valeur_poid_specifique = +1.7
        elif 83.501 <= self.poid_specifique <= 83.75:
            self.valeur_poid_specifique = +1.75
        elif 83.751 <= self.poid_specifique <= 84:
            self.valeur_poid_specifique = +1.8
        elif 74.999 >= self.poid_specifique >= 75.75:
            self.valeur_poid_specifique = -0.1
        elif 75.749 >= self.poid_specifique >= 75.5:
            self.valeur_poid_specifique = -0.2
        elif 75.499 >= self.poid_specifique >= 75.25:
            self.valeur_poid_specifique = -0.3
        elif 75.299 >= self.poid_specifique >= 75:
            self.valeur_poid_specifique = -0.4
        elif 74.999 >= self.poid_specifique >= 74.75:
            self.valeur_poid_specifique = -0.6
        elif 74.749 >= self.poid_specifique >= 74.5:
            self.valeur_poid_specifique = -0.8
        elif 74.499 >= self.poid_specifique >= 74.25:
            self.valeur_poid_specifique = -1
        elif 74.249 >= self.poid_specifique >= 74:
            self.valeur_poid_specifique = -1.2
        elif 73.999 >= self.poid_specifique >= 73.75:
            self.valeur_poid_specifique = -1.5
        elif 73.749 >= self.poid_specifique >= 73.5:
            self.valeur_poid_specifique = -1.8
        elif 73.499 >= self.poid_specifique >= 73.25:
            self.valeur_poid_specifique = -2.1
        elif 73.249 >= self.poid_specifique >= 73:
            self.valeur_poid_specifique = -2.4
        elif 72.999 >= self.poid_specifique >= 72.75:
            self.valeur_poid_specifique = -2.7
        elif 72.749 >= self.poid_specifique >= 72.5:
            self.valeur_poid_specifique = -3
        elif 72.499 >= self.poid_specifique >= 72.25:
            self.valeur_poid_specifique = -3.3
        elif 72.249 >= self.poid_specifique >= 72:
            self.valeur_poid_specifique = -3.6
        elif self.poid_specifique < 72:
            self.valeur_poid_specifique = 0
        else:
            self.valeur_poid_specifique = 0.00

        if 0.999 >= self.total_premier_category >= 0.75:
            self.bon_ref_total_premier_category = +0.125
        elif 0.749 >= self.total_premier_category >= 0.5:
            self.bon_ref_total_premier_category = +0.25
        elif 0.499 >= self.total_premier_category >= 0.25:
            self.bon_ref_total_premier_category = +0.375
        elif 0.249 >= self.total_premier_category >= 0:
            self.bon_ref_total_premier_category = +0.5
        elif 3.001 <= self.total_premier_category <= 3.25:
            self.bon_ref_total_premier_category = -0.125
        elif 3.251 <= self.total_premier_category <= 3.5:
            self.bon_ref_total_premier_category = -0.25
        elif 3.501 <= self.total_premier_category <= 3.75:
            self.bon_ref_total_premier_category = -0.375
        elif 3.751 <= self.total_premier_category <= 4:
            self.bon_ref_total_premier_category = -0.5
        elif 4.001 <= self.total_premier_category <= 4.25:
            self.bon_ref_total_premier_category = -0.625
        elif 4.251 <= self.total_premier_category <= 4.5:
            self.bon_ref_total_premier_category = -0.75
        elif 4.501 <= self.total_premier_category <= 4.75:
            self.bon_ref_total_premier_category = -0.875
        elif 4.751 <= total_premier_category <= 5:
            self.bon_ref_total_premier_category = -1
        elif 5.001 <= self.total_premier_category <= 5.25:
            self.bon_ref_total_premier_category = -1.125
        elif 5.251 <= self.total_premier_category <= 5.5:
            self.bon_ref_total_premier_category = -1.25
        elif 5.501 <= self.total_premier_category <= 5.75:
            self.bon_ref_total_premier_category = -1.375
        elif 5.751 <= self.total_premier_category <= 6:
            self.bon_ref_total_premier_category = -1.5
        elif self.total_premier_category > 6:
            self.bon_ref_total_premier_category = 0
        else:
            self.bon_ref_total_premier_category = 0

        if 5.001 <= self._casse <= 5.25:
            self.bon_ref_grains_casse = -0.075
        elif 5.251 <= self._casse <= 5.5:
            self.bon_ref_grains_casse = -0.15
        elif 5.501 <= self._casse <= 5.75:
            self.bon_ref_grains_casse = -0.225
        elif 5.751 <= self._casse <= 6:
            self.bon_ref_grains_casse = -0.3
        elif 6.001 <= self._casse <= 6.25:
            self.bon_ref_grains_casse = -0.375
        elif 6.251 <= self._casse <= 6.5:
            self.bon_ref_grains_casse = -0.45
        elif 6.501 <= self._casse <= 6.75:
            self.bon_ref_grains_casse = -0.525
        elif 6.751 <= self._casse <= 7:
            self.bon_ref_grains_casse = -0.6
        elif 5 >= self._casse >= 0:
            self.bon_ref_grains_casse = 0
        else:
            self.bon_ref_grains_casse = 0.00

        if 5.001 <= self._boute <= 6:
            self.bon_ref_grain_boute = -0.05
        elif 6.001 <= self._boute <= 7:
            self.bon_ref_grain_boute = -0.1
        elif 7.001 <= self._boute <= 8:
            self.bon_ref_grain_boute = -0.15
        elif 8.001 <= self._boute <= 9:
            self.bon_ref_grain_boute = -0.2
        elif 9.001 <= self._boute <= 10:
            self.bon_ref_grain_boute = -0.25
        elif 10.001 <= self._boute <= 11:
            self.bon_ref_grain_boute = -0.3
        elif 11.001 <= self._boute <= 12:
            self.bon_ref_grain_boute = -0.35
        elif 12.001 <= self._boute<= 13:
            self.bon_ref_grain_boute = -0.4
        elif 13.001 <= self._boute <= 14:
            self.bon_ref_grain_boute = -0.45
        elif 14.001 <= self._boute <= 15:
            self.bon_ref_grain_boute = -0.5
        elif self._boute > 15:
            self.bon_ref_grain_boute = 0.5
        elif self._boute <= 5:
            self.bon_ref_grain_boute = 0
        else:
            self.bon_ref_grain_boute = 0

        if 10.001 <= self.total_dexieum_category <= 11:
            self.bon_ref_total_dexieum_category = -0.5
        elif 11.001 <= self.total_dexieum_category <= 12:
            self.bon_ref_total_dexieum_category = -1
        elif 12.001 <= self.total_dexieum_category <= 13:
            self.bon_ref_total_dexieum_category = -1.5
        elif 13.001 <= self.total_dexieum_category <= 14:
            self.bon_ref_total_dexieum_category = -2
        elif 14.001 <= self.total_dexieum_category <= 15:
            self.bon_ref_total_dexieum_category = -2.5
        elif 15.001 <= self.total_dexieum_category <= 16:
            self.bon_ref_total_dexieum_category = -3
        elif 16.001 <= self.total_dexieum_category <= 17:
            self.bon_ref_total_dexieum_category = -3.5
        elif 17.001 <= self.total_dexieum_category <= 18:
            self.bon_ref_total_dexieum_category = -4
        elif 18.001 <= self.total_dexieum_category <= 19:
            self.bon_ref_total_dexieum_category = -4.5
        elif 19.001 <= self.total_dexieum_category <= 20:
            self.bon_ref_total_dexieum_category = -5
        elif self.total_dexieum_category > 20:
            self.bon_ref_total_dexieum_category = 0
        elif self.total_dexieum_category <= 10:
            self.bon_ref_total_dexieum_category = 0
        else:
            self.bon_ref_total_dexieum_category = 0

        if 5.001 <= self._ble_tendre <= 5.25:
            self.bon_ref_ble_tendre_dans_ble_dur = -36.75
        elif 5.251 <= self._ble_tendre <= 5.5:
            self.bon_ref_ble_tendre_dans_ble_dur = -38.5
        elif 5.501 <= self._ble_tendre <= 5.75:
            self.bon_ref_ble_tendre_dans_ble_dur = -40.25
        elif 5.751 <= self._ble_tendre <= 6:
            self.bon_ref_ble_tendre_dans_ble_dur = -42
        elif 6.001 <= self._ble_tendre <= 6.25:
            self.bon_ref_ble_tendre_dans_ble_dur = -43.75
        elif 6.251 <= self._ble_tendre <= 6.5:
            self.bon_ref_ble_tendre_dans_ble_dur = -45.5
        elif 6.501 <= self._ble_tendre <= 6.75:
            self.bon_ref_ble_tendre_dans_ble_dur = -47.25
        elif 6.751 <= self._ble_tendre <= 7:
            self.bon_ref_ble_tendre_dans_ble_dur = -49
        elif 7.001 <= self._ble_tendre <= 7.25:
            self.bon_ref_ble_tendre_dans_ble_dur = -50.75
        elif 7.251 <= self._ble_tendre <= 7.5:
            self.bon_ref_ble_tendre_dans_ble_dur = -52.5
        elif 7.501 <= self._ble_tendre <= 7.75:
            self.bon_ref_ble_tendre_dans_ble_dur = -54.25
        elif 7.751 <= self._ble_tendre <= 8:
            self.bon_ref_ble_tendre_dans_ble_dur = -56
        elif 8.001 <= self._ble_tendre <= 8.25:
            self.bon_ref_ble_tendre_dans_ble_dur = -57.75
        elif 8.251 <= self._ble_tendre <= 8.5:
            self.bon_ref_ble_tendre_dans_ble_dur = -59.5
        elif 8.501 <= self._ble_tendre <= 8.75:
            self.bon_ref_ble_tendre_dans_ble_dur = -61.25
        elif 8.751 <= self._ble_tendre <= 9:
            self.bon_ref_ble_tendre_dans_ble_dur = -63
        elif 9.001 <= self._ble_tendre <= 9.25:
            self.bon_ref_ble_tendre_dans_ble_dur = -64.75
        elif 9.251 <= self._ble_tendre <= 9.5:
            self.bon_ref_ble_tendre_dans_ble_dur = -66.5
        elif 9.501 <= self._ble_tendre <= 9.75:
            self.bon_ref_ble_tendre_dans_ble_dur = -68.25
        elif 9.751 <= self._ble_tendre <= 10:
            self.bon_ref_ble_tendre_dans_ble_dur = -70
        elif self._ble_tendre > 10:
            self.bon_ref_ble_tendre_dans_ble_dur = 0
        else:
            self.bon_ref_ble_tendre_dans_ble_dur = 0.00

        if 0 <= self._total_metadine_category<= 10:
            self.bon_ref_total_metadines = +0.5
        elif 10.001 <= self._total_metadine_category <= 20:
            self.bon_ref_total_metadines = 0
        elif 20.001 <= self._total_metadine_category<= 21:
            self.bon_ref_total_metadines = -0.05
        elif 21.001 <= self._total_metadine_category <= 22:
            self.bon_ref_total_metadines = -0.1
        elif 22.001 <= self._total_metadine_category <= 23:
            self.bon_ref_total_metadines = -0.15
        elif 23.001 <= self._total_metadine_category <= 24:
            self.bon_ref_total_metadines = -0.2
        elif 24.001 <= self._total_metadine_category <= 25:
            self.bon_ref_total_metadines = -0.25
        elif 25.001 <= self._total_metadine_category <= 26:
            self.bon_ref_total_metadines = -0.3
        elif 26.001 <= self._total_metadine_category <= 27:
            self.bon_ref_total_metadines = -0.35
        elif 27.001 <= self._total_metadine_category <= 28:
            self.bon_ref_total_metadines = -0.4
        elif 28.001 <= self._total_metadine_category <= 29:
            self.bon_ref_total_metadines = -0.45
        elif 29.001 <= self._total_metadine_category <= 30:
            self.bon_ref_total_metadines = -0.5
        elif 30.001 <= self._total_metadine_category <= 31:
            self.bon_ref_total_metadines = -0.55
        elif 31.001 <= self._total_metadine_category <= 32:
            self.bon_ref_total_metadines = -0.6
        elif 32.001 <= self._total_metadine_category<= 33:
            self.bon_ref_total_metadines = -0.65
        elif 33.001 <= self._total_metadine_category <= 34:
            self.bon_ref_total_metadines = -0.7
        elif 34.001 <= self._total_metadine_category <= 35:
            self.bon_ref_total_metadines = -0.75
        elif 35.001 <= self._total_metadine_category <= 36:
            self.bon_ref_total_metadines = -0.8
        elif 36.001 <= self._total_metadine_category<= 37:
            self.bon_ref_total_metadines = -0.85
        elif 37.001 <= self._total_metadine_category <= 38:
            self.bon_ref_total_metadines = -0.9
        elif 38.001 <= self._total_metadine_category <= 39:
            self.bon_ref_total_metadines = -0.95
        elif 39.001 <= self._total_metadine_category <= 40:
            self.bon_ref_total_metadines = -1
        elif 40.001 <= self._total_metadine_category <= 41:
            self.bon_ref_total_metadines = -1.05
        elif 41.001 <= self._total_metadine_category <= 42:
            self.bon_ref_total_metadines = -1.1
        elif 42.001 <= self._total_metadine_category <= 43:
            self.bon_ref_total_metadines = -1.15
        elif 43.001 <= self._total_metadine_category <= 44:
            self.bon_ref_total_metadines = -1.2
        elif 44.001 <= self._total_metadine_category <= 45:
            self.bon_ref_total_metadines = -1.25
        elif 45.001 <= self._total_metadine_category<= 46:
            self.bon_ref_total_metadines = -1.3
        elif 46.001 <= self._total_metadine_category <= 47:
            self.bon_ref_total_metadines = -1.35
        elif 47.001 <= self._total_metadine_category <= 48:
            self.bon_ref_total_metadines = -1.4
        elif 48.001 <= self._total_metadine_category <= 49:
            self.bon_ref_total_metadines = -1.45
        elif 49.001 <= self._total_metadine_category <= 50:
            self.bon_ref_total_metadines = -1.5
        elif 50.001 <= self._total_metadine_category <= 51:
            self.bon_ref_total_metadines = -1.55
        elif 51.001 <= self._total_metadine_category <= 52:
            self.bon_ref_total_metadines = -1.6
        elif 52.001 <= self._total_metadine_category <= 53:
            self.bon_ref_total_metadines = -1.65
        elif 53.001 <= self._total_metadine_category <= 54:
            self.bon_ref_total_metadines = -1.7
        elif 54.001 <= self._total_metadine_category <= 55:
            self.bon_ref_total_metadines = -1.75
        elif 55.001 <= self._total_metadine_category <= 56:
            self.bon_ref_total_metadines = -1.8
        elif 56.001 <= self._total_metadine_category <= 57:
            self.bon_ref_total_metadines = - 1.85
        elif 57.001 <= self._total_metadine_category <= 58:
            self.bon_ref_total_metadines = -1.9
        elif 58.001 <= self._total_metadine_category <= 59:
            self.bon_ref_total_metadines = -1.95
        elif 59.001 <= self._total_metadine_category <= 60:
            self.bon_ref_total_metadines = -2
        elif 60.001 <= self._total_metadine_category <= 61:
            self.bon_ref_total_metadines = -2.05
        elif 61.001 <= self._total_metadine_category <= 62:
            self.bon_ref_total_metadines = -2.1
        elif 62.001 <= self._total_metadine_category <= 63:
            self.bon_ref_total_metadines = -2.15
        elif 63.001 <= self._total_metadine_category <= 64:
            self.bon_ref_total_metadines = -2.2
        elif 64.001 <= self._total_metadine_category <= 65:
            self.bon_ref_total_metadines = -2.25
        elif 65.001 <= self._total_metadine_category <= 66:
            self.bon_ref_total_metadines = -2.3
        elif 66.001 <= self._total_metadine_category <= 67:
            self.bon_ref_total_metadines = -2.35
        elif 67.001 <= self._total_metadine_category <= 68:
            self.bon_ref_total_metadines = -2.4
        elif 68.001 <= self._total_metadine_category <= 69:
            self.bon_ref_total_metadines = -2.45
        elif 69.001 <= self._total_metadine_category <= 70:
            self.bon_ref_total_metadines = -2.5
        elif self._total_metadine_category > 70:
            self.bon_ref_total_metadines = 0
        else:
            self.bon_ref_total_metadines = 0.00

        self.total_value = self.valeur_poid_specifique + self.bon_ref_total_premier_category + self.bon_ref_grains_casse + self.bon_ref_total_dexieum_category + self.bon_ref_grain_boute + self.bon_ref_ble_tendre_dans_ble_dur + self.bon_ref_total_metadines
        return self.total_premier_category, self.total_dexieum_category, self._total_metadine_category, self.total_value, self.valeur_poid_specifique, self.bon_ref_total_premier_category, self.bon_ref_grains_casse, self.bon_ref_total_dexieum_category,self.bon_ref_ble_tendre_dans_ble_dur,self.bon_ref_total_metadines

    def observation(self):
        self._observation_list = []
        self.total_premier_category = self._debris_vegetaux + self._matiers_inertes + self._sans_valeur
        if self._casse <= 5:
            total_dexieum_category = self._casse + self._maigres + self._mouchetes + self._boute + self._punaises + self._pique
        else:
            total_dexieum_category = self._maigres + self._mouchetes + self._boute + self._punaises + self._pique
        total_metadine_category = self._g_mitadines + self._ble_tendre
        if 76 <= self.poid_specifique <= 80:
            self._observation_list.append("sans bonification ni réfaction ")
        elif self.poid_specifique > 80:
            self._observation_list.append("bonification ")
        elif 72 < self.poid_specifique < 76:
            self._observation_list.append("rèfaction")
        elif self.poid_specifique < 72:
            self._observation_list.append("Refuse")

        if self._teneur_en_eau <= 17:
            self._observation_list.append("accepter")
        else:
            self._observation_list.append("refuser")
        if self._nuisible <= 2.5:
            self._observation_list.append("sans bonification ni rèfaction")
        else:
            self._observation_list.append("Refuser")
        if self._ergot < 0.001:
            self._observation_list.append("accepter")
        else:
            self._observation_list.append("refuse")
        if 1 <= self._total_premier_category <= 3:
            self._observation_list.append("sans bonification ni rèfaction")
        elif self._total_premier_category < 1:
            self._observation_list.append("bonification")
        elif 3 < self._total_premier_category < 6:
            self._observation_list.append("rèfaction")
        elif self._total_premier_category >= 6:
            self._observation_list.append("prix a débattue")
        if self._casse <= 5:
            self._observation_list.append("sans bonification ni réfaction")
        else:
            self._observation_list.append("réfaction")
        if self._boute <= 5:
            self._observation_list.append(" bonification ")
        else:
            self._observation_list.append("refaction")
        if 1 <= self._total_dexieum_category <= 10:
            self._observation_list.append("sans bonification ni rèfaction")
        elif 10 < total_dexieum_category <= 20:
            self._observation_list.append("rèfaction")
        elif self._total_dexieum_category > 20:
            self._observation_list.append("prix a débattre")
        if self._ble_tendre <= 5:
            self._observation_list.append("bonification ")
        elif 5 < self._ble_tendre <= 10:
            self._observation_list.append("rèfaction")
        elif self._ble_tendre > 10:
            self._observation_list.append("prix a débattue")
        if self._total_metadine_category < 10:
            self._observation_list.append("bonification")
        elif 10 <= self._total_metadine_category <= 20:
            self._observation_list.append("sans bonification ni rèfaction")
        elif 20 < self._total_metadine_category < 70:
            self._observation_list.append("rèfaction")
        elif self._total_metadine_category >= 70:
            self._observation_list.append("prix a débattue")
        keys = ["Poids specifique", "teneur en eau", "Grain nuisible", "ergot", "Total premiere category",
                "Grain casse",
                "Grain boute", "Total Dexieum category", "ble tendre", "Total metadine category"]
        my_dict = dict(zip(keys, self._observation_list))
        return my_dict

class CCLS_Moulin(Seed_Ccls):
    def __init__(self):
        super().__init__(None)
        self.bon_p_specifique = None
        self.bon_premier_category = None
        self.bon_casse = None
        self.bon_boute = None
        self.bon_g_nuisibles = None
        self.bon_dexieum_category = None
        self.bon_metadines_category = None
        self.bon_ble_tendre = None

    def bonification(self):
        self._total_premier_category = self._debris_vegetaux + self._matiers_inertes + self._sans_valeur + self.g_caries
        self._total_dexieum_category = self._maigres + self.g_echaudes + self.g_etranders + self.g_roux + self._mouchetes + self._casse + self._boute + \
                                 self._punaises + self._pique
        self._total_metadine_category= self.indice_notin + self._ble_tendre
        if 77.99 >= self.poid_specifique >= 77.75:
            self.bon_p_specifique = -0.25
        elif 77.749 >= self.poid_specifique >= 77.5:
            self.bon_p_specifique = -0.5
        elif 77.499 >= self.poid_specifique >= 77.25:
            self.bon_p_specifique = -0.75
        elif 77.249 >= self.poid_specifique >= 77:
            self.bon_p_specifique = -1
        elif 76.99 >= self.poid_specifique >= 76.75:
            self.bon_p_specifique = -1.35
        elif 76.749 >= self.poid_specifique >= 76.5:
            self.bon_p_specifique = -1.7
        elif 76.499 >= self.poid_specifique >= 76.25:
            self.bon_p_specifique = -2.05
        elif 76.249 >= self.poid_specifique >= 76:
            self.bon_p_specifique = -2.4
        elif 75.999 >= self.poid_specifique >= 75.75:
            self.bon_p_specifique = -2.9
        elif 75.749 >= self.poid_specifique >= 75.5:
            self.bon_p_specifique = -3.4
        elif 75.499 >= self.poid_specifique >= 75.25:
            self.bon_p_specifique = -3.9
        elif 75.249 >= self.poid_specifique >= 75:
            self.bon_p_specifique = -4.4
        elif 74.999 >= self.poid_specifique >= 74.75:
            self.bon_p_specifique = -4.9

        elif 74.749 >= self.poid_specifique >= 74.5:
            self.bon_p_specifique = -5.4
        elif 74.999 >= self.poid_specifique>= 74.25:
            self.bon_p_specifique = -5.9
        elif 74.249 >= self.poid_specifique >= 74:
            self.bon_p_specifique = -6.4
        elif 78.001 <= self.poid_specifique <= 78.25:
            self.bon_p_specifique = +0.15
        elif 78.251 <= self.poid_specifique <= 78.5:
            self.bon_p_specifique = +0.3
        elif 78.501 <= self.poid_specifique <= 78.75:
            self.bon_p_specifique = +0.45
        elif 78.751 <= self.poid_specifique <= 79:
            self.bon_p_specifique = +0.6
        elif 79.001 <= self.poid_specifique <= 79.25:
            self.bon_p_specifique = +0.75
        elif 79.251 <= self.poid_specifique <= 79.5:
            self.bon_p_specifique = +0.9
        elif 79.501 <= self.poid_specifique <= 79.75:
            self.bon_p_specifique = +1.05
        elif 79.751 <= self.poid_specifique <= 80:
            self.bon_p_specifique = +1.20
        elif 80.001 <= self.poid_specifique <= 80.25:
            self.bon_p_specifique = +1.35
        elif 80.251 <= self.poid_specifique <= 80.5:
            self.bon_p_specifique = +1.5
        elif 80.501 <= self.poid_specifique <= 80.75:
            self.bon_p_specifique = +1.65
        elif 80.751 <= self.poid_specifique <= 81:
            self.bon_p_specifique = +1.80
        elif 81.001 <= self.poid_specifique <= 81.25:
            self.bon_p_specifique = +1.95
        elif 81.251 <= self.poid_specifique <= 81.5:
            self.bon_p_specifique = +2.1
        elif 81.501 <= self.poid_specifique <= 81.75:
            self.bon_p_specifique = +2.25
        elif 81.751 <= self.poid_specifique <= 82:
            self.bon_p_specifique = +2.4
        elif 82.001 <= self.poid_specifique <= 82.25:
            self.bon_p_specifique = +2.5
        elif 82.251 <= self.poid_specifique <= 82.5:
            self.bon_p_specifique = +2.6
        elif 82.501 <= self.poid_specifique <= 82.75:
            self.bon_p_specifique = +2.7
        elif 82.751 <= self.poid_specifique <= 83:
            self.bon_p_specifique = +2.8
        elif 83.001 <= self.poid_specifique <= 83.25:
            self.bon_p_specifique = +2.85
        elif 83.251 <= self.poid_specifique <= 83.5:
            self.bon_p_specifique = +2.9
        elif 83.5 <= self.poid_specifique <= 83.75:
            self.bon_p_specifique = +2.95
        elif 83.751 <= self.poid_specifique <= 84:
            self.bon_p_specifique = +3
        elif 84.001 <= self.poid_specifique <= 84.25:
            self.bon_p_specifique = +3.05
        elif 84.251 <= self.poid_specifique <= 84.5:
            self.bon_p_specifique = +3.1
        elif 84.501 <= self.poid_specifique <= 84.75:
            self.bon_p_specifique = +3.15
        elif 84.751 <= self.poid_specifique <= 85:
            self.bon_p_specifique = +3.2
        elif 85.001 <= self.poid_specifique <= 85.25:
            self.bon_p_specifique = +3.25
        elif 85.251 <= self.poid_specifique <= 85.5:
            self.bon_p_specifique = +3.3
        elif 85.501 <= self.poid_specifique <= 85.75:
            self.bon_p_specifique = +3.35
        elif self.poid_specifique > 85.75:
            self.bon_p_specifique = +3.35
        else:
            self.bon_p_specifique = 0.00
        if 0.051 <= self._nuisible <= 0.1:
            self.bon_g_nuisibles = -0.05
        elif 0.101 <= self._nuisible <= 0.15:
            self.bon_g_nuisibles = -0.1
        elif 0.151 <= self._nuisible<= 0.2:
            self.bon_g_nuisibles = -0.15
        elif 0.201 <= self._nuisible <= 0.25:
            self.bon_g_nuisibles = -0.2
        else:
            self.bon_g_nuisibles = 0.00
        if 0.999 >= self.total_premier_category >= 0.75:
            self.bon_premier_category = +0.15
        elif 0.749 >= self.total_premier_category >= 0.5:
            self.bon_premier_category = +0.3
        elif 0.499 >= self.total_premier_category >= 0.25:
            self.bon_premier_category = +0.45
        elif 0.249 >= self.total_premier_category >= 0:
            self.bon_premier_category = +0.6
        elif 1.01 <= self.total_premier_category <= 1.25:
            self.bon_premier_category = -0.15
        elif 1.26 <= self.total_premier_category <= 1.5:
            self.bon_premier_category = -0.3
        elif 1.51 <= self.total_premier_category <= 1.75:
            self.bon_premier_category = -0.45
        elif 1.76 <= self.total_premier_category <= 2:
            self.bon_premier_category = -0.6
        elif 2.01 <= self.total_premier_category <= 2.25:
            self.bon_premier_category = -0.75
        elif 2.26 <= self.total_premier_category <= 2.5:
            self.bon_premier_category = -0.9
        elif 2.51 <= self.total_premier_category <= 2.75:
            self.bon_premier_category = -1.05
        elif 2.76 <= self.total_premier_category <= 3:
            self.bon_premier_category = -1.2
        else:
            self.bon_premier_category = 0
        if 3.01 <= self._casse <= 3.25:
            self.bon_casse = -0.05
        elif 3.26 <=self._casse <= 3.5:
            self.bon_casse = -0.1
        elif 3.51 <= self._casse <= 3.75:
            self.bon_casse = -0.15
        elif 3.76 <= self._casse <= 4:
            self.bon_casse = -0.2
        elif 4.01 <= self._casse <= 4.25:
            self.bon_casse = -0.25
        elif 4.26 <= self._casse <= 4.5:
            self.bon_casse = -0.3
        elif 4.51 <= self._casse <= 4.75:
            self.bon_casse = -0.35
        elif 4.76 <= self._casse <= 5:
            self.bon_casse = -0.4
        elif 5.01 <= self._casse <= 5.25:
            self.bon_casse = -0.475
        elif 5.26 <= self._casse <= 5.5:
            self.bon_casse = -0.55
        elif 5.51 <= self._casse <= 5.75:
            self.bon_casse = -0.625
        elif 5.76 <= self._casse <= 6:
            self.bon_casse = -0.7
        elif 6.01 <= self._casse <= 6.25:
            self.bon_casse = -0.775
        elif 6.26 <= self._casse <= 6.5:
            self.bon_casse = -0.850
        elif 6.51 <= self._casse <= 6.75:
            self.bon_casse = -0, 925
        elif 6.76 <= self._casse <= 7:
            self.bon_casse = -1.0
        elif 7.01 <= self._casse <= 7.25:
            self.bon_casse = -1.075
        elif 7.26 <= self._casse <= 7.5:
            self.bon_casse = -1.15
        elif 7.51 <= self._casse <= 7.75:
            self.bon_casse = -1.225
        elif 7.76 <= self._casse <= 8:
            self.bon_casse = -1.3
        else:
            self.bon_casse = 0.00
        if 4.01 <= self._boute <= 5:
            self.bon_boute = -0.05
        elif 5.01 <=self._boute <= 6:
            self.bon_boute = -0.15
        elif 6.01 <= self._boute <= 7:
            self.bon_boute = -0.25
        else:
            self.bon_boute = 0
        if 10.01 <= self.total_dexieum_category <= 10.25:
            self.bon_dexieum_category = -0.075
        elif 10.26 <= self.total_dexieum_category <= 10.5:
            self.bon_dexieum_category = -0.15
        elif 10.51 <= self.total_dexieum_category <= 10.75:
            self.bon_dexieum_category = -0.225
        elif 10.76 <= self.total_dexieum_category <= 11:
            self.bon_dexieum_category = -0.3
        elif 11.01 <= self.total_dexieum_category <= 11.25:
            self.bon_dexieum_category = -0.375

        elif 11.26 <= self.total_dexieum_category <= 11.5:
            self.bon_dexieum_category = -0.45
        elif 11.51 <= self.total_dexieum_category <= 11.75:
            self.bon_dexieum_category = -0.525
        elif 11.76 <= self.total_dexieum_category <= 12:
            self.bon_dexieum_category = -0.6
        elif 12.01 <= self.total_dexieum_category <= 12.25:
            self.bon_dexieum_category = -0.675

        elif 12.26 <= self.total_dexieum_category <= 12.5:
            self.bon_dexieum_category = -0.75
        elif 12.51 <= self.total_dexieum_category <= 12.75:
            self.bon_dexieum_category = -0.825
        elif 12.76 <= self.total_dexieum_category <= 13:
            self.bon_dexieum_category = -0.9
        elif 13.01 <= self.total_dexieum_category <= 13.25:
            self.bon_dexieum_category = -0.975
        elif 13.26 <= self.total_dexieum_category <= 13.5:
            self.bon_dexieum_category = -1.05
        elif 13.51 <= self.total_dexieum_category <= 13.75:
            self.bon_dexieum_category = -1.125
        elif 13.76 <= self.total_dexieum_category <= 14:
            self.bon_dexieum_category = -1.2
        elif 14.01 <= self.total_dexieum_category <= 14.25:
            self.bon_dexieum_category = -1.275
        elif 14.26 <= self.total_dexieum_category <= 14.5:
            self.bon_dexieum_category = -1.35
        elif 14.51 <= self.total_dexieum_category <= 14.75:
            self.bon_dexieum_category = -1.425
        elif 14.76 <= self.total_dexieum_category <= 15:
            self.bon_dexieum_category = -1.5
        elif 15.01 <= self.total_dexieum_category <= 15.25:
            self.bon_dexieum_category = -1.6
        elif 15.26 <= self.total_dexieum_category <= 14.5:
            self.bon_dexieum_category = -1.7
        elif 15.51 <= self.total_dexieum_category <= 15.75:
            self.bon_dexieum_category = -1.8
        elif 15.76 <= self.total_dexieum_category <= 16:
            self.bon_dexieum_category = -1.9
        else:
            bon_dexieum_category = 0
        if 2.51 <= self.ble_tendre <= 2.75:
            self.bon_ble_tendre = -0.025
        elif 2.76 <= self.ble_tendre <= 3:
            self.bon_ble_tendre = -0.05
        elif 3.01 <= self.ble_tendre <= 3.25:
            self.bon_ble_tendre = -0.75
        elif 3.26 <= self.ble_tendre <= 3.5:
            self.bon_ble_tendre = -0.1
        elif 3.51 <= self.ble_tendre <= 3.75:
            bon_ble_tendre = -0.125
            print(bon_ble_tendre)
        elif 3.76 <= self.ble_tendre <= 4:
            self.bon_ble_tendre = -0.15
        elif 4.01 <= self.ble_tendre <= 4.25:
            self.bon_ble_tendre = -0.175
        elif 4.26 <= self.ble_tendre <= 4.5:
            self.bon_ble_tendre = -0.05
        elif 4.51 <= self.ble_tendre <= 4.75:
            self.bon_ble_tendre = -0.05
        elif 4.76 <= self.ble_tendre <= 5:
            self.bon_ble_tendre = -0.05
        elif self._ble_tendre > 5:
            self.bon_ble_tendre = 0
        elif self.ble_tendre < 2.5:
            self.bon_ble_tendre = 0
        else:
            self.bon_ble_tendre = 0.00
        if 11 >= self._total_metadine_category >= 10.01:
            self.bon_metadines_category = +0.13
        elif 10 >= self._total_metadine_category >= 9.01:
            self.bon_metadines_category = +0.195
        elif 9 >= self._total_metadine_category >= 0:
            self.bon_metadines_category = +0.26
        elif 13 >= self._total_metadine_category >= 12.01:
            self.bon_metadines_category = -0.065
        elif 14 >= self._total_metadine_category >= 13.01:
            self.bon_metadines_category = -0.14
        elif 15 >= self._total_metadine_category >= 14.01:
            self.bon_metadines_category = -0.225
        elif 16 >= self._total_metadine_category >= 15.01:
            self.bon_metadines_category = -0.32
        elif 17 >= self._total_metadine_category >= 16.01:
            self.bon_metadines_category = -0.425
        elif 18 >= self._total_metadine_category >= 17.01:
            self.bon_metadines_category = -0.555
        elif 19 >= self._total_metadine_category >= 18.01:
            self.bon_metadines_category = -0.675
        elif 20 >= self._total_metadine_category >= 19.01:
            self.bon_metadines_category = -0.825
        elif 21 >= self._total_metadine_category >= 20.01:
            self.bon_metadines_category = -0.975
        elif 22 >= self._total_metadine_category >= 21.01:
            self.bon_metadines_category = -1.15
        elif 23 >= self._total_metadine_category >= 22.01:
            self.bon_metadines_category = -1.325
        elif 24 >= self._total_metadine_category >= 23.01:
            self.bon_metadines_category = -1.525
        elif 25 >= self._total_metadine_category >= 24.01:
            self.bon_metadines_category = -1.7
        elif 26 >= self._total_metadine_category >= 25.01:
            self.bon_metadines_category = -1.9
        elif 27 >= self._total_metadine_category >= 26.01:
            self.bon_metadines_category = -2.1
        elif 28 >= self._total_metadine_category >= 27.01:
            self.bon_metadines_category = -2.3
        elif 29 >= self._total_metadine_category >= 28.01:
            self.bon_metadines_category = -2.5
        elif 30 >= self._total_metadine_category >= 29.01:
            self.bon_metadines_category = -2.75
        elif 31 >= self._total_metadine_category >= 30.01:
            self.bon_metadines_category = -3
        elif 32 >= self._total_metadine_category >= 31.01:
            self.bon_metadines_category = -3.25
        elif 33 >= self._total_metadine_category >= 32.01:
            self.bon_metadines_category = -3.5
        elif 34 >= self._total_metadine_category >= 33.01:
            self.bon_metadines_category = -3.75
        elif 2.51 >= self._total_metadine_category >= 2.75:
            self.bon_metadines_category = -0.025
        elif 2.76 >= self._total_metadine_category >= 3:
            self.bon_metadines_category = -0.075
        elif 3.25 >= self._total_metadine_category >= 3.01:
            self.bon_metadines_category = -0.1
        elif 3.26 >= self._total_metadine_category >= 3.5:
            self.bon_metadines_category = -0.1
        elif 3.51 >= self._total_metadine_category >= 3.75:
            self.bon_metadines_category = -0.125
        elif 3.76 >= self._total_metadine_category >= 4:
            self.bon_metadines_category = -0.15
        else:
            self.bon_metadines_category = 0.00
        self.bon_total = self.bon_p_specifique + self.bon_g_nuisibles + self.bon_premier_category + self.bon_casse + self.bon_dexieum_category + \
                    self.bon_boute + self.bon_ble_tendre + self.bon_metadines_category
        return self._total_premier_category,self._total_dexieum_category,self.bon_metadines_category,self.bon_total, self.bon_p_specifique, self.bon_g_nuisibles, self.bon_premier_category, self.bon_casse, self.bon_dexieum_category, \
               self.bon_ble_tendre, self.bon_metadines_category, self.bon_boute

    def observation(self):
        self.observation_list = []
        self._total_premier_category = self._debris_vegetaux + self._matiers_inertes + self._sans_valeur + self.g_caries
        self._total_dexieum_category = self._casse + self._maigres + self.g_echaudes + self.g_etranders + self.g_roux + self._mouchetes + self._boute + self._punaises + self._pique
        self._total_metadine_category = self.indice_notin + self._ble_tendre
        if self.poid_specifique == 78:
            self.observation_list.append("sans bonification ni réfaction")
        elif self.poid_specifique> 78:
            self.observation_list.append("bonification")
        elif 74 < self.poid_specifique < 78:
            self.observation_list.append("refaction")
        elif self.poid_specifique < 74:
            self.observation_list.append("refuser")
        if self._teneur_en_eau  <= 17:
            self.observation_list.append("accepter")
        else:
            self.observation_list.append("refuser")
        if 0.25 >= self._nuisible > 0.05:
            self.observation_list.append("refaction")
        elif self._nuisible <= 0.05:
            self.observation_list.append("accepter")
        else:
            self.observation_list.append("refuse")
        if self._ergot < 0.001:
            self.observation_list.append("accepter")
        else:
            self. observation_list.append("refuse")
        if self.total_premier_category <= 1:
            self.observation_list.append("sans bonification ni réfaction")
        else:
            self.observation_list.append("réfaction")
        if self._casse <= 3:
            self.observation_list.append("sans bonification ni réfaction")
        else:
            self.observation_list.append("réfaction")
        if self._boute <= 4:
            self.observation_list.append("sans bonification ni réfaction")
        else:
            self.observation_list.append("refaction")
        if self.total_dexieum_category <= 10:
            self.observation_list.append("sans bonification ni réfaction")
        else:
            self.observation_list.append("refaction")
        if 5 >= self.ble_tendre > 2.5:
            self.observation_list.append("réfaction")
        elif self.ble_tendre < 2.5:
            self.observation_list.append("Classé comme Graines mitadinès ")
        elif self.ble_tendre > 5:
            self.observation_list.append("Prix a dépattre ")
        if 12 >= self.total_metadine_category >= 11.1:
            self.observation_list.append("sans bonification ni réfaction")
        elif self.total_metadine_category <= 11:
            self.observation_list.append("bonification")
        elif self.total_metadine_category > 12:
            self.observation_list.append("réfaction")
        keys = ["Poids specifique", "humidité", "Grain nuisible", "ergot", "Total premiere category", "Grain casse",
                "Grain boute", "Total Dexieum category", "ble tendre", "Total metadine category"]
        my_dict = dict(zip(keys, self.observation_list))
        return my_dict
Seed_Ccls.poid_specifique = float(input("Poid spécifique kg/hl:"))
Seed_Ccls.teneur_en_eau =float(input("teneur en eau %:"))
Seed_Ccls.matiers_inertes = float(input("matiérs inertes  %:"))
Seed_Ccls.debris_vegetaux = float(input("les débris végétaux  %:"))
Seed_Ccls.nuisible = float(input("Grains nuisibles  %:"))
Seed_Ccls.ergot = float(input("ergot  %:"))
Seed_Ccls.sans_valeur = float(input("grains sans valeur  %:"))
Seed_Ccls.g_caries = float(input("grains cariés  %:"))
Seed_Ccls.casse = float(input("Grains cassés  %:"))
Seed_Ccls.maigres = float(input("Grains maigres  %:"))
Seed_Ccls.g_echaudes = float(input("Grains échaudés  %:"))
Seed_Ccls.g_etranders =  float(input("Grains etranders utilisable pour le bétail  %:"))
Seed_Ccls.g_roux = float(input("Grains de blé dur roux  %:"))
Seed_Ccls.mouchetes = float(input("Grains fortemnt mouchetés  %:"))
Seed_Ccls.punaises = float(input("Grains punaisés  %:"))
Seed_Ccls.boute = float(input("Grains bouté  %:"))
Seed_Ccls.indice_notin = float(input("indice notin (mitadinès):"))
for key in format(CCLS_Moulin.observation):
    print(f"{key}: {CCLS_Moulin.observation [key]}")













