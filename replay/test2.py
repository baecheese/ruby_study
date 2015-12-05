#-*-coding:utf-8

'''
단 하나의 print 문을 사용하여 다음을 출력하라.

     *     
    ***
   *****
    ***
     *
'''

n = 0

while n < 6:
	a = '  *'
	b = ' ***'
	c = '*****'
	if n == 1 or 5 :
		print (a)
	elif n == 2 or 4:
		print(b)
	else:
		print(c)
n = n + 1