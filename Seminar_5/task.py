
def f(a,b):
    if b == 0:
        return 1
    return a * f(a, b-1)

a = 5 
b =3

print(f(a,b))

def sum(a,b):
    if a == 0 and b == 0 :
        return 0
    if a == 0:
        return 1 + sum(0,b-1)
    if b == 0:
        return 1 + sum(a-1,0)
    return 2 + sum(a-1,b-1)

a = 5
b = 20
print(sum(a,b))