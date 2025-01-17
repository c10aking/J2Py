#주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 is_odd 를 작성해 보자. is_odd 함수는 홀수이면 True, 짝수이면 False 를 리턴

def is_odd(number):
    if number % 2 == 1:
        return True
    else :
        return False
    
print(is_odd(4))