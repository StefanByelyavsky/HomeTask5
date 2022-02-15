lst_bs = list(input('список:'))
a = len(lst_bs)
if a == 0:
    lst_l = list()
    lst_r = list()
elif a == 1:
    lst_l = lst_bs[0]
    lst_r = list()
elif a >= 2:
    a, b = divmod(a, 2)
    if b == 0:
        a += 0
    else: a += 1
    lst_l = lst_bs[:a]
    lst_r = lst_bs[a:]
print(lst_bs)
print(lst_l)
print(lst_r)