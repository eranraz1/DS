#import planes as p
from planes import NormalPlanes
def main():
    plane11 = NormalPlanes()
    plane11.set_position(3,4)
    print(plane11.get_position())
if __name__ == '__main__':
    main()

plane11 = NormalPlanes()
plane11.set_position(3,4)
print(plane11.get_position())
print(plane11.__str__)  
plane11.__repr__  

'''
####################################################################
conntrol_tower_loaction = (4,4)
import random
class CrazyPlan:
    def __init__(self):
        self.__x = 0
        self.__y = 0
    def update_position(self):
        self.__x += random.randint(-1,1)
        self.__y += random.randint(-1,1)
    def get_position(self):
        print('main ran')
        return self.__x, self.__y
        
    def set_position(self,x,y):
        if (x,y) == conntrol_tower_loaction:
            print('location of the tower')
        elif x < 0 or y < 0:
            print('illigal location')
        else:
            self.__x =x
            self.__y =y
            print('position set')
            return self.__x, self.__y
        
def main():  
    plane1 = CrazyPlan()
    plane1.__x = 5 
    plane1.__y = 5
    print(plane1.__y)
    print(plane1.get_position())
    
main()

plane1.get_position()

plane2  = CrazyPlan()
plane2.get_position()
plane2.set_position(2, 3)



plane1.__x = 5 
print(plane1.get_position())

print(x1,y1)
plane1.update_position()
x1,y1 = plane1.get_position()
print(x1,y1)
'''

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
