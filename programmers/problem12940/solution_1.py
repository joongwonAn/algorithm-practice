def solution(n, m):
    def gcd(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b
    
    answer = [gcd(n ,m), (n*m)/gcd(n, m)]
    return answer

test_cases = [
    ((3, 12), [3, 12]),
    ((2, 5), [1, 10]),
    ((10, 15), [5, 30]),
    ((7, 9), [1, 63]),
    ((1000000, 1), [1, 1000000]),
]

def run_tests():
    for i, (inputs, expected) in enumerate(test_cases, 1):
        result = solution(*inputs)
        if result == expected:
            print(f"Test case {i}: PASS")
        else:
            print(f"Test case {i}: FAIL")
            print(f"  Input: {inputs}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

if __name__ == "__main__":
    run_tests()