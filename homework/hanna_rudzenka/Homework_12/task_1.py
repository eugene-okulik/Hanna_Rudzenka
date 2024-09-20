class Flowers:
    def __init__(self, lifespan, color, stem_length, cost, freshness):
        self.lifespan = lifespan
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.freshness = freshness

    def __str__(self):
        return (
            f"{self.__class__.__name__}(lifespan={self.lifespan}, color={self.color}, stem_length={self.stem_length}"
            f", cost={self.cost}, freshness={self.freshness})"
        )

    def __repr__(self):
        return self.__str__()


class Rose(Flowers):
    def __init__(self, lifespan, color, stem_length, cost, freshness):
        super().__init__(lifespan, color, stem_length, cost, freshness)


rose1 = Rose(7, 'red', 10, 2, 5)
rose2 = Rose(5, 'white', 15, 1.5, 4)


class Tulip(Flowers):
    def __init__(self, lifespan, color, stem_length, cost, freshness):
        super().__init__(lifespan, color, stem_length, cost, freshness)


tulip1 = Tulip(8, 'yellow', 12, 2, 6)
tulip2 = Tulip(3, 'pink', 11, 1, 5)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers_to_list(self, flower):
        self.flowers.append(flower)

    def average_bouquet_lifespan(self):
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def check_bouquet_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def sort_by(self, parameter):
        return sorted(self.flowers, key=lambda flower: getattr(flower, parameter))

    def search_flower_by_cost(self, cost):
        return [flower for flower in self.flowers if flower.cost < cost]
