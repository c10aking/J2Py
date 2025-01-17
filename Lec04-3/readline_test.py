f = open("/Users/c10aking/Mystudy/J2Py/Lec04-3/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break # 모든 줄을 읽고 화면에 출력을 원할 시
    print(line)
f.close()