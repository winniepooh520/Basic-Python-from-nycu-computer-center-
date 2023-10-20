def avg(L):
    return sum(L) / len(L)
def printList(L):
    i = 0
    n = len(L)
    while i < n:
        print('[', i, ']', L[i], sep = '')
        i += 1
def sumList(L1, L2, start = 0, stop = 0):
    if stop <= start:
        stop = min(len(L1), len(L2)) 
    i = start
    Lr = []
    while i < stop:
        Lr.append(L1[i] + L2[i])
        i += 1
    return Lr
def swap(a, b):
    return b, a