import random
class CrazyPlan:
    def __init__(self):
        self.x = 0
        self.y = 0
    def update_position(self):
        self.x += random.randint(-1,1)
        self.y += random.randint(-1,1)
    def get_position(self):
        return self.x, self.y
    

plane1 = CrazyPlan()

xpos1,ypos1 = plane1.get_position()


lst = [2,3]
def func():
    print('func ran')
    global lst
    lst = [2,3,4]
func()
print (lst)


