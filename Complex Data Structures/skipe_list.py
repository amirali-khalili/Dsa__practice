import random

# ایجاد skip list خالی
def create_skip_list(max_level=2, p=0.5):
    skip_list = {"levels": [[] for _ in range(max_level+1)], "max_level": max_level, "p": p}
    return skip_list

# انتخاب تصادفی سطح برای نود جدید
def random_level(skip_list):
    lvl = 0
    while random.random() < skip_list["p"] and lvl < skip_list["max_level"]:
        lvl += 1
    return lvl

# درج عنصر
def insert(skip_list, value):
    lvl = random_level(skip_list)
    for i in range(lvl+1):
        skip_list["levels"][i].append(value)
        skip_list["levels"][i].sort()  # مرتب‌سازی برای سادگی

# جستجو
def search(skip_list, value):
    lvl = len(skip_list["levels"]) - 1
    while lvl >= 0:
        for v in skip_list["levels"][lvl]:
            if v == value:
                return True
            elif v > value:
                break
        lvl -= 1
    return False

# نمایش لیست
def display(skip_list):
    print("***** Skip List *****")
    for i, level in enumerate(skip_list["levels"]):
        print(f"Level {i}: {level}")

# مثال استفاده
sl = create_skip_list()
for num in [10, 20, 30, 40, 50]:
    insert(sl, num)

display(sl)
print("جستجو 30:", search(sl, 30))
print("جستجو 25:", search(sl, 25))
