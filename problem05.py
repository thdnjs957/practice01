# 문제5.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.
# 주어진 리스트에서 3의 배수의 개수=> 6
# 주어진 리스트에서 3의 배수의 합=> 150
my_list = list() # empty list
count = 0
sum = 0;
for i in range(1,20):
    my_list.append(i)
print(my_list[0])

for i in range(len(my_list)):
    if my_list[i] % 3 == 0:
        count += 1
        sum += my_list[i]

print(count, sum)




