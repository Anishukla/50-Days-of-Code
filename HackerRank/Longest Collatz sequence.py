CL = 5_000_000

def memo(f):
    f.cache = [0] * (CL + 1)
    f.cache[1] = 1

    def _f(n):
        chv = 0
        if n < CL:
            chv = f.cache[n]
        func_val = chv if chv else f(n)
        if not chv and n < CL:
            f.cache[n] = func_val
        return func_val
    return _f


@memo
def collatz(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz(n // 2)
    if n % 2 == 1:
        return 1 + collatz(3 * n + 1)

mxv = [0] * (CL + 1)
mxs = 1
keep_i = 1
for i in range(1, CL+1):
    collatz_i = collatz(i)
    if collatz_i >= mxs:
        keep_i = i
        mxs = collatz_i
    mxv[i] = keep_i

T = int(input())
for _ in range(T):
    n = int(input())
    print(mxv[n])
