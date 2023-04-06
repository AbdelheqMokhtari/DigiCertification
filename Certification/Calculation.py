from enum import Enum


class SeedCategory(Enum):
    CATEGORY_1 = "Base"
    CATEGORY_2 = "Reproduction"
    CATEGORY_3 = "Ordinary"
    CATEGORY_4 = "Refused"


class Seed:
    def __init__(self, category, pure_seeds, total_seeds):
        if isinstance(category, SeedCategory):
            self.category = category
        else:
            raise ValueError("Invalid color")

        # self.seed_category = seed_category
        self.pure_seeds = pure_seeds
        self.total_seeds = total_seeds
        # self.seed_category = SeedCategory.CATEGORY_1

    @property
    def purity_percentage(self):
        return (self.pure_seeds / self.total_seeds) * 100

    @property
    def seed_category(self):

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


seed = Seed(SeedCategory.CATEGORY_1, 195, 200)
print(seed.purity_percentage)  # Output: 95.0
print(seed.seed_category.value)  # Output: Category 1
