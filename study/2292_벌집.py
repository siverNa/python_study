n = int(input())

num  = 1
cnt = 6
room = 1

if n == 1 :
    print(1)
else :
    while True :
        num = num + cnt
        room += 1
        if n <= num :
            print(room)
            break
        cnt += 6