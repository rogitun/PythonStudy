def add(a,b):
    return a+b

def manyArgs(*args):

    for i in args:
        print(i,end=' ')

res = add('hansel','kkk')
res2 = add(b=123,a=999)

print(res2)
print(res)

manyArgs(1,2,3,4,5,6,9,"asda")


