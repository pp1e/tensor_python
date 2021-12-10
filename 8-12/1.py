class Animals:
    def __init__(self, name, kind, gender, weight):
        self.name = name
        self.kind = kind
        self.gender = gender
        self.weight = weight

    def move(self, distantion, direction):
        print(self.name + ' moved ' + distantion + ' to the ' + direction)

    def eat(self, food):
        print(self.name + ' ate ' + food)


class Mammals(Animals):
    def __init__(self, name, kind, gender, weight, coat_color):
        super().__init__(name, kind, gender, weight)
        self.coat_color = coat_color

    def hunt(self):
        print(self.name + ' is hunting...')

class Human(Mammals):
    def __init__(self, name, kind, gender, weight, coat_color, eyes_color, profession):
        super().__init__(name, kind, gender, weight, coat_color)
        self.eyes_color = eyes_color
        self.profession = profession

    def think(self):
        print(self.name + ' is thinking...')

class Dog(Mammals):
    def __init__(self, name, kind, gender, weight, coat_color, owner):
        super().__init__(name, kind, gender, weight, coat_color)
        self.owner = owner

    def play(self):
        print(self.name + ' is playing with its owner ' + self.owner)

class Cat(Mammals):
    def __init__(self, name, kind, gender, weight, coat_color, favorite_toy):
        super().__init__(name, kind, gender, weight, coat_color)
        self.favorite_toy = favorite_toy

    def jump(self):
        print(self.name + 'jumped from balcony and she is totally ok :o')

class Student(Human):
    def __init__(self, name, kind, gender, weight, coat_color, eyes_color, profession, hw_count):
        super().__init__(name, kind, gender, weight, coat_color, eyes_color, profession)
        self.hw_count = hw_count

    def study(self):
        print(self.name + ' is studing...')

    def __cmp__(self, student):
        return self.hw_count - student.hw_count

    def __eq__(self, student):
        return self.hw_count == student.hw_count

croc = Animals('Gena', 'Crocodile', 'Male', 80)
croc.eat('Cheburashka')

tiger = Mammals('Vasya', 'Tiger', 'Male', 100, 'Orange')
tiger.eat('Goat')
tiger.hunt()

human = Human('Pasha', 'Human', 'Male', 70, 'Brown', 'Blue', 'Engeener')
human.think()

cat = Cat('Murzik', 'Cat', 'Female', 7, 'Grey', 'Ball')
cat.jump()

dog = Dog('Richard', 'Dog', 'Male', 9, 'Ginger', 'Denis')
dog.play()

stud1 = Student('Zhenya', 'Human', 'Male', 65, 'Blond', 'Brown', 'Student', 10)
stud2 = Student('Matvey', 'Human', 'Male', 75, 'Brown', 'Blue', 'Programmer', 12)

print(stud1 == stud2)
print(stud1 > stud2)
print(stud1 < stud2)