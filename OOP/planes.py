conntrol_tower_loaction = (4,4)
import random
class NormalPlanes:
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
    print('this wont print if the file was imported')

if __name__ == '__main__':
    main()
    
