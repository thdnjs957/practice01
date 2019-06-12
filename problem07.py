# 문제 7.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오
my_list = list() # empty list

for i in range(1, 6):
    number = input('>')
    my_list.append(i)

avg = sum(my_list, 0.0)/len(my_list)
print('평균 : ', avg)