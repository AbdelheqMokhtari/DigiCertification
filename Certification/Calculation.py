from enum import Enum


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
        # self.seed_category = SeedCategory.CATEGORY_1

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

    @property
    def calculate_purity_specific(self):
        self.calculate_sum_and_set_other_species()
        self.calculate_sum_and_set_inert_matter()
        self.calculate_sum_and_set_total_seed()
        self.calculate_percentage()
        self._state = self.output_total_specific_purity
        self.take_decision(0)
        self.seed_category_update(0)
        return self._state
        # return self._percentage

    @property
    def calculate_enumeration(self):
        self._state = self.calculate_total
        self.take_decision(1)
        self.seed_category_update(1)
        return self._state


seed = Seed(SeedCategory.CATEGORY_1)

print("the initial category of this simple :", seed.seed_category)

print("\n** 120g Analyse **\n")

print("--Pure seeds--\n")
seed.pure_seeds = float(input("semences pures (g) :"))

print("\n--matiere inertes--\n")
seed.grains_multees = float(input("Grains mutilées (g) :"))
seed.debris_vegeteux = float(input("Debris vegéteux (g) :"))
seed.balles = float(input("balles (g) :"))
seed.terres = float(input("Terres (g) :"))
seed.gravies = float(input("Gravies (g) :"))
seed.other_im = float(input("autres (g) :"))

print("\n--other species--\n")

seed.winter_wheat = int(input("Number of winter wheat in 120g sample size # :"))
seed.winter_wheat_weight = float(input("winter wheat (g) :"))

seed.barely = int(input("Number of barely in 120g sample size # :"))
seed.barely_weight = float(input("barely (g) :"))

seed.oats = int(input("Number of oats in 120g sample size # :"))
seed.oats_weight = float(input("oats (g) :"))

seed.triticale = int(input("Number of triticale in 120g sample size # :"))
seed.triticale_weight = float(input("triticale (g) :"))

print("\n** 120g Results **\n")
successes = seed.calculate_purity_specific

if successes:
    print("1) Semences pure :")
    print("\tSemences pures (g) = {:.2f} g".format(seed.pure_seeds))
    print("\tSemences pures % = {:.2f} %".format(seed.percentage[0]))
    print("\n2) Matiers inertes :")
    print("\n\t\tMatiers inertes (g) = {:.2f} g".format(seed.output_weight[0]))
    print("\t\tMatiers inertes % = {:.2f} %".format(seed.percentage[1]))
    print("\n\t\t\tGrains Multées (g) = {:.2f} g".format(seed.grains_multees))
    print("\t\t\tGrains Multées % = {:.2f} %".format(seed.percentage[2]))
    print("\n\t\t\tDebris vegetaux (g) = {:.2f} g".format(seed.debris_vegeteux))
    print("\t\t\tDebris vegetaux % = {:.2f} %".format(seed.percentage[3]))
    print("\n\t\t\tBalles (g) = {:.2f} g".format(seed.balles))
    print("\t\t\tBalles % = {:.2f} %".format(seed.percentage[4]))
    print("\n\t\t\tTerres (g) = {:.2f} g".format(seed.terres))
    print("\t\t\tTerres % = {:.2f} %".format(seed.percentage[5]))
    print("\n\t\t\tGravies (g) = {:.2f} g".format(seed.gravies))
    print("\t\t\tGravies % = {:.2f} %".format(seed.percentage[6]))
    print("\n\t\t\tAutres (g) = {:.2f} g".format(seed.other_im))
    print("\t\t\tAutres % = {:.2f} %".format(seed.percentage[7]))
    print("\n3) Semences d'autres plantes:")
    print("\n\t\tSemences d'autres plantes (g) = {:.2f} g".format(seed.output_weight[1]))
    print("\t\tSemences d'autres plantes % = {:.2f} %".format(seed.percentage[8]))
    print("\n\t\t\tBle tendre (g) = {:.2f} g".format(seed.winter_wheat_weight))
    print("\t\t\tBle tendre = ", seed.winter_wheat)
    print("\t\t\tBle tendre % = {:.2f} %".format(seed.percentage[9]))
    print("\n\t\t\tOrge (g) = {:.2f} g".format(seed.barely_weight))
    print("\t\t\tOrge = ", seed.barely)
    print("\t\t\tOrge % = {:.2f} %".format(seed.percentage[10]))
    print("\n\t\t\tAvoine (g) = {:.2f} g".format(seed.oats_weight))
    print("\t\t\tAvoine = ", seed.oats)
    print("\t\t\tAvoine % = {:.2f} % ".format(seed.percentage[11]))
    print("\n\t\t\tTriticale (g) = {:.2f} g".format(seed.triticale_weight))
    print("\t\t\tTriticale = ", seed.triticale)
    print("\t\t\tTriticale % = {:.2f} %".format(seed.percentage[12]))
    print("\nTotal :")
    print("\t\tTotal weight for analyse of specific purity = {:.2f} g".format(seed.output_weight[2]))
    print("\t\tTotal Percentage = ", int(seed.percentage[13]), "%")
    print("\n\t\tThe Decision of this sample after the 120 G analyse : ", seed.seed_decision)
    print("\t\tThe category of this sample after the 120 G analyse : ", seed.seed_category)

print("\n** enumeration in 380g  **\n")
seed.winter_wheat = int(input("Number of winter wheat in 380g sample size # :"))
seed.barely = int(input("Number of barely in 380g sample size # :"))
seed.oats = int(input("Number of oats in 380g sample size # :"))
seed.triticale = int(input("Number of triticale in 380g sample size # :"))

print("\n** 500g Results **\n")
successes = seed.calculate_enumeration
if successes:
    print("Number total of winter wheat in 500g : ", seed.winter_wheat)
    print("Number total of barely in 500g : ", seed.barely)
    print("Number total of oats in 500g : ", seed.oats)
    print("Number total of triticale in 500g : ", seed.triticale)
    print("\ntotal number of other species in the sample : ", seed.total)
    print("\n\t\tThe Decision of this sample after the 380 G enumeration analyse : ", seed.seed_decision)
    print("\t\tThe category of this sample after the 380 G enumeration analyse : ", seed.seed_category)
