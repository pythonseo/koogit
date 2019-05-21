##def fib(max):
##    n,a,b =0,0,1
##    while n < max:
##        yield b
##        a,b =b,a+b
##        n = n+1
##    return 'done'
##g=fib(6)
##while True:
##    try:
##        x=next(g)
##        print(x)
##    except StopIteration as e:
##        print('error',e)
##        break
def consume(name):
    print('%s start'%name)
    while True:
        baozi=yield
        print('%s start eat %s'%(name,baozi))

def producer():
    a=consume('a')
    b=consume('b')
    baozi='yige'
    a.__next__()
    b.__next__()
    n=0
    while n<5:
        a.send(baozi)
        b.send(baozi)
        n+=1


producer()



