class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def introduce(self):
        print("Hi")
        print("I am a " + self.breed + " dog.")
        print("I am " + str(self.age) + " years old")
        print("I am " + self.color + " in color")

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def bark(self):
        print('Woof woof')
    
    def sleep(self):
        print('Zzzzzz')
    
    def eat(self):
        print('i am eating')
    
    def run(self, speed):
        print('I am', self.name)
        print('Okay, i will run in', str(speed), 'km/hr')
        print()

dog = Dog('dechen', 'bhutanese', 20, 'black')
petdog = Dog('dorji', 'pug', 10, 'white')
my_friend_dog = Dog('tashi', 'german shephard', 15, 'brown')

how_fast_should_dog_run = 1000
dog.run(10)
dog.run(100)
dog.run(how_fast_should_dog_run)
petdog.run(20)
