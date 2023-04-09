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
            raise ValueError("Invalid color")

        # self.seed_category = seed_category
        self.pure_seeds = None
        self.total_seeds = None
        # self.seed_category = SeedCategory.CATEGORY_1

    @property
    def purity_percentage(self):
        return (self.pure_seeds / self.total_seeds) * 100

    @property
    def seed_category_update(self):

        purity = self.purity_percentage
        category = self.category

        if self.category == SeedCategory.CATEGORY_1:
            if purity >= 99:
                return SeedCategory.CATEGORY_1
            elif purity >= 98:
                return SeedCategory.CATEGORY_2
            elif purity >= 97:
                return SeedCategory.CATEGORY_3
            else:
                return SeedCategory.CATEGORY_4

        elif category == SeedCategory.CATEGORY_2:
            if purity >= 98:
                return SeedCategory.CATEGORY_2
            elif purity >= 97:
                return SeedCategory.CATEGORY_3
            else:
                return SeedCategory.CATEGORY_4

        elif category == SeedCategory.CATEGORY_3:
            if purity >= 97:
                return SeedCategory.CATEGORY_3
            else:
                return SeedCategory.CATEGORY_4
        else:
            return SeedCategory.CATEGORY_4

    def pure_seeds(self):
        return self.pure_seeds

    def pure_seeds(self, value):
        self.pure_seeds = value

    def total_seeds(self):
        return self.total_seeds

    def total_seeds(self, value):
        self.total_seeds = value


seed = Seed(SeedCategory.CATEGORY_2)
seed.total_seeds = 200
seed.pure_seeds = 200
print(seed.purity_percentage)  # Output: 97.5
print(seed.seed_category_update.value)  # Output: Ordinary
