# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:47:14 2021

@author: eranra
"""
import random
class CrazyPlan:
    def __init__(self):
        self.__x = 0
        self.__y = 0
    def update_position(self):
        self.__x += random.randint(-1,1)
        self.__y += random.randint(-1,1)
    def get_position(self):
        return self.__x, self.__y
        print('main ran')
    
plane1 = CrazyPlan()
plane1.__x, plane1.__y= plane1.get_position()
x1,y1 = plane1.get_position()


print(x1,y1)
plane1.update_position()
x1,y1 = plane1.get_position()
print(x1,y1)


class Frog:
    def __init__ (self):
        self.age = 0
        self.name = 'Kermit'
    def aging(self):
        self.age  += 1
        
kiko = Frog()
kiko.name
kiko.age
kiko.aging()
dir(kiko)
