import sys 
from math import gcd

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    N = arr[0] # 배열 크기
    nums = arr[1:] # 실제 숫자 리스트

    total = 0
    for i in range(N):
        for j in range(i+1, N):
            total = total + gcd(nums[i], nums[j])
    
    print(total)