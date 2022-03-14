import math

def solution(n, k):
    #소수 판별법 정리
    # 1. 2부터 sqrt(n) 까지 나누었을 때 소수면 소수
    # 2. dp로 소수 판별을 저장한 후 소수 판별
    # 3. 2부터 n - 1 까지 나누었을 때 나누어지지 않으면 소수
    # 4. 에라토스테네스의 체
    answer = 0
    def convert_num(n, k):
        result = ''
        while n > 0:
            result += str(n % k)
            n = n // k
        return result[::-1]
    def is_prime_number(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    tmp = convert_num(n, k).replace('0', ' ')
    l = list(map(int, tmp.split()))
    for number in l:
        if is_prime_number(number):
            answer += 1
    return answer

#참고 풀이
# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:   # math를 이용하지 않는 sqrt
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt