# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.
str = input('수를 입력하세요')
if(str.isdigit() == False):
    print('정수를 입력해주세요')
    exit(0)
number = int(str)
if number % 2 == 0:
    print('짝수')
else:
    print('홀수')
