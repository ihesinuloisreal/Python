def pure_quadratic(u1, u2, d1, d2):
    r1 = u1 * d1
    r2 = u2 * d2
    o1 = r1 + r2
    o2 = u1 - u2
    return o1 / o2

print(pure_quadratic(9, 25, 27, 11))