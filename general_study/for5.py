add = 0

# range 함수 : 숫자 리스트를 자동으로 만들어 준다
# 시작 숫자와 끝 숫자를 지정하려면 range(시작 숫자, 끝 숫자) 형태를 사용하는데,
# 이때 끝 숫자는 포함되지 않는다.
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
'''
len 함수는 리스트 안의 요소 개수를 돌려주는 함수이다. 
따라서 len(marks)는 5가 될 것이고 range(len(marks))는 range(5)가 될 것이다. 
'''
for number in range(len(marks)):
    if marks[number] < 60: 
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))