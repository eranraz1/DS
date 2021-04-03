import os 
print(os.getcwd())
def func1(f):
    print('this is func1')
    f()
def func2():
    print('this is func2')

func1(func2)


def f1(func):
    def wrapper(*args,**kwargs):
        print('f1 start')
        func(*args, **kwargs)
        print('f1 end')
    return wrapper
@f1
def f2(name, last):
    print(f'f2 exec from {name} ,{last}')
f2('Eran', 'Raz')

def adding(num1, num2):
    return num1+ num2


### timer decorator
import time 
def timer(func):
  def wrapper(*args, **kwargs):
      start = time.time()
      func(*args, **kwargs)
      end = time.time()
      gap = end - start
      print (f'duration: {gap}')
  return wrapper    
    
@timer
def test_func():
    time.sleep(3)
    print('slept')

test_func()
    
  
### logger

import datetime
def logger(func):
    def wrapper(*args, **kwargs):
        with open ('log.txt','a') as logi:
            logi.write(f'called function {func} with' + ''.join([str(i) for i in args])+ 'at ' + str(datetime.datetime.now())+ '\n')
        return func(*args, **kwargs)
        print('logged')
    return wrapper

@logger
def run(a,b,c):
    print(a+b+c)

run (3,4,5)


    
    
    
###########################################
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='func_logging.log', encoding='utf-8', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    #logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    print('logged')
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

@my_logger
def display_info(name,age):
    print(f'display_info ran with args : {name} & {age}')


display_info('Eran',45)
