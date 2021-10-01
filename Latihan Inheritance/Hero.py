import os
# nilai tetap jika tidak ada kategori Hero`
class Hero:
    def __init__(self, name):
        self.health_point = [0, 1305, 2135, 4021, 5961]
        self.attPower_point = [0, 20, 45, 75, 90]
        self.armor_point = [0, 15, 30, 72, 100, 120]
        self.__name = name
        self.__exp = 0
        self.__level = 0
    
    def view_info(self):
        print("{}\n\t Level: {}\n\t Health: {}\n\t Attack Power: {}\n\tArmor: {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__power,
            self.__armor
            )
        )
     
    @property
    def health_point(self):
        pass
    @property
    def attPower_point(self):
        pass
    @property
    def armor_point(self):
        pass
    @property
    def levelUp(self):
        pass
    @property
    def gainExp(self):
        pass

    @health_point.setter
    def health_point(self, input):
        self.__health_point = input
    @attPower_point.setter
    def attPower_point(self, input):
        self.__attPower_point = input
    @armor_point.setter
    def armor_point(self, input):
        self.__armor_point = input        

    @gainExp.setter
    def gainExp(self, input):
        self.__exp = input
        if(self.__exp > 100):
            self.levelUp = self.__exp // 100
            self.__exp %= 100
    @levelUp.setter
    def levelUp(self, input):
        self.__level += input
        self.__health = self.__health_point[self.__level]
        self.__power = self.__attPower_point[self.__level]
        self.__armor = self.__armor_point[self.__level]

class HeroAgility(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.health_point = [0, 1200, 2100, 4135, 5000]
        self.attPower_point = [0, 10, 25, 30, 45]
        self.armor_point = [0, 12, 20, 30, 50]
        self.levelUp = 1

class HeroIntelligent(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.health_point = [0, 1000, 1500, 3200, 4725]
        self.attPower_point = [0, 15, 35, 60, 75]
        self.armor_point = [0, 5, 15, 25, 45]
        self.levelUp = 1
        