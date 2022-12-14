import random
class Character:
    def __init__(self, name, race, c_class, color, stats):
        self.name = name = input("Please enter a nmae for your character")
        self.race = race
        self.c_class = c_class
        self.color = color
        self.stats = stats
        
        
    def pick_race(self):
        race_list = ["Human", "Orc", "Elf"]
        
        while True:
            inp = input("Pick your race: 1: Human, 2: Orc, 3: Elf")
            if inp == "1":
                self.race = race_list[0]
                break
            elif inp == "2":
                self.race = race_list[1]
                break
            elif inp == "3":
                self.race = race_list[2]
                break
            else:
                print("Invalid input")
                
    def pick_class(self):
        class_list = ["Warrior", "Mage", "Rogue"]
        while True:
            inp = input("Pick your class: 1: Warrior, 2: Mage, 3: Rogue")
            if inp == "1":
                self.c_class = class_list[0]
                break
            elif inp == "2":
                self.c_class = class_list[1]
                break
            elif inp == "3":
                self.c_class = class_list[2]
                break
            else:
                print("Invalid input")
                
                
    def pick_color(self):
        color_list = ["Black", "Red", "Green"]
        while True:
            inp = input("Pick your color: 1: Black, 2: Red, 3: Green")
            if inp == "1":
                self.color = color_list[0]
                break
            elif inp == "2":
                self.color = color_list[1]
                break
            elif inp == "3":
                self.color = color_list[2]
                break
            else:
                print("Invalid input")
                
    def generate_stats(self):
        self.stats = {"Strength": random.randint(10,15), "Agility": random.randint(10,15), "Health": 100}
        print(self.stats)
        if self.stats["Strength"] >= 13:
            print("Bigger")
            self.stats["Agility"] -= 2
            self.stats["Health"] += 50
        
                
                
char_1 = Character("a","x","y","z",{})
char_1.pick_race()
char_1.pick_class()
char_1.pick_color()
char_1.generate_stats()




print(f"Congratulations {char_1.name}, you created your character! It seems a good combination! A {char_1.color} {char_1.race} {char_1.c_class} seems really powerful!")
print(f"Your stats are : {char_1.stats}")
print(char_1.stats)



              
