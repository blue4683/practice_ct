import sys
input = sys.stdin.readline


def get_prime(n):
    arr = [0] * (n + 1)
    prime = []
    for i in range(2, int(n ** 0.5) + 1):
        p = i ** 2
        for j in range(p, n + 1, i):
            arr[j] = 1

    for i in range(2, n + 1):
        if not arr[i]:
            prime.append(i)

    return prime


n = int(input())
prime = get_prime(n)
m = len(prime)

left, right = 0, 0
psum = 2
result = 0
while left < m:
    if psum <= n:
        if psum == n:
            result += 1

        if right < m - 1:
            right += 1
            psum += prime[right]

        else:
            break

    else:
        psum -= prime[left]
        left += 1

print(result)
