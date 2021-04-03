import datetime
def logger(func):
    def wrapper(*args, **kwargs):
        with open ('log.txt','a') as logi:
            logi.write('test')
        return func(*args, **kwargs)
        print('logged')
    return wrapper

@logger
def run(a,b,c):
    print(a+b+c)

run (3,4,5)