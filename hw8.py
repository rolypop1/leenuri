shopping_bag = {}

while True:
    print('[구입]')
    item = input('상품명? ')
    if item == '':
        print(f'>>> 장바구니 보기: {shopping_bag}')
        print('')
        break
    count = input('수량은? ')
    shopping_bag[item] = count
    print(f'장바구니에 {item} {count}개가 담겼습니다')
    print('')

print('[검색]')
item = input('장바구니에서 확인하고자 하는 상품은? ')
if item in shopping_bag:
    print(f'{item}은(는) {shopping_bag[item]}개 담겨 있습니다.')
else:
    print(f'장바구니에 {item}은(는) 없습니다.')
