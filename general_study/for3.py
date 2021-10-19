score = [90, 25, 67, 45, 80]
member = 0

for s in score:
    member += 1
    if s >= 60:
        print("%d번 학생은 통과입니다." % member)
    else:
        print("%d번 학생은 통과하지 못했습니다." % member)