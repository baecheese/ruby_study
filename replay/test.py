#-*-coding:utf-8

'''
 반복문을 사용해서 단 하나의 print문으로 구구단을 출력해보세요.
 출력된 결과물은 다음과 같은 형태여야 합니다.

 1 x 1 = 1
 1 x 2 = 2
 1 x 3 = 3
 ......
 9 x 9 = 81

'''

a = 1
b = 1

while a < 10 :
	b = 1
	while b < 10:
		print (str(a) + 'X' + str(b) + '= ' + str(a*b))
		b = b + 1
	a = a + 1