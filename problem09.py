# 문제9.
# 주어진 if 문을 dict를 사용해서 수정하세요.

a = dict({'오뎅':300, '순대':400, '만두':500})

menu = input('메뉴: ')
if(menu in a):
    print('price = ', a.get(menu))
    exit(0)
print('0')

