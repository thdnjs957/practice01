# 문제10
# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.
sum = 0;
str = input('숫자를 입력하세요: ')
number = int(str)
if(number % 2 == 0):
    for i in range(2,number+1,2):
        sum += i
    print(sum)
    exit(0)
for i in range(1,number+1,2):
    sum += i
print(sum)


