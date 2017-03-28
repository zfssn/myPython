l1=['1','2','3','4','5']
l2=['a','b','c','d','e']
for i in l1:
    print(i)
for i in l2:
    print(i)
# 列表生成式
l3=[a+b for a in l1 for b in l2]
print(l3)
for m in l1:
    for n in l2:
        print(m+n)
tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'
jiazi=[tiangan[x%len(tiangan)]+dizhi[x%len(dizhi)] for x in range(60)]
print(jiazi)
print(type(list(range(10))))

l4=[]
for x in range(1,11):
    l4.append(x*x)
print(l4)

# 列表生成式
l5=[x*x for x in range(1,11)]
print(l5)

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower()  if isinstance(s,str) else s for s in L ])
print([s for s in L if not isinstance(s,str)])
# 在for 前写if判断处理取值
l6=[1,2,3,4,5,6]
print([x if x>3 else -x for x in l6 if x%2==0])