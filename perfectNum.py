import sys

sys.setrecursionlimit(150000)

def perfectNum(n):
    return [x for x in range(2, n) if commonDiv(x, x-1) == x]

def commonDiv(num: int, temp: int) -> list:
    if temp == 1:
        return 1
    elif num % temp == 0:
        return commonDiv(num, temp-1) + temp
    return commonDiv(num, temp-1)

def primeNums(n: int):
    return [x for x in range(1, n) if primeNum()]

def primeNum(num: int, temp: int) -> list:
    if commonDiv(num, temp) == 1:
        return True
    else:
        return False
    
print(perfectNum(8129))