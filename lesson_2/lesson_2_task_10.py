def bank(x, y):
    for i in range(1, y+1):
        x *=1.1
    return x


n = int(input("Введите сумму: "))
m = int(input("Введите срок: "))
print(bank(n, m))