MOD = 10 ** 9 + 7

def mat_mul(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
        ]


def mat_pow(M, e):
    R = [[1, 0], [0, 1]]
    while e:
        if e & 1:
            R = mat_mul(R, M)
            
        M = mat_mul(M, M)
        e >>= 1
        
    return R


a, b, p, q, n = map(int, input().split())
if n == 0:
    print(a % MOD)
    
elif n == 1:
    print(b % MOD)
    
else:
    R = mat_pow([[p % MOD, q % MOD], [1, 0]], n - 1)
    print((R[0][0] * b + R[0][1] * a) % MOD)
    