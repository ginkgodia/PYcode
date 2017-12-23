def persistence(n):
    flag=True
    snm = 1
    tries = 0
    x = 1
    if n > 10:
            while flag:

                snm = snm*x
                if n < 10:
                    n = snm*n
                    snm = 1
                    x = 1
                    tries = tries + 1
                    if n < 10:
                        flag = False
                else:

                    x = n % 10
                    n = n / 10
            return tries
    else:
        return tries
import operator
