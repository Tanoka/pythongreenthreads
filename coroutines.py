#generator
def generaOne(x):
    while True:
       x = x + 1
       yield  x

#coroutine..just print value sended
def corouTest():
    while True:
        x = yield
        print("Corou Test: ", x)

#coroutines working concurrently, like a pipe
def corouOne(corou):
    while True:
        x = yield 
        if x % 2 == 0:
            print("Par ", x)
        else:
            print("Impar ", x, end='')
            corou.send(x)

def corouTwo(corou):
    while True:
        x = yield
        if x % 3 == 0:
            print(" multiplo 3 ", x)
        else:
            print(" No mult 3 ", x, end='')
            corou.send(x)

def corouLast():
    while True:
        x = yield
        print(" Final ", x)


#Generator working
for x in generaOne(11):
    print("generator: ", x)
    if x > 15:
        break

#Coroutines
co1 = corouTest()
co1.__next__()
co1.send(12)
co1.send(17)
co1.close()

#Create coroutines, initialice and chain them
c1 = corouLast()
c1.__next__()
c2 = corouTwo(c1)
c2.__next__()
c3 = corouOne(c2)
c3.__next__()

for x in range(1,40):
    c3.send(x)




    

    



