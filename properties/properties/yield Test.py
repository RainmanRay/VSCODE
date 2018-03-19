def foo():
    print('Ok_1')
    a = 'abc'
    yield a
    print('OK_2')
    yield 2

foo().__next__()
print(type(foo))
print(type(foo()))



print('======================================')
for i in foo():
    print(i)