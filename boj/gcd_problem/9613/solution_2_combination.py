import sys 
from math import gcd
from itertools import combinations

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    N = arr[0] # 배열 크기
    nums = arr[1:] # 실제 숫자 리스트

    total = 0
    # conbination 사용
    for a, b in combinations(nums, 2):
        total += gcd(a, b)
    
    print(total)