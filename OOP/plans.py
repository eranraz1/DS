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
def main():
    print('this wont print if the file was imported')

if __name__ == '__main__':
    main()
    
