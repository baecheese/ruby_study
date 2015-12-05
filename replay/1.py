'''
print("Hello world 0")
print("Hello world 9")
print("Hello world 18")
print("Hello world 27")

while False:
	print('Hello world')
print('After while')

i = 0
i = i + 1
i = i + 1
print(i)

i = 0
while i < 3:
	print('Hello world ' + str(i*9) )
	i = i + 1

i = 0
while i < 10:
	if i == 4:
		print(i)
	i = i + 1

i = 0
while i < 10:
	if i == 4:
		break
	print(i)
	i = i + 1
print('percent')

홀수일때는 'H' 이라고 출력 / 짝수일 때는 'Z'
1 is 홀수입니다.
2 is 짝수입니다.
20번
'''

i = 1
while i <= 20 :
	number = str(i)
	if i % 2 == 0 :
		print( number + ' is Z')
	else :
		print( number + ' is H')
	i = i + 1