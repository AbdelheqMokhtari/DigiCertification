from enum import Enum
from PyQt5 import QtCore, QtGui, QtWidgets


class SeedCategory(Enum):
    CATEGORY_1 = "Base"
    CATEGORY_2 = "Reproduction"
    CATEGORY_3 = "Ordinary"
    CATEGORY_4 = "Refused"


class Decision(Enum):
    DECISION_1 = "Accepté"
    DECISION_2 = "déclassé"
    DECISION_3 = "Refusé"
    DECISION_4 = "retiré"


class Seed:
    def __init__(self, category):
        if isinstance(category, SeedCategory):
            self.category = category
        else:
            raise ValueError("Invalid Category")

        # self.seed_category = seed_category
        self._decision = Decision.DECISION_3
        self._pure_seeds = None
        self._grains_multees = None
        self._debris_vegeteux = None
        self._balles = None
        self._terres = None
        self._gravies = None
        self._other_im = None
        self._inert_matter = None
        self._winter_wheat = 0
        self._winter_wheat_weight = None
        self._barely = 0
        self._barely_weight = None
        self._oats = 0
        self._oats_weight = None
        self._triticale = 0
        self._triticale_weight = None
        self._other_species = None
        self._total_seeds = None
        self._percentage = []
        self._output_weight = []
        self._state = True
        self._total = 0
        self._graines_fraiches = 0
        self._graines_dures = 0
        self._graines_mortes = 0
        self._germenation_percentage = 0
        # self.seed_category = SeedCategory.CATEGORY_1

    @property
    def graines_fraiches(self):
        return self._graines_fraiches

    @graines_fraiches.setter
    def graines_fraiches(self, value):
        self._graines_fraiches = value

    @property
    def graines_dures(self):
        return self._graines_dures

    @graines_dures.setter
    def graines_dures(self, value):
        self._graines_dures = value

    @property
    def graines_mortes(self):
        return self._graines_mortes

    @graines_mortes.setter
    def graines_mortes(self, value):
        self._graines_mortes = value

    @property
    def germenation_percentage(self):
        return self._germenation_percentage

    @germenation_percentage.setter
    def germenation_percentage(self, value):
        self._germenation_percentage = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def decision(self):
        return self._decision

    @decision.setter
    def decision(self, value):
        self._decision = value

    @property
    def output_weight(self):
        return self._output_weight

    @property
    def percentage(self):
        return self._percentage

    @property
    def pure_seeds(self):
        return self._pure_seeds

    @pure_seeds.setter
    def pure_seeds(self, value):
        self._pure_seeds = value

    @property
    def grains_multees(self):
        return self._grains_multees

    @grains_multees.setter
    def grains_multees(self, value):
        self._grains_multees = value

    @property
    def debris_vegeteux(self):
        return self._debris_vegeteux

    @debris_vegeteux.setter
    def debris_vegeteux(self, value):
        self._debris_vegeteux = value

    @property
    def balles(self):
        return self._balles

    @balles.setter
    def balles(self, value):
        self._balles = value

    @property
    def terres(self):
        return self._terres

    @terres.setter
    def terres(self, value):
        self._terres = value

    @property
    def gravies(self):
        return self._gravies

    @gravies.setter
    def gravies(self, value):
        self._gravies = value

    @property
    def other_im(self):
        return self._other_im

    @other_im.setter
    def other_im(self, value):
        self._other_im = value

    @property
    def winter_wheat(self):
        return self._winter_wheat

    @winter_wheat.setter
    def winter_wheat(self, value):
        self._winter_wheat += value

    @property
    def winter_wheat_weight(self):
        return self._winter_wheat_weight

    @winter_wheat_weight.setter
    def winter_wheat_weight(self, value):
        self._winter_wheat_weight = value

    @property
    def barely(self):
        return self._barely

    @barely.setter
    def barely(self, value):
        self._barely += value

    @property
    def barely_weight(self):
        return self._barely_weight

    @barely_weight.setter
    def barely_weight(self, value):
        self._barely_weight = value

    @property
    def oats(self):
        return self._oats

    @oats.setter
    def oats(self, value):
        self._oats += value

    @property
    def oats_weight(self):
        return self._oats_weight

    @oats_weight.setter
    def oats_weight(self, value):
        self._oats_weight = value

    @property
    def triticale(self):
        return self._triticale

    @triticale.setter
    def triticale(self, value):
        self._triticale += value

    @property
    def triticale_weight(self):
        return self._triticale_weight

    @triticale_weight.setter
    def triticale_weight(self, value):
        self._triticale_weight = value

    @property
    def other_species(self):
        return self._other_species

    @other_species.setter
    def other_species(self, value):
        self._other_species = value

    @property
    def inert_matter(self):
        return self._inert_matter

    @inert_matter.setter
    def inert_matter(self, value):
        self._inert_matter = value

    @property
    def total_seeds(self):
        return self._total_seeds

    @total_seeds.setter
    def total_seeds(self, value):
        self._total_seeds = value

    @property
    def sum_inert_mater(self):
        addition = self.grains_multees + self.debris_vegeteux + self.balles + self.terres + self.gravies + self.other_im
        return addition

    @sum_inert_mater.setter
    def sum_inert_mater(self, value):
        pass  # do nothing when trying to set sum_attr1_attr2

    def calculate_sum_and_set_inert_matter(self):
        self.inert_matter = self.sum_inert_mater

    @property
    def sum_other_species(self):
        addition = self.winter_wheat_weight + self.oats_weight + self.barely_weight + self.triticale_weight
        return addition

    @sum_other_species.setter
    def sum_other_species(self, value):
        pass  # do nothing when trying to set sum_attr1_attr2

    def calculate_sum_and_set_other_species(self):
        self.other_species = self.sum_other_species

    @property
    def sum_total_seed(self):
        addition = self.pure_seeds + self.other_species + self.inert_matter
        return addition

    @sum_total_seed.setter
    def sum_total_seed(self, value):
        pass  # do nothing when trying to set sum_attr1_attr2

    def calculate_sum_and_set_total_seed(self):
        self.total_seeds = self.sum_total_seed

    @property
    def purity_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.pure_seeds / self.total_seeds) * 100

    @property
    def inert_matter_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.inert_matter / self.total_seeds) * 100

    @property
    def other_species_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.other_species / self.total_seeds) * 100

    @property
    def grains_multees_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.grains_multees / self.total_seeds) * 100

    @property
    def debris_vegeteux_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.debris_vegeteux / self.total_seeds) * 100

    @property
    def balles_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.balles / self.total_seeds) * 100

    @property
    def terres_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.terres / self.total_seeds) * 100

    @property
    def gravies_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.gravies / self.total_seeds) * 100

    @property
    def other_im_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.other_im / self.total_seeds) * 100

    @property
    def winter_wheat_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.winter_wheat_weight / self.total_seeds) * 100

    @property
    def barely_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.barely_weight / self.total_seeds) * 100

    @property
    def oats_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.oats_weight / self.total_seeds) * 100

    @property
    def triticale_percentage(self):
        if self.total_seeds == 0:
            return 0
        return (self.triticale_weight / self.total_seeds) * 100

    def calculate_percentage(self):
        self._percentage.append(self.purity_percentage)
        self._percentage.append(self.inert_matter_percentage)
        self._percentage.append(self.grains_multees_percentage)
        self._percentage.append(self.debris_vegeteux_percentage)
        self._percentage.append(self.balles_percentage)
        self._percentage.append(self.terres_percentage)
        self._percentage.append(self.gravies_percentage)
        self._percentage.append(self.other_im_percentage)
        self._percentage.append(self.other_species_percentage)
        self._percentage.append(self.winter_wheat_percentage)
        self._percentage.append(self.barely_percentage)
        self._percentage.append(self.oats_percentage)
        self._percentage.append(self.triticale_percentage)
        self._percentage.append(self.purity_percentage + self.inert_matter_percentage + self.other_species_percentage)

    def take_decision(self, value):
        if value == 0:
            purity = self.purity_percentage
            category = self.category
            if category == SeedCategory.CATEGORY_1:
                if purity >= 99:
                    self.decision = Decision.DECISION_1
                elif 99 > purity >= 97:
                    self.decision = Decision.DECISION_2
                else:
                    self.decision = Decision.DECISION_3

            elif category == SeedCategory.CATEGORY_2:
                if purity >= 98:
                    self.decision = Decision.DECISION_1
                elif 98 > purity >= 97:
                    self.decision = Decision.DECISION_2
                else:
                    self.decision = Decision.DECISION_3

            elif category == SeedCategory.CATEGORY_3:
                if purity >= 97:
                    self.decision = Decision.DECISION_1
                else:
                    self.decision = Decision.DECISION_3
        if value == 1:
            total = self.total
            category = self.category
            if category == SeedCategory.CATEGORY_1:
                if total > 4:
                    self.decision = Decision.DECISION_2
            elif category == SeedCategory.CATEGORY_2:
                if total > 4:
                    self.decision = Decision.DECISION_2
        if value == 2:
            germination = self.germenation_percentage
            if germination < 85:
                self.decision = Decision.DECISION_3

    def seed_category_update(self, value):

        if value == 0:
            purity = self.purity_percentage
            category = self.category
            if self.category == SeedCategory.CATEGORY_1:
                if purity >= 99:
                    self.category = SeedCategory.CATEGORY_1
                elif 99 > purity >= 98:
                    self.category = SeedCategory.CATEGORY_2
                elif purity >= 97:
                    self.category = SeedCategory.CATEGORY_3
                else:
                    self.category = SeedCategory.CATEGORY_4

            elif category == SeedCategory.CATEGORY_2:
                if purity >= 98:
                    self.category = SeedCategory.CATEGORY_2
                elif purity >= 97:
                    self.category = SeedCategory.CATEGORY_3
                else:
                    self.category = SeedCategory.CATEGORY_4

            elif category == SeedCategory.CATEGORY_3:
                if purity >= 97:
                    self.category = SeedCategory.CATEGORY_3
                else:
                    self.category = SeedCategory.CATEGORY_4

            else:
                self.category = SeedCategory.CATEGORY_4
        if value == 1:
            total = self.total
            category = self.category
            if category == SeedCategory.CATEGORY_1:
                if 8 > total > 4:
                    self.category = SeedCategory.CATEGORY_2
                elif total > 8:
                    self.category = SeedCategory.CATEGORY_3
            if category == SeedCategory.CATEGORY_2:
                if total > 8:
                    self.category = SeedCategory.CATEGORY_3
        if value == 2:
            germination = self.germenation_percentage
            if germination < 85:
                self.category = SeedCategory.CATEGORY_4

    @property
    def seed_category(self):
        return self.category.value

    @property
    def seed_decision(self):
        return self.decision.value

    @property
    def calculate_total(self):
        total = 0
        for attribute in [self._winter_wheat, self._oats, self._barely, self._triticale]:
            if isinstance(attribute, int):
                total += attribute
        self.total = total
        return True

    @property
    def output_inert_matter(self):
        self._output_weight.append(self.grains_multees + self.debris_vegeteux + self.balles + self.terres + self.gravies
                                   + self.other_im)
        return self.grains_multees + self.debris_vegeteux + self.balles + self.terres + self.gravies + self.other_im

    @property
    def output_other_species(self):
        self._output_weight.append(self.winter_wheat_weight + self.barely_weight + self.oats_weight
                                   + self.triticale_weight)
        return self.winter_wheat_weight + self.barely_weight + self.oats_weight + self.triticale_weight

    @property
    def output_total_specific_purity(self):
        self._output_weight.append(self.pure_seeds + self.output_inert_matter + self.output_other_species)
        return True

    def calculate_germenation_percentage(self):
        positive = self._graines_fraiches
        total = self._graines_fraiches + self._graines_mortes + self._graines_dures
        self.germenation_percentage = (positive / total) * 100

    @property
    def calculate_purity_specific(self):
        self.calculate_sum_and_set_other_species()
        self.calculate_sum_and_set_inert_matter()
        self.calculate_sum_and_set_total_seed()
        self.calculate_percentage()
        self._state = self.output_total_specific_purity
        self.take_decision(0)
        if self.decision == Decision.DECISION_2:
            self.seed_category_update(0)
        return self._state
        # return self._percentage

    @property
    def calculate_enumeration(self):
        self._state = self.calculate_total
        self.take_decision(1)
        if self.decision == Decision.DECISION_2:
            self.seed_category_update(1)
        return self._state

    @property
    def calculate_germenation(self):
        self.calculate_germenation_percentage()
        self.take_decision(2)
        if self.decision == Decision.DECISION_3:
            self.seed_category_update(2)
        return True


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_sample_code = QtWidgets.QLabel(self.centralwidget)
        self.label_sample_code.setGeometry(QtCore.QRect(40, 20, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_sample_code.setFont(font)
        self.label_sample_code.setObjectName("label_sample_code")
        self.label_code_etablissement = QtWidgets.QLabel(self.centralwidget)
        self.label_code_etablissement.setGeometry(QtCore.QRect(40, 60, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_code_etablissement.setFont(font)
        self.label_code_etablissement.setObjectName("label_code_etablissement")
        self.label_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_weight.setGeometry(QtCore.QRect(40, 100, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_weight.setFont(font)
        self.label_weight.setObjectName("label_weight")
        self.label_date_reception = QtWidgets.QLabel(self.centralwidget)
        self.label_date_reception.setGeometry(QtCore.QRect(40, 140, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_date_reception.setFont(font)
        self.label_date_reception.setObjectName("label_date_reception")
        self.input_sample_code = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sample_code.setGeometry(QtCore.QRect(240, 20, 220, 30))
        self.input_sample_code.setObjectName("input_sample_code")
        self.input_code_etablissement = QtWidgets.QLineEdit(self.centralwidget)
        self.input_code_etablissement.setGeometry(QtCore.QRect(240, 60, 220, 30))
        self.input_code_etablissement.setObjectName("input_code_etablissement")
        self.input_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.input_weight.setGeometry(QtCore.QRect(240, 100, 220, 30))
        self.input_weight.setObjectName("input_weight")
        self.date_edit_reception = QtWidgets.QDateEdit(self.centralwidget)
        self.date_edit_reception.setGeometry(QtCore.QRect(240, 140, 220, 30))
        self.date_edit_reception.setObjectName("date_edit_reception")
        self.label_species = QtWidgets.QLabel(self.centralwidget)
        self.label_species.setGeometry(QtCore.QRect(750, 20, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_species.setFont(font)
        self.label_species.setObjectName("label_species")
        self.label_variety = QtWidgets.QLabel(self.centralwidget)
        self.label_variety.setGeometry(QtCore.QRect(750, 60, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_variety.setFont(font)
        self.label_variety.setObjectName("label_variety")
        self.label_category = QtWidgets.QLabel(self.centralwidget)
        self.label_category.setGeometry(QtCore.QRect(750, 100, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_category.setFont(font)
        self.label_category.setObjectName("label_category")
        self.label_sample_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_sample_weight.setGeometry(QtCore.QRect(750, 140, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_sample_weight.setFont(font)
        self.label_sample_weight.setObjectName("label_sample_weight")
        self.input_sample_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sample_weight.setGeometry(QtCore.QRect(950, 140, 220, 30))
        self.input_sample_weight.setObjectName("input_sample_weight")
        self.label_seed_purity = QtWidgets.QLabel(self.centralwidget)
        self.label_seed_purity.setGeometry(QtCore.QRect(30, 280, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_seed_purity.setFont(font)
        self.label_seed_purity.setObjectName("label_seed_purity")
        self.input_seed_purity = QtWidgets.QLineEdit(self.centralwidget)
        self.input_seed_purity.setGeometry(QtCore.QRect(270, 280, 120, 25))
        self.input_seed_purity.setObjectName("input_seed_purity")
        self.label_inert_matter = QtWidgets.QLabel(self.centralwidget)
        self.label_inert_matter.setGeometry(QtCore.QRect(30, 320, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_inert_matter.setFont(font)
        self.label_inert_matter.setObjectName("label_inert_matter")
        self.label_grains_mutilees = QtWidgets.QLabel(self.centralwidget)
        self.label_grains_mutilees.setGeometry(QtCore.QRect(160, 370, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_grains_mutilees.setFont(font)
        self.label_grains_mutilees.setObjectName("label_grains_mutilees")
        self.label_debris_vegetaux = QtWidgets.QLabel(self.centralwidget)
        self.label_debris_vegetaux.setGeometry(QtCore.QRect(160, 410, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_debris_vegetaux.setFont(font)
        self.label_debris_vegetaux.setObjectName("label_debris_vegetaux")
        self.output_seed_purity = QtWidgets.QLabel(self.centralwidget)
        self.output_seed_purity.setGeometry(QtCore.QRect(430, 280, 120, 25))
        self.output_seed_purity.setFrameShape(QtWidgets.QFrame.Box)
        self.output_seed_purity.setText("")
        self.output_seed_purity.setObjectName("output_seed_purity")
        self.output_inert_matter_total = QtWidgets.QLabel(self.centralwidget)
        self.output_inert_matter_total.setGeometry(QtCore.QRect(270, 320, 120, 25))
        self.output_inert_matter_total.setFrameShape(QtWidgets.QFrame.Box)
        self.output_inert_matter_total.setText("")
        self.output_inert_matter_total.setObjectName("output_inert_matter_total")
        self.output_inert_matter = QtWidgets.QLabel(self.centralwidget)
        self.output_inert_matter.setGeometry(QtCore.QRect(430, 320, 120, 25))
        self.output_inert_matter.setFrameShape(QtWidgets.QFrame.Box)
        self.output_inert_matter.setText("")
        self.output_inert_matter.setObjectName("output_inert_matter")
        self.input_graines_mutilees = QtWidgets.QLineEdit(self.centralwidget)
        self.input_graines_mutilees.setGeometry(QtCore.QRect(330, 370, 120, 25))
        self.input_graines_mutilees.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_graines_mutilees.setObjectName("input_graines_mutilees")
        self.input_debris_vegetaux = QtWidgets.QLineEdit(self.centralwidget)
        self.input_debris_vegetaux.setGeometry(QtCore.QRect(330, 410, 120, 25))
        self.input_debris_vegetaux.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_debris_vegetaux.setObjectName("input_debris_vegetaux")
        self.label_balles = QtWidgets.QLabel(self.centralwidget)
        self.label_balles.setGeometry(QtCore.QRect(160, 450, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_balles.setFont(font)
        self.label_balles.setObjectName("label_balles")
        self.label_terres = QtWidgets.QLabel(self.centralwidget)
        self.label_terres.setGeometry(QtCore.QRect(160, 490, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_terres.setFont(font)
        self.label_terres.setObjectName("label_terres")
        self.label_gravies = QtWidgets.QLabel(self.centralwidget)
        self.label_gravies.setGeometry(QtCore.QRect(160, 530, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_gravies.setFont(font)
        self.label_gravies.setObjectName("label_gravies")
        self.label_autres = QtWidgets.QLabel(self.centralwidget)
        self.label_autres.setGeometry(QtCore.QRect(160, 570, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_autres.setFont(font)
        self.label_autres.setObjectName("label_autres")
        self.input_balles = QtWidgets.QLineEdit(self.centralwidget)
        self.input_balles.setGeometry(QtCore.QRect(330, 450, 120, 25))
        self.input_balles.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_balles.setObjectName("input_balles")
        self.input_terres = QtWidgets.QLineEdit(self.centralwidget)
        self.input_terres.setGeometry(QtCore.QRect(330, 490, 120, 25))
        self.input_terres.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_terres.setObjectName("input_terres")
        self.input_gravies = QtWidgets.QLineEdit(self.centralwidget)
        self.input_gravies.setGeometry(QtCore.QRect(330, 530, 120, 25))
        self.input_gravies.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_gravies.setObjectName("input_gravies")
        self.input_autres = QtWidgets.QLineEdit(self.centralwidget)
        self.input_autres.setGeometry(QtCore.QRect(330, 570, 120, 25))
        self.input_autres.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_autres.setObjectName("input_autres")
        self.output_graines_mutilees = QtWidgets.QLabel(self.centralwidget)
        self.output_graines_mutilees.setGeometry(QtCore.QRect(490, 370, 120, 25))
        self.output_graines_mutilees.setFrameShape(QtWidgets.QFrame.Box)
        self.output_graines_mutilees.setText("")
        self.output_graines_mutilees.setObjectName("output_graines_mutilees")
        self.output_Debris_Vegetaux = QtWidgets.QLabel(self.centralwidget)
        self.output_Debris_Vegetaux.setGeometry(QtCore.QRect(490, 410, 120, 25))
        self.output_Debris_Vegetaux.setFrameShape(QtWidgets.QFrame.Box)
        self.output_Debris_Vegetaux.setText("")
        self.output_Debris_Vegetaux.setObjectName("output_Debris_Vegetaux")
        self.output_balles = QtWidgets.QLabel(self.centralwidget)
        self.output_balles.setGeometry(QtCore.QRect(490, 450, 120, 25))
        self.output_balles.setFrameShape(QtWidgets.QFrame.Box)
        self.output_balles.setText("")
        self.output_balles.setObjectName("output_balles")
        self.output_terres = QtWidgets.QLabel(self.centralwidget)
        self.output_terres.setGeometry(QtCore.QRect(490, 490, 120, 25))
        self.output_terres.setFrameShape(QtWidgets.QFrame.Box)
        self.output_terres.setText("")
        self.output_terres.setObjectName("output_terres")
        self.output_gravies = QtWidgets.QLabel(self.centralwidget)
        self.output_gravies.setGeometry(QtCore.QRect(490, 530, 120, 25))
        self.output_gravies.setFrameShape(QtWidgets.QFrame.Box)
        self.output_gravies.setText("")
        self.output_gravies.setObjectName("output_gravies")
        self.output_autres = QtWidgets.QLabel(self.centralwidget)
        self.output_autres.setGeometry(QtCore.QRect(490, 570, 120, 25))
        self.output_autres.setFrameShape(QtWidgets.QFrame.Box)
        self.output_autres.setText("")
        self.output_autres.setObjectName("output_autres")
        self.label_other_species = QtWidgets.QLabel(self.centralwidget)
        self.label_other_species.setGeometry(QtCore.QRect(30, 620, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_other_species.setFont(font)
        self.label_other_species.setObjectName("label_other_species")
        self.output_other_spacies_total = QtWidgets.QLabel(self.centralwidget)
        self.output_other_spacies_total.setGeometry(QtCore.QRect(270, 620, 120, 25))
        self.output_other_spacies_total.setFrameShape(QtWidgets.QFrame.Box)
        self.output_other_spacies_total.setText("")
        self.output_other_spacies_total.setObjectName("output_other_spacies_total")
        self.output_other_species = QtWidgets.QLabel(self.centralwidget)
        self.output_other_species.setGeometry(QtCore.QRect(430, 620, 120, 25))
        self.output_other_species.setFrameShape(QtWidgets.QFrame.Box)
        self.output_other_species.setText("")
        self.output_other_species.setObjectName("output_other_species")
        self.label_winter_wheat = QtWidgets.QLabel(self.centralwidget)
        self.label_winter_wheat.setGeometry(QtCore.QRect(160, 670, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_winter_wheat.setFont(font)
        self.label_winter_wheat.setObjectName("label_winter_wheat")
        self.label_analyse_id = QtWidgets.QLabel(self.centralwidget)
        self.label_analyse_id.setGeometry(QtCore.QRect(1460, 20, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_analyse_id.setFont(font)
        self.label_analyse_id.setObjectName("label_analyse_id")
        self.label_year_haverst = QtWidgets.QLabel(self.centralwidget)
        self.label_year_haverst.setGeometry(QtCore.QRect(1460, 60, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_year_haverst.setFont(font)
        self.label_year_haverst.setObjectName("label_year_haverst")
        self.label_date_sampling = QtWidgets.QLabel(self.centralwidget)
        self.label_date_sampling.setGeometry(QtCore.QRect(1460, 100, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_date_sampling.setFont(font)
        self.label_date_sampling.setObjectName("label_date_sampling")
        self.input_analyse_id = QtWidgets.QLineEdit(self.centralwidget)
        self.input_analyse_id.setGeometry(QtCore.QRect(1660, 20, 220, 30))
        self.input_analyse_id.setObjectName("input_analyse_id")
        self.input_year_haverst = QtWidgets.QLineEdit(self.centralwidget)
        self.input_year_haverst.setGeometry(QtCore.QRect(1660, 60, 220, 30))
        self.input_year_haverst.setObjectName("input_year_haverst")
        self.date_edit_sampling = QtWidgets.QDateEdit(self.centralwidget)
        self.date_edit_sampling.setGeometry(QtCore.QRect(1660, 100, 220, 30))
        self.date_edit_sampling.setObjectName("date_edit_sampling")
        self.label_specific_puirty = QtWidgets.QLabel(self.centralwidget)
        self.label_specific_puirty.setGeometry(QtCore.QRect(165, 210, 330, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(67, 173, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 173, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_specific_puirty.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_specific_puirty.setFont(font)
        self.label_specific_puirty.setAlignment(QtCore.Qt.AlignCenter)
        self.label_specific_puirty.setObjectName("label_specific_puirty")
        self.label_enumeration = QtWidgets.QLabel(self.centralwidget)
        self.label_enumeration.setGeometry(QtCore.QRect(810, 210, 330, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(67, 173, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 173, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_enumeration.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_enumeration.setFont(font)
        self.label_enumeration.setAlignment(QtCore.Qt.AlignCenter)
        self.label_enumeration.setObjectName("label_enumeration")
        self.label_germenation = QtWidgets.QLabel(self.centralwidget)
        self.label_germenation.setGeometry(QtCore.QRect(1480, 210, 330, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(67, 173, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 173, 97))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_germenation.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_germenation.setFont(font)
        self.label_germenation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_germenation.setObjectName("label_germenation")
        self.label_orge = QtWidgets.QLabel(self.centralwidget)
        self.label_orge.setGeometry(QtCore.QRect(160, 710, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_orge.setFont(font)
        self.label_orge.setObjectName("label_orge")
        self.label_avoine = QtWidgets.QLabel(self.centralwidget)
        self.label_avoine.setGeometry(QtCore.QRect(160, 750, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_avoine.setFont(font)
        self.label_avoine.setObjectName("label_avoine")
        self.label_triticale = QtWidgets.QLabel(self.centralwidget)
        self.label_triticale.setGeometry(QtCore.QRect(160, 790, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_triticale.setFont(font)
        self.label_triticale.setObjectName("label_triticale")
        self.input_winter_wheat = QtWidgets.QLineEdit(self.centralwidget)
        self.input_winter_wheat.setGeometry(QtCore.QRect(340, 670, 120, 25))
        self.input_winter_wheat.setObjectName("input_winter_wheat")
        self.output_winter_wheat = QtWidgets.QLabel(self.centralwidget)
        self.output_winter_wheat.setGeometry(QtCore.QRect(500, 670, 120, 25))
        self.output_winter_wheat.setFrameShape(QtWidgets.QFrame.Box)
        self.output_winter_wheat.setText("")
        self.output_winter_wheat.setObjectName("output_winter_wheat")
        self.output_orge = QtWidgets.QLabel(self.centralwidget)
        self.output_orge.setGeometry(QtCore.QRect(500, 710, 120, 25))
        self.output_orge.setFrameShape(QtWidgets.QFrame.Box)
        self.output_orge.setText("")
        self.output_orge.setObjectName("output_orge")
        self.input_orge = QtWidgets.QLineEdit(self.centralwidget)
        self.input_orge.setGeometry(QtCore.QRect(340, 710, 120, 25))
        self.input_orge.setObjectName("input_orge")
        self.output_avoine = QtWidgets.QLabel(self.centralwidget)
        self.output_avoine.setGeometry(QtCore.QRect(500, 750, 120, 25))
        self.output_avoine.setFrameShape(QtWidgets.QFrame.Box)
        self.output_avoine.setText("")
        self.output_avoine.setObjectName("output_avoine")
        self.input_avoine = QtWidgets.QLineEdit(self.centralwidget)
        self.input_avoine.setGeometry(QtCore.QRect(340, 750, 120, 25))
        self.input_avoine.setObjectName("input_avoine")
        self.output_triticale = QtWidgets.QLabel(self.centralwidget)
        self.output_triticale.setGeometry(QtCore.QRect(500, 790, 120, 25))
        self.output_triticale.setFrameShape(QtWidgets.QFrame.Box)
        self.output_triticale.setText("")
        self.output_triticale.setObjectName("output_triticale")
        self.input_triticale = QtWidgets.QLineEdit(self.centralwidget)
        self.input_triticale.setGeometry(QtCore.QRect(340, 790, 120, 25))
        self.input_triticale.setObjectName("input_triticale")
        self.label_other_plantes = QtWidgets.QLabel(self.centralwidget)
        self.label_other_plantes.setGeometry(QtCore.QRect(40, 890, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_other_plantes.setFont(font)
        self.label_other_plantes.setObjectName("label_other_plantes")
        self.radio_yes_other_plants = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_yes_other_plants.setGeometry(QtCore.QRect(270, 890, 82, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.radio_yes_other_plants.setFont(font)
        self.radio_yes_other_plants.setObjectName("radio_yes_other_plants")
        self.radio_no_other_plants = QtWidgets.QRadioButton(self.centralwidget)
        self.radio_no_other_plants.setGeometry(QtCore.QRect(420, 890, 82, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.radio_no_other_plants.setFont(font)
        self.radio_no_other_plants.setObjectName("radio_no_other_plants")
        self.label_other_plantes_total = QtWidgets.QLabel(self.centralwidget)
        self.label_other_plantes_total.setGeometry(QtCore.QRect(750, 280, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_other_plantes_total.setFont(font)
        self.label_other_plantes_total.setObjectName("label_other_plantes_total")
        self.label_winter_wheatD = QtWidgets.QLabel(self.centralwidget)
        self.label_winter_wheatD.setGeometry(QtCore.QRect(870, 350, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_winter_wheatD.setFont(font)
        self.label_winter_wheatD.setObjectName("label_winter_wheatD")
        self.label_orgeD = QtWidgets.QLabel(self.centralwidget)
        self.label_orgeD.setGeometry(QtCore.QRect(870, 390, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_orgeD.setFont(font)
        self.label_orgeD.setObjectName("label_orgeD")
        self.label_avoineD = QtWidgets.QLabel(self.centralwidget)
        self.label_avoineD.setGeometry(QtCore.QRect(870, 430, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_avoineD.setFont(font)
        self.label_avoineD.setObjectName("label_avoineD")
        self.label_triticaleD = QtWidgets.QLabel(self.centralwidget)
        self.label_triticaleD.setGeometry(QtCore.QRect(870, 470, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_triticaleD.setFont(font)
        self.label_triticaleD.setObjectName("label_triticaleD")
        self.output_other_plants_total = QtWidgets.QLabel(self.centralwidget)
        self.output_other_plants_total.setGeometry(QtCore.QRect(1040, 280, 120, 30))
        self.output_other_plants_total.setFrameShape(QtWidgets.QFrame.Box)
        self.output_other_plants_total.setText("")
        self.output_other_plants_total.setObjectName("output_other_plants_total")
        self.label_insects = QtWidgets.QLabel(self.centralwidget)
        self.label_insects.setGeometry(QtCore.QRect(750, 590, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_insects.setFont(font)
        self.label_insects.setObjectName("label_insects")
        self.label_graines_dures = QtWidgets.QLabel(self.centralwidget)
        self.label_graines_dures.setGeometry(QtCore.QRect(1430, 400, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_graines_dures.setFont(font)
        self.label_graines_dures.setObjectName("label_graines_dures")
        self.input_graines_dures = QtWidgets.QLineEdit(self.centralwidget)
        self.input_graines_dures.setGeometry(QtCore.QRect(1730, 400, 120, 30))
        self.input_graines_dures.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_graines_dures.setObjectName("input_graines_dures")
        self.input_graines_fraiches = QtWidgets.QLineEdit(self.centralwidget)
        self.input_graines_fraiches.setGeometry(QtCore.QRect(1730, 360, 120, 30))
        self.input_graines_fraiches.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_graines_fraiches.setObjectName("input_graines_fraiches")
        self.label_graines_fraiches = QtWidgets.QLabel(self.centralwidget)
        self.label_graines_fraiches.setGeometry(QtCore.QRect(1430, 360, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_graines_fraiches.setFont(font)
        self.label_graines_fraiches.setObjectName("label_graines_fraiches")
        self.input_graines_mortes = QtWidgets.QLineEdit(self.centralwidget)
        self.input_graines_mortes.setGeometry(QtCore.QRect(1730, 440, 120, 30))
        self.input_graines_mortes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_graines_mortes.setObjectName("input_graines_mortes")
        self.label_graines_mortes = QtWidgets.QLabel(self.centralwidget)
        self.label_graines_mortes.setGeometry(QtCore.QRect(1430, 440, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_graines_mortes.setFont(font)
        self.label_graines_mortes.setObjectName("label_graines_mortes")
        self.output_germination_total = QtWidgets.QLabel(self.centralwidget)
        self.output_germination_total.setGeometry(QtCore.QRect(1730, 500, 120, 30))
        self.output_germination_total.setFrameShape(QtWidgets.QFrame.Box)
        self.output_germination_total.setText("")
        self.output_germination_total.setObjectName("output_germination_total")
        self.label_germination_total = QtWidgets.QLabel(self.centralwidget)
        self.label_germination_total.setGeometry(QtCore.QRect(1430, 500, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_germination_total.setFont(font)
        self.label_germination_total.setObjectName("label_germination_total")
        self.button_calculate = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: calculate_it())
        self.button_calculate.setGeometry(QtCore.QRect(170, 950, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_calculate.setFont(font)
        self.button_calculate.setObjectName("button_calculate")
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(530, 950, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_reset.setFont(font)
        self.button_reset.setObjectName("button_reset")
        self.button_scan = QtWidgets.QPushButton(self.centralwidget)
        self.button_scan.setGeometry(QtCore.QRect(890, 950, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_scan.setFont(font)
        self.button_scan.setObjectName("button_scan")
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(1250, 950, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setObjectName("button_save")
        self.button_print = QtWidgets.QPushButton(self.centralwidget)
        self.button_print.setGeometry(QtCore.QRect(1610, 950, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.button_print.setFont(font)
        self.button_print.setObjectName("button_print")
        self.label_decision = QtWidgets.QLabel(self.centralwidget)
        self.label_decision.setGeometry(QtCore.QRect(850, 800, 671, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_decision.setFont(font)
        self.label_decision.setObjectName("label_decision")
        self.output_decision = QtWidgets.QLabel(self.centralwidget)
        self.output_decision.setGeometry(QtCore.QRect(1529, 800, 300, 40))
        self.output_decision.setFrameShape(QtWidgets.QFrame.Box)
        self.output_decision.setText("")
        self.output_decision.setObjectName("output_decision")
        self.comboBox_species = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_species.setGeometry(QtCore.QRect(950, 20, 220, 30))
        self.comboBox_species.setObjectName("comboBox_species")
        self.comboBox_species.addItem("")
        self.comboBox_species.addItem("")
        self.comboBox_species.addItem("")
        self.comboBox_species.addItem("")
        self.comboBox_species.addItem("")
        self.comboBox_variety = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_variety.setGeometry(QtCore.QRect(950, 60, 220, 30))
        self.comboBox_variety.setObjectName("comboBox_variety")
        self.comboBox_variety.addItem("")
        self.comboBox_variety.addItem("")
        self.comboBox_variety.addItem("")
        self.comboBox_variety.addItem("")
        self.comboBox_category = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_category.setGeometry(QtCore.QRect(950, 100, 220, 30))
        self.comboBox_category.setObjectName("comboBox_category")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.comboBox_category.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(890, 590, 271, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radio_yes_insects = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_yes_insects.setEnabled(True)
        self.radio_yes_insects.setObjectName("radio_yes_insects")
        self.horizontalLayout.addWidget(self.radio_yes_insects)
        self.radio_no_insects = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_no_insects.setObjectName("radio_no_insects")
        self.horizontalLayout.addWidget(self.radio_no_insects)
        self.label_total = QtWidgets.QLabel(self.centralwidget)
        self.label_total.setGeometry(QtCore.QRect(40, 840, 211, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total.setFont(font)
        self.label_total.setObjectName("label_total")
        self.output_total_weight = QtWidgets.QLabel(self.centralwidget)
        self.output_total_weight.setGeometry(QtCore.QRect(270, 840, 120, 25))
        self.output_total_weight.setFrameShape(QtWidgets.QFrame.Box)
        self.output_total_weight.setText("")
        self.output_total_weight.setObjectName("output_total_weight")
        self.output_total_percentage = QtWidgets.QLabel(self.centralwidget)
        self.output_total_percentage.setGeometry(QtCore.QRect(430, 840, 120, 25))
        self.output_total_percentage.setFrameShape(QtWidgets.QFrame.Box)
        self.output_total_percentage.setObjectName("output_total_percentage")
        self.spinBox_winter_wheat = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_winter_wheat.setGeometry(QtCore.QRect(270, 670, 42, 25))
        self.spinBox_winter_wheat.setObjectName("spinBox_winter_wheat")
        self.spinBox_orge = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_orge.setGeometry(QtCore.QRect(270, 710, 42, 25))
        self.spinBox_orge.setObjectName("spinBox_orge")
        self.spinBox_avoine = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_avoine.setGeometry(QtCore.QRect(270, 750, 42, 25))
        self.spinBox_avoine.setObjectName("spinBox_avoine")
        self.spinBox_triticale = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_triticale.setGeometry(QtCore.QRect(270, 790, 42, 25))
        self.spinBox_triticale.setObjectName("spinBox_triticale")
        self.spinBox_winter_wheatD = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_winter_wheatD.setGeometry(QtCore.QRect(1170, 350, 120, 30))
        self.spinBox_winter_wheatD.setObjectName("spinBox_winter_wheatD")
        self.spinBox_orgeD = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_orgeD.setGeometry(QtCore.QRect(1170, 390, 120, 30))
        self.spinBox_orgeD.setObjectName("spinBox_orgeD")
        self.spinBox_avoineD = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_avoineD.setGeometry(QtCore.QRect(1170, 430, 120, 30))
        self.spinBox_avoineD.setObjectName("spinBox_avoineD")
        self.spinBox_triticaleD = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_triticaleD.setGeometry(QtCore.QRect(1170, 470, 120, 30))
        self.spinBox_triticaleD.setObjectName("spinBox_triticaleD")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def test_it():
            seed = Seed(SeedCategory.CATEGORY_1)
            seed.pure_seeds = float(self.input_seed_purity.text())
            self.output_seed_purity.setText(f'{seed.pure_seeds}')

        def calculate_it():
            seed = Seed(SeedCategory.CATEGORY_1)
            seed.pure_seeds = float(self.input_seed_purity.text())
            seed.grains_multees = float(self.input_graines_mutilees.text())
            seed.debris_vegeteux = float(self.input_debris_vegetaux.text())
            seed.balles = float(self.input_balles.text())
            seed.terres = float(self.input_terres.text())
            seed.gravies = float(self.input_gravies.text())
            seed.other_im = float(self.input_autres.text())
            seed.winter_wheat_weight = float(self.input_winter_wheat.text())
            seed.barely_weight = float(self.input_orge.text())
            seed.oats_weight = float(self.input_avoine.text())
            seed.triticale_weight = float(self.input_triticale.text())
            print("test")
            successes = seed.calculate_purity_specific

            if successes:
                self.output_seed_purity.setText("{:.2f} %".format(seed.percentage[0]))
                self.output_inert_matter_total.setText("{:.2f} g".format(seed.output_weight[0]))
                self.output_inert_matter.setText("{:.2f} %".format(seed.percentage[1]))
                self.output_graines_mutilees.setText("{:.2f} %".format(seed.percentage[2]))
                self.output_Debris_Vegetaux.setText("{:.2f} %".format(seed.percentage[3]))
                self.output_balles.setText("{:.2f} %".format(seed.percentage[4]))
                self.output_terres.setText("{:.2f} %".format(seed.percentage[5]))
                self.output_gravies.setText("{:.2f} %".format(seed.percentage[6]))
                self.output_autres.setText("{:.2f} %".format(seed.percentage[7]))
                self.output_other_spacies_total.setText("{:.2f} g".format(seed.output_weight[1]))
                self.output_other_species.setText("{:.2f} %".format(seed.percentage[8]))
                self.output_winter_wheat.setText("{:.2f} %".format(seed.percentage[9]))
                self.output_orge.setText("{:.2f} %".format(seed.percentage[10]))
                self.output_avoine.setText("{:.2f} %".format(seed.percentage[11]))
                self.output_triticale.setText("{:.2f} %".format(seed.percentage[12]))
                self.output_total_weight.setText("{:.2f} g".format(seed.output_weight[2]))
                self.output_total_percentage.setText("{:.2f} %".format(seed.percentage[13]))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CNCC "))
        self.label_sample_code.setText(_translate("MainWindow", "N° du lot"))
        self.label_code_etablissement.setText(_translate("MainWindow", "Code etablissement"))
        self.label_weight.setText(_translate("MainWindow", "poids du lot"))
        self.label_date_reception.setText(_translate("MainWindow", "Date de reception"))
        self.label_species.setText(_translate("MainWindow", "Espéce"))
        self.label_variety.setText(_translate("MainWindow", "Varieté"))
        self.label_category.setText(_translate("MainWindow", "Category"))
        self.label_sample_weight.setText(_translate("MainWindow", "Poids de l\'echontillon (g)"))
        self.label_seed_purity.setText(_translate("MainWindow", "Semance pures"))
        self.label_inert_matter.setText(_translate("MainWindow", "Matiers inertes"))
        self.label_grains_mutilees.setText(_translate("MainWindow", "Graines mutilées (g)"))
        self.label_debris_vegetaux.setText(_translate("MainWindow", "Debris Végetaux (g)"))
        self.label_balles.setText(_translate("MainWindow", "Balles (g)"))
        self.label_terres.setText(_translate("MainWindow", "Terres (g)"))
        self.label_gravies.setText(_translate("MainWindow", "Gravies (g)"))
        self.label_autres.setText(_translate("MainWindow", "Autres (g)"))
        self.label_other_species.setText(_translate("MainWindow", "Semences d’autres espèces"))
        self.label_winter_wheat.setText(_translate("MainWindow", "Blé tendre"))
        self.label_analyse_id.setText(_translate("MainWindow", "N° Analyse"))
        self.label_year_haverst.setText(_translate("MainWindow", "Année Recolte"))
        self.label_date_sampling.setText(_translate("MainWindow", "Date Prélévement"))
        self.label_specific_puirty.setText(_translate("MainWindow", "Analyse de la pureté specifique"))
        self.label_enumeration.setText(_translate("MainWindow", "Analyse de denombrement"))
        self.label_germenation.setText(_translate("MainWindow", "Le test de germination"))
        self.label_orge.setText(_translate("MainWindow", "Orge"))
        self.label_avoine.setText(_translate("MainWindow", "Avoine"))
        self.label_triticale.setText(_translate("MainWindow", "Triticale"))
        self.label_other_plantes.setText(_translate("MainWindow", "Semences autres plantes"))
        self.radio_yes_other_plants.setText(_translate("MainWindow", "YES"))
        self.radio_no_other_plants.setText(_translate("MainWindow", "NO"))
        self.label_other_plantes_total.setText(_translate("MainWindow", "Semances autres espéces"))
        self.label_winter_wheatD.setText(_translate("MainWindow", "Blé tendre"))
        self.label_orgeD.setText(_translate("MainWindow", "Orge"))
        self.label_avoineD.setText(_translate("MainWindow", "Avoine"))
        self.label_triticaleD.setText(_translate("MainWindow", "Triticale"))
        self.label_insects.setText(_translate("MainWindow", "Insects"))
        self.label_graines_dures.setText(_translate("MainWindow", "Graines Dures"))
        self.label_graines_fraiches.setText(_translate("MainWindow", "Grain Fraiches"))
        self.label_graines_mortes.setText(_translate("MainWindow", "Graines Mortes"))
        self.label_germination_total.setText(_translate("MainWindow", "TOTAL (%)"))
        self.button_calculate.setText(_translate("MainWindow", "Calculate"))
        self.button_calculate.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))
        self.button_reset.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.button_scan.setText(_translate("MainWindow", "Scan"))
        self.button_scan.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.button_save.setText(_translate("MainWindow", "Save"))
        self.button_save.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.button_print.setText(_translate("MainWindow", "Print"))
        self.button_print.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.label_decision.setText(_translate("MainWindow", "Décision du service de contrôle et certification des semence"))
        self.comboBox_species.setItemText(0, _translate("MainWindow", "Blé dur"))
        self.comboBox_species.setItemText(1, _translate("MainWindow", "Blé tendre"))
        self.comboBox_species.setItemText(2, _translate("MainWindow", "Orge"))
        self.comboBox_species.setItemText(3, _translate("MainWindow", "Avoine"))
        self.comboBox_species.setItemText(4, _translate("MainWindow", "Triticale"))
        self.comboBox_variety.setItemText(0, _translate("MainWindow", "Bousselam"))
        self.comboBox_variety.setItemText(1, _translate("MainWindow", "Vitron"))
        self.comboBox_variety.setItemText(2, _translate("MainWindow", "GTA"))
        self.comboBox_variety.setItemText(3, _translate("MainWindow", "Oued el Bared"))
        self.comboBox_category.setItemText(0, _translate("MainWindow", "PreBase (G1,G2,G3)"))
        self.comboBox_category.setItemText(1, _translate("MainWindow", "Base(G4)"))
        self.comboBox_category.setItemText(2, _translate("MainWindow", "Reproduction(R1,R2,R3)"))
        self.comboBox_category.setItemText(3, _translate("MainWindow", "Ordinaire"))
        self.radio_yes_insects.setText(_translate("MainWindow", "YES"))
        self.radio_no_insects.setText(_translate("MainWindow", "NO"))
        self.label_total.setText(_translate("MainWindow", "TOTAL"))
        self.input_seed_purity.setText("0")
        self.input_graines_mutilees.setText("0")
        self.input_debris_vegetaux.setText("0")
        self.input_balles.setText("0")
        self.input_terres.setText("0")
        self.input_gravies.setText("0")
        self.input_autres.setText("0")
        self.input_winter_wheat.setText("0")
        self.input_orge.setText("0")
        self.input_avoine.setText("0")
        self.input_triticale.setText("0")
        # self.output_total_percentage.setText(_translate("MainWindow", "100%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
