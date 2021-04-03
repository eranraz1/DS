from typing import NewType


def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="Eran")



numbers = (1, 2, 3, 4)
result = map(lambda x : x+1 , numbers)
print (list(result))

numbers1 = [1, 2, 3, 10]
numbers2 = [4, 5, 6,]
  
result = map(lambda x, y : x + y , numbers1, numbers2)
print(list(result))

a = 5+3 + 4 \
    + 2000
print(a)


def wage(w_hours):
    pay = w_hours*25
    return pay

def bonus(w_hours):
    if w_hours > 160:
        pay = wage(w_hours)*1.05
    else: 
        pay = wage(w_hours)
    return pay


def square(x):
    return x*x
def cube(x):
    return x**3

f = square
def my_map(func,arg_list):
    new_list= []
    for i in arg_list:
        new_list.append(func(i))
    return new_list

lista = [1,2,3,4,5,9]
print(my_map(square,lista))
print(my_map(cube,lista))


def logger(msg):
    def log_msg():
        print (f'Log: {msg}')
    return log_msg

log_hi = logger ('hi')
print(log_hi)
print(logger ('hi'))
log_hi()

def html_tag(tag):
    def wrapper(msg):
        print(f'<tag><msg></tag>')

