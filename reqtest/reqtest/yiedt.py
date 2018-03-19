def fun():
    a = 1+1
    print(a+1)
    yield a

    print('done')

b =fun()
print(next(b))

next(b)
#next(b)