class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider


class Rider:
    def __init__(self, name):
        self.name = name


take = Rider("Take Yutaka")
deep_impact = Horse("DeepImpact", take)

print(deep_impact.rider.name)
