g=(x * x for x in range(10))
print(next(g))
for n in g:
    print(n)
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
for f in fib(5):
    print(f)

def triangles():
        g = [1]
        while True:
            yield g
            g.append(0)
            g = [g[i] + g[i-1] for i in range(len(g))]
# def triangles(): 
#     L = [1] 
#     while True:
#         yield L 
#         L = [1] + [L[i-1]+L[i] for i in range(len(L)) if i>0] + [1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break