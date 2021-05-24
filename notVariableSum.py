# 변수생성 없이 0에서 10까지 더하기
def sum(a):
    if a == 0:
        return 0
    return sum(a-1) + a


print(sum(10))
