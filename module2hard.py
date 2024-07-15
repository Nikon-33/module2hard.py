import random

num = random.randint(3, 20)
print("Подберем пароль для значения - ", num)
pass_ = ""

for x in range(1, 10):
    for y in range(2, 20):
        sum = x + y
        if x == y or x > y:
            continue
        elif num % int(sum) == 0:
            pass_ = pass_ + str(x)
            pass_ = pass_ + str(y)


print(pass_)
