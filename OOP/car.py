class Car:
    # top_speed = 100

    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed,
        self.warnings = []

    def drive(self):
        print('I am driving but certaninly not faster than {}'.format(self.top_speed))

car1 = Car()
car1.drive()

# car1.top_speed = 200
car1.warnings.append('New warning')
car1.drive()

car2 = Car()
car2.drive()