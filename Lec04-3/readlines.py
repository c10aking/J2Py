f = open("/Users/c10aking/Mystudy/J2Py/Lec04-3/새파일.txt",'r')
lines = f.readlines() # 파일의 모든 줄을 읽어 각 줄을 요소로 가지는 리스트릴 리턴한다.
for line in lines:
    print(line)
f.close()