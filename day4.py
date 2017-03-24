s1=int(input('请输入去年成绩'));
s2=int(input('请输入今年成绩'));
r=((s2-s1)/s1)*100;
strtemp='提高';
if(s1 > s2):
    r=((s1-s2)/s1)*100;
    strtemp='降低';
elif (s1==s2):
    print('今年成绩与去年一致');
    return;

print('今年成绩比去年%s%.1f%%' % (strtemp,r));
