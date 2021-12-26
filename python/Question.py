import math

start=7
end=4


def f(ipt):
    opt = 0
    for i in range(start + end + 1):
        x_i = pow(2, start-i)
        ipt_i = math.exp(x_i)

        if (ipt >= ipt_i):
            ipt /= ipt_i
            opt += x_i

    return opt 



print("result: ",f(4))