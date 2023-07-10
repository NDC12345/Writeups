def pollard_rho(g, s, p):
    def f(x):
        return (x * g) % p

    # Khởi tạo giá trị ban đầu
    x = 1
    y = f(x)
    d = None

    # Áp dụng thuật toán Pollard's rho
    while d is None:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), p)

    if d == 1:
        raise ValueError("Failed to find a factor")

    # Tìm giá trị x
    a = s % p
    b = pow(g, -x, p)
    x = (a * b) % p
    return x

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

g = 8999
s = 11721478752747238947534577901795278971298347908127389421908790123
p = 12297383901740584470151577318651150337988716807049317851420298478128932232846789427512414204247770572072680737351875225891650166807323215624748551744377958007176198392481481171792078565005580006750936049744616851983231170824931892761202881982041842121034608612146861881334101500003915726821683000760611763097

x = pollard_rho(g, s, p)
flag = "tjctf{" + str(x) + "}"
print(flag)
