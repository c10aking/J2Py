#입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. 단, 입력으로 들어오는 수의 개수는 정해져 있지 않음

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args) 
print(avg_numbers(1, 2)) # 1.5 출 력
print(avg_numbers(1,2,3,4,5)) # 3.0 출 력