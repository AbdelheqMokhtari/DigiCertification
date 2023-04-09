from enum import Enum


class SeedCategory(Enum):
    CATEGORY_1 = "Base"
    CATEGORY_2 = "Reproduction"
    CATEGORY_3 = "Ordinary"
    CATEGORY_4 = "Refused"


class Seed:
    def __init__(self, category, pure_seeds=None, inert_matter=None, other_species=None):
        if isinstance(category, SeedCategory):
            self.category = category
        else:
            raise ValueError("Invalid Category")

        # self.seed_category = seed_category
        self.pure_seeds = pure_seeds
        self.total_seeds = 0
        self.inert_matter = inert_matter
        self.other_species = other_species
        # self.seed_category = SeedCategory.CATEGORY_1

    @property
    def purity_percentage(self):
        self.total_seeds = self.pure_seeds + self.inert_matter + self.other_species
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
    def pure_seeds(self):
        return self.pure_seeds

    def pure_seeds(self, value):
        self.pure_seeds = value

    @property
    def inert_matter(self):
        return self.inert_matter

    def inert_matter(self, value):
        self.inert_matter = value

    @property
    def other_species(self):
        return self.other_species

    def other_species(self, value):
        self.other_species = value

    @property
    def seed_category(self):
        return self.category.value


seed = Seed(SeedCategory.CATEGORY_1)
seed.pure_seeds = float(input("semences pures (g) :"))
seed.inert_matter = float(input("matiers inertes (g) :"))
seed.other_species = float(input("Semance d'autre plants (g) :"))
print(seed.seed_category)
print(seed.purity_percentage)  # Output: 97.5
seed.seed_category_update
# print(seed.seed_category_update.value)  # Output: Ordinary
print(seed.seed_category)

