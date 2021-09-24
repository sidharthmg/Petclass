from random import randrange

user_pets = []

class Pet:
    boredom_decrement = 4
    hunger_decrement = 6
    boredom_threshold = 10
    hunger_threshold = 10
    sounds = ['Woof',"Meow"]
    def _init_(self, name,type):
        self.name = name
        self.type=type
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def currentmood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.boredom >= self.boredom_threshold and self.hunger >= self.hunger_threshold:
            return "hungry & bored"
        elif self.boredom <= self.boredom_threshold and self.hunger >= self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def _str_(self) -> str:
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.currentmood() + ". "
        return state

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def teach(self,word):
        self.sounds.append(word)
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

class Dog1(Pet):
        def _init_(self):
            print("Dog 1 created")

class Dog2(Pet):
        sounds = ["Woof", "ruff ruff"]

        def _init_(self):
            print("Dog 2 created")

class Dog3(Dog1, Dog2):
        def _init_(self):
            Dog1._init_(self)
            Dog2._init_(self)
            print("Dog 3 created")
class Cat(Pet):

        def _init_(self):
            print("Cat created")

def display_user_pets():
    print("Your Pets")
    for pet in user_pets:
        print(f"\n{pet}")


p1 = Dog1()
p2 = Dog2()
p3 = Dog3()
c1 = Cat()
print("Welcome")
game_on = True
while game_on:
    if len(user_pets) == 0:
        print("\nNo Pets!")
        name = input("Enter the name of your pet: ")
        type = input("Enter the type of the pet: ")
        user_pets.append(Pet(name,type))
    print("1.Display pets\n2.Adopt a Pet\n3.Greet\n4.Teach\n5.Feed\n6.Exit")
    user_choice = int(input("Enter your choice(1-6):"))
    print(user_choice)
    if user_choice == 1:
        display_user_pets()
    elif user_choice == 2:
        print("\nAdopting a new pet!")
        name = input("Enter the name of your pet: ")
        type = input("Enter the type of the pet: ")
        user_pets.append(Pet(name, type))
    elif user_choice in range(2, 6):
        name = input("Enter the name of pet you want to interact with: ")
        pet_exists = False
        for pet in user_pets:
            if pet.name == name:
                if user_choice == 3:
                    pet.hi()
                elif user_choice == 4:
                    word = input("Enter the word you want to teach: ")
                    pet.teach(word)
                elif user_choice == 5:
                    pet.feed()
                pet_exists = True
                pet.clock_tick()
        if pet_exists == False:
            print(f"You don't have a pet with the name {name}")
    else:
        game_on = False