# -*- coding:utf-8 -*-
# 변수생성 없이 0에서 10까지 더하기

def sum(start, end):
    if end == start:
        return 0
    return sum(start, end-1) + end


print('start부터 end까지의 합을 구해줍니다.')
print('start: ')
start = int(input())
print('end: ')
end = int(input())

print(sum(start, end))
