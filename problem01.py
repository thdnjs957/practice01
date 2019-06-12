# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

str = input('수를 입력하세요')
if(str.isdigit() == False):
    print('정수를 입력해주세요')
    exit(0)
number = int(str)
if number % 3 == 0:
    print('3의 배수 입니다.')
else:
    print('3의 배수가 아닙니다.')

