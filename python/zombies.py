class Survivor:
    def __init__(self, name, wounds = 0):
        self.name = name
        self.wounds = wounds
        self.alive = True
        self.actions = 3
    def gets_hurt(self, num_of_wounds):
        if self.wounds + num_of_wounds >= 2:
            self.alive = False
            self.wounds = 2
        else:
            self.wounds += num_of_wounds
    def act(self):
        self.actions -= 1

