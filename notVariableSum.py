def sum(a):
    if a == 0:
        return 0
    return sum(a-1) + a


print(sum(10))
