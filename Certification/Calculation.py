from enum import Enum


class SeedCategory(Enum):
    CATEGORY_1 = "Base"
    CATEGORY_2 = "Reproduction"
    CATEGORY_3 = "Ordinary"
    CATEGORY_4 = "Refused"


class Seed:
    def __init__(self, category):
        if isinstance(category, SeedCategory):
            self.category = category
        else:
            raise ValueError("Invalid Category")

        # self.seed_category = seed_category
        self._pure_seeds = None
        self._other_species = None
        self._grains_multees = None
        self._debris_vegeteux = None
        self._balles = None
        self._terres = None
        self._gravies = None
        self._other_im = None
        self._inert_matter = None
        self._total_seeds = None
        # self.seed_category = SeedCategory.CATEGORY_1

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
    def purity_percentage(self):
        seed.calculate_sum_and_set_inert_matter()
        self.total_seeds = self.pure_seeds + self.other_species + self.inert_matter
        if self.total_seeds == 0:
            return 0
        return (self.pure_seeds / self.total_seeds) * 100

    @property
    def seed_category_update(self):

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

    @property
    def seed_category(self):
        return self.category.value


seed = Seed(SeedCategory.CATEGORY_2)
seed.pure_seeds = float(input("semences pures (g) :"))
print("--matiere inertes--")
seed.grains_multees = float(input("Grains mutilées (g) :"))
seed.debris_vegeteux = float(input("Debris vegéteux (g) :"))
seed.balles = float(input("balles (g) :"))
seed.terres = float(input("Terres (g) :"))
seed.gravies = float(input("Gravies (g) :"))
seed.other_im = float(input("autres (g) :"))
seed.other_species = float(input("Semance d'autre plants (g) :"))
print(seed.seed_category)
print(seed.purity_percentage)  # Output: 97.5
seed.seed_category_update
# print(seed.seed_category_update.value)  # Output: Ordinary
print(seed.seed_category)

