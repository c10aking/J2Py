f = open("/Users/c10aking/Mystudy/J2Py/Lec04-3/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data) #쓰기
f.close()