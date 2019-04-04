from model.Thread import MyThread
import time

def one(i):
    time.sleep(1)
    four(i)
    print('one', i)

def two(i):
    time.sleep(1)
    print('two', i)

def three():
    time.sleep(1)
    print('three')

def four(i):
    time.sleep(1)
    print('four', i)

def five():
    time.sleep(1)
    print('five')

def six(i):
    time.sleep(1)
    one(i)
    three()
    print('在执行six时 ，执行one，three完成')

if __name__ == '__main__':
    execute = {six: (55,)}
    MyThread(execute).run()