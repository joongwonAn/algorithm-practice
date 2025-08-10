import sys
import math

input = sys.stdin.readline
n, k = map(int, input().split())

result = math.gcd(math.factorial(n), k)
print(result)