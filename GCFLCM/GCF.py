def GCF(a, b):
    if b == 0:
        return a
    return GCF(b, a % b)
