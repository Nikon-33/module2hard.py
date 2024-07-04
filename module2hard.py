import random

num = random.randint(3, 20)
print("Подберем пароль для значения - ", num)
pass_ = {}

for x in range(1, 20):
    for y in range(1, 20):
        sum = x + y
        if num % int(sum) == 0:
            pass_.update({x: y})
            continue

print(pass_)    # минус данного способа в том, что ключи с одним названием перезаписываются
                # и такие варианты как 1+1 и 1+2 не сохраняются месте

import random

num = random.randint(3, 20)
print("Подберем пароль для значения - ", num)
pass_ = []

for x in range(1, 20):
    for y in range(1, 20):
        sum = x + y
        if num % int(sum) == 0:
            pass_.append(x)
            pass_.append(y)
            continue
print(pass_) # Не смог придумать как исключить повторяющиеся варианты, без потери данных (1 или нескольких пар чисел)

# Следгка доработанный вариант
import random

num = random.randint(3, 20)
print("Подберем пароль для значения - ", num)
pass_ = ""

for x in range(1, 20):
    for y in range(1, 20):
        sum = x + y
        if num % int(sum) == 0:
            pass_ = pass_ + str(x)
            pass_ = pass_ + str(y)
            continue
if num % 2 == 0:
    print(pass_)
else:
    print(pass_[:int(len(pass_)) // 2])
