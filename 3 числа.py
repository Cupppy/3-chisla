f=int(input('введите число'))
s=int(input('введите число'))
t=int(input('введите число'))
if f == t == s:
    print('3')
elif f == t or f == s or t == s :
    print('2')
else:
    print('0')